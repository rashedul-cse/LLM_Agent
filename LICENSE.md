#!/usr/bin/env python3
"""Validate the released survey repository's corpus and capability counts."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "data" / "processed" / "core_studies.csv"
ADJACENT = ROOT / "data" / "processed" / "adjacent_literature.csv"
CANDIDATES = ROOT / "data" / "source" / "literature_corpus.csv"
PDF_INTAKE = ROOT / "data" / "source" / "pdf_intake.csv"
APPENDIX = ROOT / "data" / "supplementary" / "appendix_a_core_census.csv"
CROSSWALK = ROOT / "data" / "processed" / "id_crosswalk.csv"
OUT = ROOT / "analysis" / "derived_summary.json"

CAPS = [
    "Provenance",
    "Source attribution",
    "Causal reconstruction",
    "Blast-radius support",
    "Recovery support",
]

ATTACK_IDS = {10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 24, 26, 29, 30, 31, 32, 33, 68, 69}
DEFENCE_IDS = {34, 35, 36, 37, 38, 39, 40, 42, 50, 53, 54, 55, 70, 71}
BENCHMARK_IDS = {19, 59, 60, 61, 62, 65, 66, 67}

EXPECTED = {
    "candidate_n": 86,
    "usable_full_texts": 79,
    "adjacent_n": 36,
    "core_n": 43,
    "roles": {"Attack/failure": 21, "Defence/system": 14, "Benchmark": 8},
    "status": {"Preprint": 34, "Peer-reviewed": 8, "Peer-reviewed workshop": 1},
    "capabilities": {
        "Provenance": {"Yes": 7, "Partial": 14, "No": 22},
        "Source attribution": {"Yes": 10, "Partial": 28, "No": 5},
        "Causal reconstruction": {"Yes": 11, "Partial": 28, "No": 4},
        "Blast-radius support": {"Yes": 9, "Partial": 16, "No": 18},
        "Recovery support": {"Yes": 7, "Partial": 12, "No": 24},
    },
    "yes_by_role": {
        "Provenance": {"Attack/failure": 0, "Defence/system": 7, "Benchmark": 0},
        "Source attribution": {"Attack/failure": 1, "Defence/system": 8, "Benchmark": 1},
        "Causal reconstruction": {"Attack/failure": 7, "Defence/system": 2, "Benchmark": 2},
        "Blast-radius support": {"Attack/failure": 3, "Defence/system": 5, "Benchmark": 1},
        "Recovery support": {"Attack/failure": 0, "Defence/system": 5, "Benchmark": 2},
    },
    "nonbenchmark_yes": {
        "Provenance": 7,
        "Source attribution": 9,
        "Causal reconstruction": 9,
        "Blast-radius support": 8,
        "Recovery support": 5,
    },
    "peer_reviewed_only_yes": {cap: 1 for cap in CAPS},
    "crosswalk_n": 4,
}

def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def role_for(row: dict[str, str]) -> str:
    sid = int(row["ID"])
    if sid in BENCHMARK_IDS:
        return "Benchmark"
    if sid in DEFENCE_IDS:
        return "Defence/system"
    if sid in ATTACK_IDS:
        return "Attack/failure"
    raise ValueError(f"Unclassified core study ID: {sid}")

def main() -> int:
    core = read_rows(CORE)
    adjacent = read_rows(ADJACENT)
    candidates = read_rows(CANDIDATES)
    pdf_intake = read_rows(PDF_INTAKE)
    appendix = read_rows(APPENDIX)
    crosswalk = read_rows(CROSSWALK)

    errors: list[str] = []

    core_ids = [int(r["ID"]) for r in core]
    if len(core) != EXPECTED["core_n"]:
        errors.append(f"Expected {EXPECTED['core_n']} core rows, found {len(core)}")
    if len(set(core_ids)) != len(core_ids):
        errors.append("Duplicate core study IDs detected")
    if len(adjacent) != EXPECTED["adjacent_n"]:
        errors.append(f"Expected {EXPECTED['adjacent_n']} adjacent rows, found {len(adjacent)}")
    if len(candidates) != EXPECTED["candidate_n"]:
        errors.append(f"Expected {EXPECTED['candidate_n']} candidate rows, found {len(candidates)}")
    if len(appendix) != EXPECTED["core_n"]:
        errors.append(f"Expected {EXPECTED['core_n']} Appendix A rows, found {len(appendix)}")
    if len(crosswalk) != EXPECTED["crosswalk_n"]:
        errors.append(f"Expected {EXPECTED['crosswalk_n']} crosswalk rows, found {len(crosswalk)}")

    usable_status = {"Complete PDF", "Verified public full text"}
    usable_full_texts = sum(r.get("PDF status") in usable_status for r in pdf_intake)
    if usable_full_texts != EXPECTED["usable_full_texts"]:
        errors.append(
            f"Expected {EXPECTED['usable_full_texts']} usable full texts, found {usable_full_texts}"
        )

    roles = Counter(role_for(r) for r in core)
    status = Counter(r["Publication status"] for r in core)
    capabilities = {cap: Counter(r[cap] for r in core) for cap in CAPS}

    yes_by_role = {cap: Counter() for cap in CAPS}
    for row in core:
        role = role_for(row)
        for cap in CAPS:
            if row[cap] == "Yes":
                yes_by_role[cap][role] += 1

    nonbenchmark = [r for r in core if role_for(r) != "Benchmark"]
    peer_reviewed = [r for r in core if r["Publication status"] == "Peer-reviewed"]
    nonbenchmark_yes = {
        cap: sum(r[cap] == "Yes" for r in nonbenchmark) for cap in CAPS
    }
    peer_reviewed_yes = {
        cap: sum(r[cap] == "Yes" for r in peer_reviewed) for cap in CAPS
    }

    if dict(roles) != EXPECTED["roles"]:
        errors.append(f"Role counts differ: {dict(roles)}")
    if dict(status) != EXPECTED["status"]:
        errors.append(f"Publication-status counts differ: {dict(status)}")

    for cap in CAPS:
        observed_cap = {k: capabilities[cap].get(k, 0) for k in ("Yes", "Partial", "No")}
        if observed_cap != EXPECTED["capabilities"][cap]:
            errors.append(f"{cap} counts differ: {observed_cap}")
        observed_role = {
            role: yes_by_role[cap].get(role, 0)
            for role in ("Attack/failure", "Defence/system", "Benchmark")
        }
        if observed_role != EXPECTED["yes_by_role"][cap]:
            errors.append(f"{cap} role counts differ: {observed_role}")
        if nonbenchmark_yes[cap] != EXPECTED["nonbenchmark_yes"][cap]:
            errors.append(
                f"{cap} non-benchmark count differs: {nonbenchmark_yes[cap]}"
            )
        if peer_reviewed_yes[cap] != EXPECTED["peer_reviewed_only_yes"][cap]:
            errors.append(
                f"{cap} peer-reviewed-only count differs: {peer_reviewed_yes[cap]}"
            )

    summary = {
        "repository_version": "1.0.0",
        "candidate_records": len(candidates),
        "usable_full_texts": usable_full_texts,
        "adjacent_background": len(adjacent),
        "core_n": len(core),
        "unique_core_ids": len(set(core_ids)),
        "roles": dict(roles),
        "publication_status": dict(status),
        "capabilities": {
            cap: {k: capabilities[cap].get(k, 0) for k in ("Yes", "Partial", "No")}
            for cap in CAPS
        },
        "yes_by_role": {
            cap: {
                role: yes_by_role[cap].get(role, 0)
                for role in ("Attack/failure", "Defence/system", "Benchmark")
            }
            for cap in CAPS
        },
        "nonbenchmark_yes": nonbenchmark_yes,
        "peer_reviewed_only_yes": peer_reviewed_yes,
        "crosswalk_rows": len(crosswalk),
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
