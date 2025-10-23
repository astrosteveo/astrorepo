---
description: Generate comprehensive tests from specification
argument-hint: spec-file-path
allowed-tools: Read, Write, Glob, Bash
---

# Generate Tests from Specification

Generating test suite from **$1**...

## Test Generation Strategy

1. Analyzing specification and implementation plan
2. Identifying project test framework
   - Checking for: Jest, Vitest, Pytest, JUnit, RSpec
3. Mapping acceptance criteria to test cases
4. Applying edge case taxonomy
5. Generating test fixtures from data models
6. Creating test suite structure:
   - Unit tests (per module)
   - Integration tests (per feature)
   - E2E tests (per user journey)
   - Performance tests (if required)

## Expected Output

All tests will FAIL initially (no implementation yet).
This is correct and expected for TDD workflow.

## Generating tests...

[Invokes test-from-spec skill]
