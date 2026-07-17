# Forensic Readiness of Persistent-Memory LLM Agents — Evidence Repository

**Repository version:** 1.0.0-rc1  
**Evidence cut-off:** 13 July 2026  
**Author:** Md Rashedul Islam  
**Affiliation:** School of Information Technology, Deakin University, Melbourne, Australia

This repository contains the screening records, study-level coding, supplementary evidence tables, and reproducibility checks supporting the survey:

> *Forensic Readiness of Persistent-Memory LLM Agents: Provenance, Incident Reconstruction, Recovery, and Open Challenges*

## Scope

The survey is a **structured scoping survey and systematisation of knowledge**, not an exhaustive PRISMA review. Its unit of analysis is the persistent-memory incident: the evidence required to reconstruct a source-to-action path, state causal confidence, determine contamination scope, and evaluate recovery.

The current bounded evidence set contains:

- 82 candidate records;
- 75 usable full texts;
- 39 core primary studies;
- 36 adjacent or background papers;
- 19 attack or failure studies;
- 12 defence, provenance, governance, system, or recovery studies;
- 8 benchmark studies.

The 39-study capability coding reports:

| Capability | Yes | Partial | No |
|---|---:|---:|---:|
| Provenance or lineage | 6 | 13 | 20 |
| Source attribution | 8 | 28 | 3 |
| Causal reconstruction | 9 | 26 | 4 |
| Blast-radius analysis | 7 | 16 | 16 |
| Recovery support | 7 | 11 | 21 |

These are descriptive counts for the bounded corpus, not estimates of field-wide prevalence.

## Repository structure

```text
.
├── data/
│   ├── source/          Original cumulative and clean workbooks, search/screening exports
│   ├── processed/       Core corpus and study-level synthesis tables
│   └── supplementary/   Appendix census, capability tables, sensitivity analyses
├── docs/                Methods, codebook, data dictionary, limitations, release checklist
├── search/              Search families, example query, and search-log guidance
├── scripts/             Standard-library reproducibility checks
├── analysis/            Machine-generated validation summary
├── metadata/            Zenodo-ready metadata
├── CITATION.cff
├── LICENSE.md
└── README.md
```

## Reproduce and validate the headline counts

Python 3.10 or later is sufficient; no third-party packages are required.

```bash
python scripts/validate_counts.py
```

The script validates:

- core-corpus size and unique study identifiers;
- attack/defence/benchmark role totals;
- publication-status totals;
- Yes/Partial/No capability totals;
- role-disaggregated explicit support;
- non-benchmark and peer-reviewed-subset sensitivity values.

A successful run writes `analysis/derived_summary.json`.

## Primary files

- `data/processed/core_studies.csv` — complete study-level core extraction.
- `data/supplementary/appendix_a_core_census.csv` — compact manuscript appendix.
- `data/supplementary/capability_overall.csv` — 6/8/9/7/7 headline coding.
- `data/supplementary/capability_by_role.csv` — role-disaggregated coding.
- `data/supplementary/capability_subset_sensitivity.csv` — full, non-benchmark, and peer-reviewed subsets.
- `data/supplementary/attack_distribution.csv` — current attack-dimension values.
- `data/supplementary/meirc_retrospective_provisional.csv` — provisional retrospective framework mapping; page-level verification remains required.

## Important release status

This package is structurally ready for GitHub or Zenodo deposit. Two scholarly tasks remain separate from repository packaging:

1. **Independent coding reliability:** the repository contains the primary coding and quantified sensitivity analysis, but no independently produced second-coder labels or Cohen's kappa. These must not be claimed unless genuinely completed.
2. **Exact database execution details:** the current search records do not consistently preserve every database-specific execution date and raw hit count. Missing values are identified in `docs/DEPOSIT_READINESS.md` and must not be invented.

## Copyright and full texts

The repository does **not** redistribute the reviewed PDF papers. The source PDFs remain subject to their publishers' or authors' copyright terms. This repository distributes only metadata, screening decisions, coded observations, and author-created supplementary materials.

## Citation

Use `CITATION.cff`. After Zenodo deposit, add the assigned DOI to `CITATION.cff`, `README.md`, and `metadata/zenodo.json`.

## Licence

Data and documentation are released under **CC BY 4.0**. Repository scripts are released under the **MIT Licence**. See `LICENSE.md`.
