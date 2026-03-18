#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Marker:
    kind: str
    value: str

    def matches(self, text: str) -> bool:
        if self.kind == "contains":
            return self.value in text
        if self.kind == "regex":
            return re.search(self.value, text, re.MULTILINE) is not None
        raise ValueError(f"unsupported marker kind: {self.kind}")


def fail(message: str) -> None:
    raise SystemExit(message)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        fail(f"missing required file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")


def parse_marker(raw_marker: object, context: str) -> Marker:
    if isinstance(raw_marker, str):
        return Marker("contains", raw_marker)
    if isinstance(raw_marker, dict) and set(raw_marker.keys()) == {"regex"}:
        regex = raw_marker["regex"]
        if not isinstance(regex, str) or not regex:
            fail(f"{context}: regex marker must be a non-empty string")
        return Marker("regex", regex)
    fail(f"{context}: marker must be a string or an object with only a regex field")


def load_invariants(repo_root: Path) -> tuple[list[dict[str, object]], dict[str, dict[str, object]]]:
    raw_data = load_json(repo_root / "conformance/invariants.json")
    if not isinstance(raw_data, dict):
        fail("conformance/invariants.json: top-level object must be a JSON object")

    version = raw_data.get("version")
    invariants = raw_data.get("invariants")
    if not isinstance(version, int):
        fail("conformance/invariants.json: version must be an integer")
    if not isinstance(invariants, list) or not invariants:
        fail("conformance/invariants.json: invariants must be a non-empty list")

    invariant_items: list[dict[str, object]] = []
    invariant_by_id: dict[str, dict[str, object]] = {}

    for index, raw_invariant in enumerate(invariants):
        context = f"conformance/invariants.json invariant #{index + 1}"
        if not isinstance(raw_invariant, dict):
            fail(f"{context}: invariant must be an object")

        invariant_id = raw_invariant.get("id")
        description = raw_invariant.get("description")
        markers = raw_invariant.get("markers")

        if not isinstance(invariant_id, str) or not invariant_id:
            fail(f"{context}: id must be a non-empty string")
        if not isinstance(description, str) or not description:
            fail(f"{context}: description must be a non-empty string")
        if invariant_id in invariant_by_id:
            fail(f"{context}: duplicate invariant id {invariant_id}")
        if not isinstance(markers, dict) or not markers:
            fail(f"{context}: markers must be a non-empty object")

        parsed_markers: dict[str, list[Marker]] = {}
        for relative_path, raw_markers in markers.items():
            if not isinstance(relative_path, str) or not relative_path:
                fail(f"{context}: marker path must be a non-empty string")
            if not isinstance(raw_markers, list) or not raw_markers:
                fail(f"{context}: markers for {relative_path} must be a non-empty list")
            parsed_markers[relative_path] = [
                parse_marker(marker, f"{context} {relative_path}") for marker in raw_markers
            ]

        item = {
            "id": invariant_id,
            "description": description,
            "markers": parsed_markers,
        }
        invariant_items.append(item)
        invariant_by_id[invariant_id] = item

    return invariant_items, invariant_by_id


def load_scenarios(repo_root: Path, invariant_by_id: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    scenario_dir = repo_root / "conformance/scenarios"
    if not scenario_dir.is_dir():
        fail(f"missing required directory: {scenario_dir}")

    scenario_paths = sorted(scenario_dir.glob("*.json"))
    if not scenario_paths:
        fail("conformance/scenarios: expected at least one scenario JSON file")

    required_fields = {
        "id": str,
        "title": str,
        "category": str,
        "user_prompt": str,
        "failure_mode": str,
        "required_invariants": list,
        "forbidden_behaviors": list,
        "without_devotion_example": str,
        "with_devotion_example": str,
    }

    scenario_items: list[dict[str, object]] = []
    scenario_ids: set[str] = set()

    for path in scenario_paths:
        raw_scenario = load_json(path)
        if not isinstance(raw_scenario, dict):
            fail(f"{path}: top-level object must be a JSON object")

        for field_name, expected_type in required_fields.items():
            value = raw_scenario.get(field_name)
            if not isinstance(value, expected_type):
                fail(f"{path}: {field_name} must be of type {expected_type.__name__}")
            if expected_type is str and not value:
                fail(f"{path}: {field_name} must be a non-empty string")

        scenario_id = raw_scenario["id"]
        if scenario_id in scenario_ids:
            fail(f"{path}: duplicate scenario id {scenario_id}")
        scenario_ids.add(scenario_id)

        required_invariants = raw_scenario["required_invariants"]
        forbidden_behaviors = raw_scenario["forbidden_behaviors"]
        if not required_invariants:
            fail(f"{path}: required_invariants must not be empty")
        if not forbidden_behaviors:
            fail(f"{path}: forbidden_behaviors must not be empty")
        if not all(isinstance(item, str) and item for item in required_invariants):
            fail(f"{path}: required_invariants must contain non-empty strings")
        if not all(isinstance(item, str) and item for item in forbidden_behaviors):
            fail(f"{path}: forbidden_behaviors must contain non-empty strings")

        for invariant_id in required_invariants:
            if invariant_id not in invariant_by_id:
                fail(f"{path}: unknown invariant id {invariant_id}")

        scenario_items.append(raw_scenario)

    return scenario_items


def check_marker_coverage(
    repo_root: Path,
    scenarios: list[dict[str, object]],
    invariant_by_id: dict[str, dict[str, object]],
) -> None:
    required_ids = []
    for scenario in scenarios:
        for invariant_id in scenario["required_invariants"]:
            if invariant_id not in required_ids:
                required_ids.append(invariant_id)

    file_cache: dict[str, str] = {}

    for invariant_id in required_ids:
        invariant = invariant_by_id[invariant_id]
        for relative_path, markers in invariant["markers"].items():
            absolute_path = repo_root / relative_path
            if not absolute_path.is_file():
                fail(f"missing marker target file for {invariant_id}: {relative_path}")
            if relative_path not in file_cache:
                file_cache[relative_path] = absolute_path.read_text(encoding="utf-8")
            file_text = file_cache[relative_path]
            if not any(marker.matches(file_text) for marker in markers):
                fail(f"{relative_path}: missing marker coverage for invariant {invariant_id}")


def render_behavior_doc(
    invariants: list[dict[str, object]],
    scenarios: list[dict[str, object]],
) -> str:
    lines = [
        "# Behavioral Conformance Examples",
        "",
        "This file is generated by `python3 scripts/check-conformance.py --write`. Do not edit it manually.",
        "",
        "## Invariants",
        "",
    ]

    for invariant in invariants:
        lines.append(f"- `{invariant['id']}`: {invariant['description']}")

    lines.extend(["", "## Scenarios", ""])

    for scenario in scenarios:
        required = ", ".join(f"`{item}`" for item in scenario["required_invariants"])
        lines.extend(
            [
                f"### {scenario['title']}",
                "",
                f"- `ID`: `{scenario['id']}`",
                f"- `Category`: `{scenario['category']}`",
                f"- `Failure mode`: {scenario['failure_mode']}",
                f"- `Required invariants`: {required}",
                "",
                f"#### Forbidden Behaviors For `{scenario['id']}`",
                "",
            ]
        )
        for behavior in scenario["forbidden_behaviors"]:
            lines.append(f"- {behavior}")

        lines.extend(
            [
                "",
                f"#### User Prompt For `{scenario['id']}`",
                "",
                "```text",
                scenario["user_prompt"],
                "```",
                "",
                f"#### Without Devotion For `{scenario['id']}`",
                "",
                "```text",
                scenario["without_devotion_example"],
                "```",
                "",
                f"#### With Devotion For `{scenario['id']}`",
                "",
                "```text",
                scenario["with_devotion_example"],
                "```",
                "",
            ]
        )

    while lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines)


def verify_or_write_behavior_doc(repo_root: Path, rendered_doc: str, write: bool) -> None:
    output_path = repo_root / "docs/README.behavior.md"
    if write:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered_doc + "\n", encoding="utf-8")
        return

    if not output_path.is_file():
        fail(f"missing generated behavior doc: {output_path}")

    existing = output_path.read_text(encoding="utf-8")
    if existing != rendered_doc + "\n":
        fail(
            "docs/README.behavior.md is stale; run `python3 scripts/check-conformance.py --write`"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check devotion conformance fixtures")
    parser.add_argument("repo_root", nargs="?", default=".")
    parser.add_argument("--write", action="store_true", help="write docs/README.behavior.md")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()

    invariants, invariant_by_id = load_invariants(repo_root)
    scenarios = load_scenarios(repo_root, invariant_by_id)
    check_marker_coverage(repo_root, scenarios, invariant_by_id)
    rendered_doc = render_behavior_doc(invariants, scenarios)
    verify_or_write_behavior_doc(repo_root, rendered_doc, args.write)
    print(
        f"Validated {len(scenarios)} conformance scenarios across {len(invariants)} invariants in {repo_root}"
    )


if __name__ == "__main__":
    main()
