---
description: Synchronize specification with current implementation
argument-hint: spec-file-path
allowed-tools: Read, Edit, Grep, Glob, Bash(git:*)
---

# Sync Specification with Code

Analyzing alignment between spec and code for **$1**...

## Synchronization Analysis

Running multi-layer analysis:

1. **Requirement Coverage**
   - Mapping acceptance criteria to code
   - Identifying implemented vs. missing

2. **Edge Case Coverage**
   - Checking edge case handling
   - Validating test coverage

3. **Drift Detection**
   - Finding code not in spec
   - Finding spec not in code

4. **Regression Check**
   - Comparing to last sync
   - Identifying removed features

## Generating Sync Report...

[Invokes spec-sync skill]

Report will include:
- Alignment percentage
- Coverage metrics
- Drift items
- Recommendations
- Action items
