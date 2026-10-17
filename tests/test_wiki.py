"""Tests for skills/company-wiki/scripts/wiki.py, the skill's rules and the example setup.

Run from the repo root: python -m unittest discover -s tests -v
"""

from __future__ import annotations

import importlib.util
import re
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "company-wiki"
EXAMPLE = ROOT / "examples" / "fennick" / "company"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


wiki = load("wiki", SKILL / "scripts" / "wiki.py")
check_skill = load("check_skill", ROOT / "scripts" / "check_skill.py")

READER_VALUES = {
    "name": "Fennick wiki",
    "company_name": "Fennick Software",
    "index": "https://docs.google.com/document/d/EXAMPLE-INDEX/edit",
    "report": "doc",
    "corrections": "https://docs.google.com/document/d/EXAMPLE-CORRECTIONS/edit",
    "admin": "Priya Raman",
    "home": "Google Drive",
}


class PackTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.skill = self.tmp / "company-wiki"
        shutil.copytree(SKILL, self.skill, ignore=shutil.ignore_patterns("__pycache__", "company"))

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_pack_ships_the_skill_and_the_company_files(self):
        (self.skill / ".env").write_text("KEY=secret", encoding="utf-8")
        (self.skill / "references" / "export.csv").write_text("a,b", encoding="utf-8")
        company = self.tmp / "company"
        company.mkdir()
        (company / "setup.md").write_text("# Company wiki setup\n", encoding="utf-8")
        (company / "notes.txt").write_text("private", encoding="utf-8")
        out = self.tmp / "out" / "company-wiki.skill"
        entries, added, left_out = wiki.pack_skill(self.skill, company, out)
        with zipfile.ZipFile(out) as archive:
            names = archive.namelist()
        self.assertEqual(names, entries)
        self.assertTrue(all(name.startswith("company-wiki/") for name in names))
        for expected in ("company-wiki/SKILL.md", "company-wiki/references/setup.md", "company-wiki/assets/reader.md",
                         "company-wiki/scripts/wiki.py", "company-wiki/company/setup.md"):
            self.assertIn(expected, names)
        self.assertEqual(added, ["setup.md"])
        self.assertIn(".env", left_out)
        self.assertIn("references/export.csv", left_out)
        self.assertIn("company/notes.txt", left_out)
        self.assertFalse(any(name.endswith((".env", ".csv", ".txt")) for name in names))

    def test_company_folder_overrides_the_skills_own_copy(self):
        (self.skill / "company").mkdir()
        (self.skill / "company" / "setup.md").write_text("old", encoding="utf-8")
        (self.skill / "company" / "glossary.md").write_text("kept", encoding="utf-8")
        company = self.tmp / "new"
        company.mkdir()
        (company / "setup.md").write_text("new", encoding="utf-8")
        out = self.tmp / "company-wiki.zip"
        _, added, _ = wiki.pack_skill(self.skill, company, out)
        with zipfile.ZipFile(out) as archive:
            self.assertEqual(archive.read("company-wiki/company/setup.md").decode(), "new")
            self.assertEqual(archive.read("company-wiki/company/glossary.md").decode(), "kept")
        self.assertEqual(added, ["glossary.md", "setup.md"])

    def test_pack_refuses_a_missing_company_folder(self):
        out = self.tmp / "company-wiki.skill"
        code = wiki.main(["pack", "--out", str(out), "--company", str(self.tmp / "missing")])
        self.assertEqual(code, 1)


class ReaderTests(unittest.TestCase):
    def setUp(self):
        self.template = (SKILL / "assets" / "reader.md").read_text(encoding="utf-8")

    def test_fills_every_placeholder(self):
        text = wiki.fill_reader(self.template, dict(READER_VALUES))
        self.assertNotRegex(text, r"\{\{")
        self.assertIn("name: company-wiki-reader", text)
        self.assertIn("# Fennick wiki", text)
        self.assertIn(READER_VALUES["index"], text)
        self.assertIn(READER_VALUES["corrections"], text)
        self.assertIn("in Google Drive", text)

    def test_each_report_mode(self):
        for report, expected in (("comment", "Wiki correction:"), ("admin", "send to Priya Raman")):
            values = dict(READER_VALUES, report=report, corrections=None)
            self.assertIn(expected, wiki.fill_reader(self.template, values))

    def test_doc_reports_need_the_corrections_link(self):
        with self.assertRaises(ValueError):
            wiki.fill_reader(self.template, dict(READER_VALUES, corrections=""))

    def test_a_quote_in_the_company_name_keeps_the_yaml_valid(self):
        text = wiki.fill_reader(self.template, dict(READER_VALUES, company_name='Fennick "FSW" Software'))
        description = re.search(r'^description: "(.*)"$', text, re.MULTILINE).group(1)
        self.assertNotIn('"', description)

    def test_a_long_company_name_is_refused(self):
        with self.assertRaises(ValueError):
            wiki.fill_reader(self.template, dict(READER_VALUES, company_name="Fennick " * 30))

    def test_the_built_reader_passes_the_skill_rules(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            out = tmp / "company-wiki-reader.skill"
            args = ["reader", "--out", str(out)]
            for key, value in READER_VALUES.items():
                args += [f"--{key.replace('_', '-')}", value]
            self.assertEqual(wiki.main(args), 0)
            with zipfile.ZipFile(out) as archive:
                self.assertEqual(archive.namelist(), ["company-wiki-reader/SKILL.md"])
                archive.extractall(tmp)
            self.assertEqual(check_skill.check_skill(tmp / "company-wiki-reader"), [])
        finally:
            shutil.rmtree(tmp)


class SkillTests(unittest.TestCase):
    def test_the_skill_passes_the_skill_rules(self):
        self.assertEqual(check_skill.check_skill(SKILL), [])

    def test_every_mode_file_exists(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        for target in re.findall(r"\]\((references/[a-z-]+\.md)", text):
            self.assertTrue((SKILL / target).is_file(), target)

    def test_the_example_setup_has_every_section_of_the_template(self):
        template = (SKILL / "references" / "company-folder.md").read_text(encoding="utf-8")
        block = template.split("## Setup template", 1)[1].split("```markdown", 1)[1].split("```", 1)[0]
        sections = re.findall(r"^## (.+)$", block, re.MULTILINE)
        example = (EXAMPLE / "setup.md").read_text(encoding="utf-8")
        self.assertEqual(re.findall(r"^## (.+)$", example, re.MULTILINE), sections)

    def test_the_example_company_folder_packs(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            _, added, _ = wiki.pack_skill(SKILL, EXAMPLE, tmp / "company-wiki.skill")
            self.assertEqual(added, ["glossary.md", "home.md", "setup.md", "structure.md", "style.md"])
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
