# Focused Search Families

Each family combines an agent block, a memory block, and a third concept block.

## Agent block

```text
("LLM agent*" OR "large language model agent*" OR "language model agent*")
```

## Memory block

```text
("persistent memory" OR "long-term memory" OR "agent memory")
```

## Third concept blocks

1. **Poisoning and injection**  
   `"memory poisoning" OR "memory injection" OR backdoor OR sleeper OR "stored prompt injection"`

2. **Privacy and extraction**  
   `"memory extraction" OR leakage OR exfiltration OR "membership inference" OR "cross-user"`

3. **Provenance and lineage**  
   `provenance OR lineage OR traceability OR "tamper-evident" OR "audit log"`

4. **Forensics and attribution**  
   `forensic* OR traceback OR attribution OR "incident reconstruction" OR "causal reconstruction" OR "root cause"`

5. **Recovery and forgetting**  
   `rollback OR recovery OR remediation OR revocation OR "verified forgetting" OR unlearning OR "post-recovery"`

6. **Propagation and scope**  
   `propagation OR contamination OR contagion OR "cross-agent" OR "dependency graph" OR "blast radius"`

## Robustness query for terminology outside the mandatory memory block

```text
("LLM agent" OR "language model agent")
AND
(experience OR reflection OR profile OR skill OR
 "workflow state" OR "agent state" OR "knowledge base")
AND
(poison* OR attack* OR provenance OR forensic* OR
 rollback OR recovery OR contamination)
```

The exact per-database syntax and execution dates should be recorded in `search_log.csv` before the repository is described as fully reproducible.
