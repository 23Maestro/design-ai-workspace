# Task tracker

For a standalone copy with no tracker, use local Markdown. This is the template
default. When adopted into an app with a real tracker, that tracker owns task
state. Change this file to its rules; do not keep a second live backlog here.
For Jerami's current consulting work, Asana owns the actual template task.

## Local file rules

- Spec: `.scratch/<flow>/spec.md`.
- Tickets: `.scratch/<flow>/issues/<NN>-<slug>.md`, 1 file per ticket.
- Each ticket has a status, acceptance checks, and blocking ticket references.
- Comments append under a `## Comments` heading.

When a bundled skill says to publish a spec or ticket, write it at the matching
path after the user approves that step. A ready ticket never starts an agent.
No pilot tickets are created by this blank template.

Before `code-review`, the user names a valid base ref and spec. Its committed
diff requirement remains in force. Initial repo setup does not authorize a
commit. Record a pending review if the base or committed diff is absent.
