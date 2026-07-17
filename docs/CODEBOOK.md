# Operational Coding Codebook

## Corpus role

### Attack/failure
A primary study whose main contribution is an adversarial attack, privacy attack, contamination mechanism, propagation mechanism, or non-adversarial persistent-state failure.

### Defence/system
A primary study whose main contribution is prevention, detection, provenance, access control, governance, evidence capture, attribution, rollback, unlearning, or recovery architecture.

### Benchmark
A primary study whose main contribution is an evaluation suite, dataset, environment, or structured benchmark. A benchmark can contain attacks without being counted as an attack paper for the mutually exclusive role totals.

## Forensic-capability coding

| Capability | Yes | Partial | No |
|---|---|---|---|
| Provenance / lineage | Implements or formally specifies explicit source and transformation lineage | Records source metadata, logs, or partial lineage without end-to-end derivation | No dedicated provenance support |
| Source attribution | Identifies the responsible source, memory, actor, or channel and evaluates or formalises that attribution | Records candidate source or memory identity without explicit attribution assessment | No source-attribution support |
| Causal reconstruction | Uses controlled intervention, counterfactual replay, mechanistic dependency, or equivalent explicit causal analysis | Shows retrieval, correlation, trajectory association, or behavioural influence without controlled causal evidence | No causal reconstruction |
| Blast-radius analysis | Enumerates or analyses derived, copied, shared, propagated, or affected memories/agents | Discusses propagation or examines only a limited downstream copy | No contamination-scope analysis |
| Recovery | Performs dependency-aware cleanup, rollback, revocation, forgetting, or repair with post-recovery validation | Deletes, blocks, quarantines, or rolls back without complete non-reappearance validation | No recovery mechanism |

## Interpretation rule

The exact ordering of capability percentages can be sensitive to individual Partial→Yes decisions. Therefore:

- report raw fractions before percentages;
- treat all five capabilities as minority explicit-support categories;
- do not interpret small differences between capabilities as precise field-wide rankings;
- preserve study-level rationale in the workbook.

## Attack-distribution coding

The current normalized entry-channel categories are mutually exclusive. Targeted operation, memory target, temporal behaviour, and propagation scope are multi-label and may sum above 19.

The present repository does **not** contain a completed normalized forensic-effect code for every attack paper. Do not infer trace-poor, provenance-laundering, evidence-deleting, log-flooding, or rollback-concealment labels solely from the five capability columns.
