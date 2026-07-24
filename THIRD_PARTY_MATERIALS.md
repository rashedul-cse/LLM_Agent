# Data Dictionary

## `data/processed/core_studies.csv`

| Field | Meaning |
|---|---|
| ID | Stable corpus study identifier |
| Full title | Verified study title |
| Authors | Author string recorded during extraction |
| Year | Publication or preprint year |
| Publication status | Peer-reviewed, peer-reviewed workshop, or preprint |
| Venue | Verified or currently reported venue |
| DOI / arXiv / ID | Persistent bibliographic identifier where available |
| PDF file | Local intake filename used during screening; full text is not redistributed |
| Evidence group | Study-level role or topic |
| Memory form | Primary persistent-memory representation or store |
| Agent setting | Evaluated agent/application context |
| Primary lifecycle phase | Main acquire/write/store/retrieve/execute/share/recover operations |
| Attack / control mechanism | Main technical mechanism |
| Attacker access / trust assumption | Access model or trusted-component assumption |
| Activation / persistence | Trigger, delay, recurrence, propagation, or temporal pattern |
| Concise study contribution | Extracted contribution summary |
| Key reported result | Study-reported result; values marked for verification require page-level checking |
| Forensic artefacts available | Artefacts exposed by the reported study |
| Provenance | Yes / Partial / No |
| Source attribution | Yes / Partial / No |
| Causal reconstruction | Yes / Partial / No |
| Blast-radius support | Yes / Partial / No |
| Recovery support | Yes / Partial / No |
| PDF status | Intake status |
| Uploaded filename | Local intake filename |
| Main manuscript role | Intended use in the survey |
| Selection status | Core inclusion state |
| Extraction status | Full-text extraction state |
| Verification note | Remaining metadata or claim-verification note |

## Other principal files

- `appendix_a_core_census.csv`: compact census for the manuscript appendix.
- `capability_overall.csv`: overall Yes/Partial/No counts and percentages.
- `capability_by_role.csv`: explicit-Yes counts by mutually exclusive study role.
- `capability_subset_sensitivity.csv`: full, non-benchmark, and peer-reviewed-only results.
- `recoding_thresholds.csv`: number of Partial→Yes changes needed to cross selected thresholds.
- `attack_distribution.csv`: corpus-level attack-dimension summaries.
- `benchmark_symbols.csv`: direct/partial/absent benchmark coverage.
- `survey_coverage_scores.csv`: directional coverage of this survey's seven analytical capabilities.
- `screening_tracker.csv`: cumulative screening record from the source workbook.
- `search_log.csv`: search-log information present in the cumulative workbook.
