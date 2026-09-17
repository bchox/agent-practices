---
name: debugging
description: Diagnose reproducible software failures, regressions, crashes, or incorrect behavior before proposing a fix.
---

# Debugging

Reproduce the smallest version of the failure and record the actual and expected behavior. Trace evidence through logs, tests, call sites, and recent changes; distinguish the root cause from downstream symptoms.

Change one meaningful variable at a time. Add temporary instrumentation only when existing evidence is insufficient, and remove it before finishing unless it has lasting operational value.

Do not implement a fix when the request is diagnosis-only. When a fix is in scope, add a regression test and verify both the focused scenario and the relevant broader suite.
