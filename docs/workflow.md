# Design workflow

## 1. Connect the real app

An engineer records the app commands, existing React components, and token
sources using [app setup](app-setup.md). Keep the current Figma workflow for
ideas and approved references. A second design app is not required.

## 2. Define 1 flow

Fill in the [pilot brief](../briefs/pilot.md). Use `grill-with-docs` to settle
the goal, states, component choices, and review rules. `domain-modeling` is
available when a term needs a clear shared meaning. Name the observable test
surface and get agreement before writing behavior tests.

## 3. Plan only as much as needed

For 1 small change, move to `implement` once the brief is clear. For work across
several sessions, invoke `to-spec`, then `to-tickets`. Keep blocking links clear.
Use `prototype` only when a runnable trial is needed to answer an open question.
Each named step is a user-invoked skill, not an automatic command chain.

## 4. Build 1 complete slice

Invoke `implement` in the real app repo. Reuse its components and tokens. Apply
the `tdd` red-green method to agreed behavior. Run the existing app checks.
Show the running flow before adding more screens or variants.

## 5. Review the result

Use the [review record](../templates/review.md). Check the rendered screen at
agreed sizes, keyboard use, and component states. The designer judges the look
and interaction. The engineer judges the code and checks. `code-review` keeps
its standards and spec findings separate. It needs a valid, non-empty committed
diff against a named base. Before commits are authorized, review the current
files and diff directly; do not call that the skill's completed review.

Use an existing approved hosted preview path. Publication needs authorization.
For Jerami's projects, Sites owns review previews. A localhost link is not the
review handoff. Stop any test server started for an automated check.

## 6. Accept and learn

Merge or publish only when authorized. Compare the pilot with the old workflow:
record Figma time, time to an accepted change, and engineer rework. Inspect
component reuse. Report the actual observations before claiming a wider result.

## When architecture work fits

`improve-codebase-architecture` is optional. Use it before a pilot only when
existing components are hard to find, test, or change. Otherwise use it later
when repeated changes expose real friction. It proposes candidates; the user
picks one. `codebase-design` can help design the chosen module. A full redesign
is not a prerequisite for trying 1 flow.
