# Review Design and Corpus Construction

## Review type

The study uses a structured scoping survey and systematisation-of-knowledge design. The goal is a bounded, transparent corpus focused on persistent operational memory and post-compromise evidence, rather than an exhaustive census of all papers using broad combinations of “agent,” “memory,” and “security.”

## Corpus flow

1. **Candidate identification:** 82 records from focused searches, seed papers, related surveys, and backward/forward snowballing.
2. **Full-text verification:** 75 usable and bibliographically identifiable full texts.
3. **Core inclusion:** 39 primary studies concerning persistent operational memory or closely coupled durable state and contributing empirical, formal, systems, or benchmark evidence relevant to security or forensic readiness.
4. **Adjacent/background role:** 36 surveys, standards, capability studies, static-RAG studies, general agent-security papers, or forensic foundations retained for context.
5. **Unavailable candidates:** 7 records lacked usable full text before the evidence cut-off and were excluded from corpus-derived counts.

## Inclusion criteria

A study enters the core corpus when:

- retained state survives beyond one inference, session, or task;
- the retained state can influence a later response, plan, tool action, user, agent, or recovery decision;
- the paper contributes evidence about attack, failure, defence, provenance, attribution, reconstruction, propagation, governance, forgetting, or recovery;
- the evidence is empirical, formal, system-oriented, or benchmark-based.

Surveys, standards, commentary, static operator-curated RAG papers, transient prompt-injection work, conventional RAM forensics, and parametric-memory-only studies are adjacent unless persistent operational memory is directly evaluated.

## Version handling

Preprint and peer-reviewed versions of the same work are treated as one study. The most authoritative verified version is preferred. Publication status is recorded separately from evidence role and is not used as a quality score.

## Coding

Each core study is coded for bibliographic status, memory form, agent setting, lifecycle phase, mechanism, attacker access or trust assumptions, activation pattern, evidence artefacts, reported findings, and limitations.

Five forensic capabilities use a three-level code:

- **Yes:** explicit evaluated or formally specified support;
- **Partial:** indirect, incomplete, or supporting evidence without end-to-end coverage;
- **No:** no dedicated support in the study.

The repository contains the primary coding and sensitivity calculations. It does not claim independent inter-rater reliability unless second-coder files are added later.

## Synthesis

Counts are descriptive of the bounded corpus. No pooled effect size or population-prevalence inference is made because the literature mixes attacks, systems, formal methods, benchmarks, and rapidly changing preprints.
