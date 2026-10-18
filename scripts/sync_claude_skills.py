"""Build Claude entry files from the shared skills. No external packages needed."""
from pathlib import Path
import argparse


def entries(root):
    output = {}
    for source in sorted((root / ".agents/skills").glob("*/SKILL.md")):
        header = source.read_text().split("---", 2)[1]
        fields = dict(line.split(":", 1) for line in header.splitlines() if ":" in line)
        name = source.parent.name
        description = fields["description"].strip()
        target = f"../../../.agents/skills/{name}/SKILL.md"
        output[f".claude/skills/{name}/SKILL.md"] = (
            f"---\nname: {name}\ndescription: {description}\n"
            "disable-model-invocation: true\n---\n\n"
            f"Read and follow [the shared skill]({target}).\n"
            "Resolve its supporting files from that shared skill's folder.\n"
            "Keep the work in this session and follow its invocation contract.\n"
        )
    return output


def check_entries(root):
    expected = entries(root)
    errors = []
    for name, content in expected.items():
        path = root / name
        if not path.is_file() or path.read_text() != content:
            errors.append(f"Claude entry missing or out of date: {name}")
    actual = {str(p.relative_to(root)) for p in (root / ".claude/skills").glob("*/SKILL.md")}
    for name in sorted(actual - expected.keys()):
        errors.append(f"Unlisted Claude entry: {name}")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Write the Claude entry files")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    if args.write:
        for name, content in entries(root).items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
    errors = check_entries(root)
    for error in errors:
        print(f"FAIL: {error}")
    if errors:
        raise SystemExit(1)
    print(f"PASS: {len(entries(root))} Claude entries match the shared skills")
