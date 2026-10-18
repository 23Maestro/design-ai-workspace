# Bundled skills

These are local copies of adapted Matt Pocock skills. Source file hashes are
in `skills-manifest.json`. Supporting files and invocation settings are kept.
Named skills are launched only when the user asks.
Claude entry files in `.claude/skills/` point to the same shared instructions.
Their frontmatter sets `disable-model-invocation: true`. Codex keeps its
invocation settings in `agents/openai.yaml`. See [the quick start](quick-start.md).

| Skill | Place in the flow |
| --- | --- |
| ask-matt | Pick the next skill. |
| grill-with-docs | Settle the brief while keeping shared terms clear. |
| grill-me | Interview without saving project docs. |
| grilling | Reference method for 1 question at a time. |
| domain-modeling | Resolve a term or a durable domain decision. |
| research | Check a claim against primary sources. |
| to-spec | Turn agreed work into a spec. |
| to-tickets | Split a larger spec into complete slices. |
| implement | Build and check 1 complete slice. |
| tdd | Check agreed behavior through its public interface. |
| code-review | Review standards and spec in separate passes. |
| codebase-design | Design a module when its interface needs thought. |
| improve-codebase-architecture | Find real friction in existing code. Optional. |
| prototype | Answer an open question with a small runnable trial. |
| handoff | Carry context to another directory or session. |
| setup-matt-pocock-skills | Change the tracker or domain-doc setup when asked. |

`ask-matt` also describes skills outside this bundle. A reference in that map
does not mean the skill is installed. Check this list before recommending a
launch. No agent hook, model setting, or global skill install is added.
