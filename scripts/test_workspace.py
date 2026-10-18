"""Regression checks for a fresh copy of the harness, through its file checker."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


class WorkspaceTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="design-workspace-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        source = Path(__file__).resolve().parents[1]
        shutil.copytree(source, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def run_check(self):
        return subprocess.run(
            [sys.executable, "scripts/check_workspace.py"],
            cwd=self.root, text=True, capture_output=True, check=False,
        )

    def test_complete_copy_passes(self):
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_claude_entry_is_reported(self):
        (self.root / ".claude/skills/ask-matt/SKILL.md").unlink()
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Claude entry missing or out of date", result.stderr)

    def test_automatic_claude_invocation_is_reported(self):
        entry = self.root / ".claude/skills/implement/SKILL.md"
        entry.write_text(entry.read_text().replace(
            "disable-model-invocation: true", "disable-model-invocation: false"
        ))
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Claude entry missing or out of date", result.stderr)

    def test_missing_shared_rule_import_is_reported(self):
        (self.root / "CLAUDE.md").write_text("# Claude Code\n")
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("CLAUDE.md must import the shared AGENTS.md", result.stderr)


if __name__ == "__main__":
    unittest.main()
