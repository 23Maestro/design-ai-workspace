---
name: handoff
description: "Compact the current conversation into a handoff document for another agent to pick up. Use only when the user explicitly names this skill."
---

## Invocation contract

Use this skill only when the user explicitly names it. Keep all analysis and execution in the current session. Recommend related skills or a separate task when useful, and leave every launch to the user. Leave agent hooks and model settings unchanged. Stage, commit, push, branch, and worktree actions require a separate explicit request from the user.

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace.
Include a "suggested skills" section in the document, which suggests skills that the agent should invoke.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
