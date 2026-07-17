#!/usr/bin/env python3
"""Validate the survey repository's headline corpus and capability counts."""

from __future__ import annotations
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "data" / "processed" / "core_studies.csv"
OUT = ROOT / "analysis" / "derived_summary.json"

CAPS = [
    "Provenance",
    "Source attribution",
    "Causal reconstruction",
    "Blast-radius support",
    "Recovery support",
]

EXPECTED = {
    "core_n": 39,
    "roles": {"Attack/failure": 19, "Defence/system": 12, "Benchmark": 8},
    "status": {"Preprint": 30, "Peer-reviewed": 8, "Peer-reviewed workshop": 1},
    "capabilities": {
        "Provenance": {"Yes": 6, "Partial": 13, "No": 20},
        "Source attribution": {"Yes": 8, "Partial": 28, "No": 3},
        "Causal reconstruction": {"Yes": 9, "Partial": 26, "No": 4},
        "Blast-radius support": {"Yes": 7, "Partial": 16, "No": 16},
        "Recovery support": {"Yes": 7, "Partial": 11, "No": 21},
    },
    "yes_by_role": {
        "Provenance": {"Attack/failure": 0, "Defence/system": 6, "Benchmark": 0},
        "Source attribution": {"Attack/failure": 0, "Defence/system": 7, "Benchmark": 1},
        "Causal reconstruction": {"Attack/failure": 6, "Defence/system": 1, "Benchmark": 2},
        "Blast-radius support": {"Attack/failure": 2, "Defence/system": 4, "Benchmark": 1},
        "Recovery support": {"Attack/failure": 0, "Defence/system": 5, "Benchmark": 2},
    },
    "nonbenchmark_yes": {
        "Provenance": 6,
        "Source attribution": 7,
        "Causal reconstruction": 7,
        "Blast-radius support": 6,
        "Recovery support": 5,
    },
    "peer_plus_workshop_yes": {cap: 1 for cap in CAPS},
}

def role_for(row: dict[str, str]) -> str:
    group = row["Evidence group"].strip().lower()
    sid = int(row["ID"])
    benchmark_ids = {19, 59, 60, 61, 62, 65, 66, 67}
    defence_ids = {34, 35, 36, 37, 38, 39, 40, 42, 50, 53, 54, 55}
    if sid in benchmark_ids:
        return "Benchmark"
    if sid in defence_ids:
        return "Defence/system"
    return "Attack/failure"

def main() -> int:
    with CORE.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    errors: list[str] = []
    ids = [int(r["ID"]) for r in rows]
    if len(rows) != EXPECTED["core_n"]:
        errors.append(f"Expected 39 core rows, found {len(rows)}")
    if len(set(ids)) != len(ids):
        errors.append("Duplicate core study IDs detected")

    roles = Counter(role_for(r) for r in rows)
    status = Counter(r["Publication status"] for r in rows)
    capabilities = {cap: Counter(r[cap] for r in rows) for cap in CAPS}

    yes_by_role = {cap: Counter() for cap in CAPS}
    for r in rows:
        role = role_for(r)
        for cap in CAPS:
            if r[cap] == "Yes":
                yes_by_role[cap][role] += 1

    nonbenchmark = [r for r in rows if role_for(r) != "Benchmark"]
    peer_plus_workshop = [
        r for r in rows
        if r["Publication status"] in {"Peer-reviewed", "Peer-reviewed workshop"}
    ]
    nonbenchmark_yes = {
        cap: sum(1 for r in nonbenchmark if r[cap] == "Yes") for cap in CAPS
    }
    peer_yes = {
        cap: sum(1 for r in peer_plus_workshop if r[cap] == "Yes") for cap in CAPS
    }

    if dict(roles) != EXPECTED["roles"]:
        errors.append(f"Role counts differ: {dict(roles)}")
    if dict(status) != EXPECTED["status"]:
        errors.append(f"Publication-status counts differ: {dict(status)}")

    for cap in CAPS:
        if dict(capabilities[cap]) != EXPECTED["capabilities"][cap]:
            errors.append(f"{cap} counts differ: {dict(capabilities[cap])}")
        if dict(yes_by_role[cap]) != {
            k: v for k, v in EXPECTED["yes_by_role"][cap].items() if v != 0
        }:
            # Counter omits zeros; compare after filling.
            observed = {role: yes_by_role[cap].get(role, 0) for role in EXPECTED["roles"]}
            if observed != EXPECTED["yes_by_role"][cap]:
                errors.append(f"{cap} role counts differ: {observed}")
        if nonbenchmark_yes[cap] != EXPECTED["nonbenchmark_yes"][cap]:
            errors.append(f"{cap} non-benchmark count differs: {nonbenchmark_yes[cap]}")
        if peer_yes[cap] != EXPECTED["peer_plus_workshop_yes"][cap]:
            errors.append(f"{cap} peer-reviewed subset differs: {peer_yes[cap]}")

    summary = {
        "repository_version": "1.0.0-rc1",
        "core_n": len(rows),
        "unique_ids": len(set(ids)),
        "roles": dict(roles),
        "publication_status": dict(status),
        "capabilities": {cap: dict(capabilities[cap]) for cap in CAPS},
        "yes_by_role": {
            cap: {role: yes_by_role[cap].get(role, 0) for role in EXPECTED["roles"]}
            for cap in CAPS
        },
        "nonbenchmark_yes": nonbenchmark_yes,
        "peer_plus_workshop_yes": peer_yes,
        "validation_passed": not errors,
        "errors": errors,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Validation passed.")
    print(json.dumps(summary, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
