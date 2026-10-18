"""Check the template's links and copied skill files. Requires only Python 3."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import sys
from sync_claude_skills import check_entries


def check(root):
    errors = []
    required = [
        "README.md", "AGENTS.md", "CLAUDE.md", "CONTEXT.md", "LICENSE",
        "docs/quick-start.md",
        "THIRD_PARTY_NOTICES.md", "docs/workflow.md", "docs/app-setup.md",
        "docs/agents/domain.md", "docs/agents/issue-tracker.md",
        "docs/agents/triage-labels.md", "briefs/pilot.md", "templates/review.md",
        "design-system/components.md", "design-system/rules.md",
    ]
    for name in required:
        if not (root / name).is_file():
            errors.append(f"Missing file: {name}")
    errors.extend(check_entries(root))
    claude_guide = root / "CLAUDE.md"
    if claude_guide.is_file() and "@AGENTS.md" not in claude_guide.read_text().splitlines():
        errors.append("CLAUDE.md must import the shared AGENTS.md")
    manifest = json.loads((root / "skills-manifest.json").read_text())
    for name, expected in manifest["files"].items():
        source = root / name
        if not source.is_file():
            errors.append(f"Missing skill file: {name}")
        elif hashlib.sha256(source.read_bytes()).hexdigest() != expected:
            errors.append(f"Changed skill file: {name}")
    skills = sorted((root / ".agents/skills").glob("*/SKILL.md"))
    expected_skills = {Path(name).parts[2] for name in manifest["files"]}
    if {p.parent.name for p in skills} != expected_skills:
        errors.append("Skill list differs from the saved source list")
    for skill in skills:
        if f"name: {skill.parent.name}\n" not in skill.read_text():
            errors.append(f"Skill name does not match its folder: {skill.parent.name}")
        policy = skill.parent / "agents/openai.yaml"
        if not policy.is_file() or "allow_implicit_invocation: false" not in policy.read_text():
            errors.append(f"Skill needs explicit invocation: {skill.parent.name}")
    links = 0
    for source in root.rglob("*.md"):
        if ".git" in source.relative_to(root).parts:
            continue
        text = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", source.read_text(), flags=re.M | re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", text):
            target = target.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path or target.startswith("/"):
                continue
            links += 1
            if not (source.parent / unquote(parsed.path)).exists():
                errors.append(f"Broken link in {source.relative_to(root)}: {target}")
    return errors, len(skills), len(manifest["files"]), links


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    try:
        errors, skills, files, links = check(root)
    except (OSError, ValueError, KeyError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    if errors:
        sys.exit(1)
    print(f"PASS: {skills} skills, {files} source hashes, {links} local links")
