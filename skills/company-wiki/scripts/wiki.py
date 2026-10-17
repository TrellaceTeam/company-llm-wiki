#!/usr/bin/env python3
"""Pack the company-wiki skill, and build the team's reader skill, as files a chat app installs.

Usage:
    python wiki.py pack --out company-wiki.skill [--company <folder with setup.md>]
    python wiki.py reader --name "Fennick wiki" --company-name "Fennick Software" \\
        --index <link> --report doc --corrections <link> --admin "Priya Raman" \\
        [--home "Google Drive"] --out company-wiki-reader.skill

pack zips this skill with the company's setup files, so the person's own copy starts
with no setup questions. reader fills in the team's skill from assets/reader.md.
Both read and write local files only, with no network, so they run in a chat app's
sandbox and on a laptop alike. Python 3.9 or later, standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "company-wiki"
READER_NAME = "company-wiki-reader"
MAX_DESCRIPTION = 199
PLACEHOLDER = re.compile(r"\{\{[a-z_]+\}\}")
REPORT_STEPS = {
    "doc": (
        "Add the report to the end of the corrections doc, {corrections}, as one line: the date, "
        "the person's name, the page link, what's wrong and how they know. When you can't edit the "
        "doc, give the person that line to paste there."
    ),
    "comment": (
        'Add the report as a comment on the page, starting with "Wiki correction:". When you can\'t '
        "comment, give the person the text to add as a comment themselves."
    ),
    "admin": "Give the person the report as text to send to {admin}.",
}


def _ships(rel: Path) -> bool:
    """Only the skill's own files ship. Anything else beside them, such as an export, a key file
    or a run's notes, may hold private data."""
    parts = rel.parts
    if parts == ("SKILL.md",):
        return True
    if len(parts) == 2 and parts[0] in ("references", "assets"):
        return rel.suffix == ".md"
    if len(parts) == 2 and parts[0] == "scripts":
        return rel.suffix == ".py"
    return False


def pack_skill(root: Path, company: Path, out: Path):
    """Zip the skill at root into out, with a company/ folder made of the skill's own company/*.md
    files overlaid by the Markdown files in company. Return (entries, company files, left out)."""
    root, out = root.resolve(), out.resolve()
    entries, left_out = [], []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if not path.is_file() or path.resolve() == out or rel.parts[0] == "company" or "__pycache__" in rel.parts:
            continue
        if _ships(rel):
            entries.append((f"{SKILL_NAME}/{rel.as_posix()}", path))
        else:
            left_out.append(rel.as_posix())
    files = {}
    for folder in (root / "company", company):
        if folder.is_dir():
            for path in sorted(folder.iterdir()):
                if path.is_file() and path.suffix.lower() == ".md":
                    files[path.name] = path
                elif not path.name.startswith("."):
                    left_out.append(f"{folder.name}/{path.name}")
    entries += [(f"{SKILL_NAME}/company/{name}", path) for name, path in sorted(files.items())]
    out.parent.mkdir(parents=True, exist_ok=True)
    # Some app sandboxes date files 1970, which a zip can't hold unless strict timestamps are off.
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, strict_timestamps=False) as archive:
        for arcname, path in entries:
            archive.write(path, arcname)
    return [arcname for arcname, _ in entries], sorted(files), sorted(set(left_out))


def pack(args) -> int:
    company = Path(args.company) if args.company else ROOT / "company"
    if args.company and not company.is_dir():
        print(f"No folder at {company}. Point --company at the folder that holds setup.md.", file=sys.stderr)
        return 1
    entries, added, left_out = pack_skill(ROOT, company, Path(args.out))
    print(f"wrote {args.out}: {len(entries)} files, with company files: {', '.join(added) or 'none'}")
    if left_out:
        shown = ", ".join(left_out[:8]) + (f" and {len(left_out) - 8} more" if len(left_out) > 8 else "")
        print(f"  left out {shown}. Only the skill's own files and the company's .md files go in.")
    if "setup.md" not in added:
        print("  check: no company/setup.md went in, so this copy will start with setup.")
    return 0


def _one_line(value: str) -> str:
    return " ".join(value.split())


def fill_reader(template: str, values: dict) -> str:
    """Fill the reader template. Raise ValueError when a value is missing or the result breaks a rule."""
    report = values["report"]
    if report not in REPORT_STEPS:
        raise ValueError(f"--report must be one of {', '.join(REPORT_STEPS)}")
    if report == "doc" and not values.get("corrections"):
        raise ValueError("--report doc needs --corrections, the corrections doc's link")
    filled = {key: _one_line(value or "") for key, value in values.items()}
    for key in ("name", "company_name", "index", "admin", "home"):
        if not filled.get(key):
            raise ValueError(f"--{key.replace('_', '-')} is empty")
    filled["report_steps"] = REPORT_STEPS[report].format(corrections=filled.get("corrections", ""), admin=filled["admin"])
    text = template
    # The company name sits inside a double-quoted YAML value, so a double quote there would end it.
    text = text.replace('"Answer questions about {{company}}', '"Answer questions about ' + filled["company_name"].replace('"', "'"))
    for key, value in (("company", filled["company_name"]), ("name", filled["name"]), ("home", filled["home"]),
                       ("index", filled["index"]), ("admin", filled["admin"]), ("report_steps", filled["report_steps"])):
        text = text.replace("{{" + key + "}}", value)
    left = PLACEHOLDER.findall(text)
    if left:
        raise ValueError(f"the template still has {', '.join(sorted(set(left)))}")
    match = re.search(r'^description: "(.*)"$', text, re.MULTILINE)
    if not match or len(match.group(1)) > MAX_DESCRIPTION:
        raise ValueError("the description is over 199 characters. Use a shorter --company-name")
    return text


def reader(args) -> int:
    template = (ROOT / "assets" / "reader.md").read_text(encoding="utf-8")
    values = {"name": args.name, "company_name": args.company_name, "index": args.index, "report": args.report,
              "corrections": args.corrections, "admin": args.admin, "home": args.home}
    try:
        text = fill_reader(template, values)
    except ValueError as error:
        print(f"reader: {error}", file=sys.stderr)
        return 1
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(f"{READER_NAME}/SKILL.md", text)
    print(f"wrote {args.out}: {READER_NAME}/SKILL.md for {values['company_name']}")
    print(f"  index: {_one_line(args.index)}")
    print(f"  reports: {args.report}" + (f", to {_one_line(args.corrections)}" if args.report == "doc" else ""))
    return 0


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("pack", help="zip this skill with the company's setup files, for a chat app to install")
    p.add_argument("--out", required=True, help="the file to write, such as company-wiki.skill or company-wiki.zip")
    p.add_argument("--company", help="the folder with setup.md. Default: company/ in this skill's folder")

    r = sub.add_parser("reader", help="build the team's company-wiki-reader skill")
    r.add_argument("--name", required=True, help="the wiki's name, such as Fennick wiki")
    r.add_argument("--company-name", required=True, help="the company's name")
    r.add_argument("--index", required=True, help="the link to the wiki's index")
    r.add_argument("--report", required=True, choices=sorted(REPORT_STEPS), help="where people report a wrong page")
    r.add_argument("--corrections", help="the corrections doc's link, for --report doc")
    r.add_argument("--admin", required=True, help="the admin's name")
    r.add_argument("--home", default="Google Drive", help="the tool the wiki lives in. Default: Google Drive")
    r.add_argument("--out", required=True, help="the file to write, such as company-wiki-reader.skill")

    args = parser.parse_args(argv)
    return {"pack": pack, "reader": reader}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
