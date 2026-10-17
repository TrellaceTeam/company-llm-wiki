# Contributing

Improvements are welcome, especially from teams who set it up in an app or a home we haven't tried.

## Tell us how setup went

Open an issue with the app and plan you used, where the wiki lives, the step where something went wrong, and what the assistant said. Change every name and link first. A real file, page or link never goes in an issue.

## Share a home that worked

When the wiki works in a tool other than Google Drive, such as Notion or SharePoint, the `company/home.md` setup wrote is the useful part. Open an issue with it, its links replaced, and its self-test results. We'll add what holds for everyone to [homes.md](skills/company-wiki/references/homes.md).

## Keep company folders out

Setup saves a company's folder links and choices in `skills/company-wiki/company/`. Git ignores that folder in this repository, so a test setup never lands in a pull request.

## Keep examples fictional

Examples and tests use the fictional Fennick Software, its customers and its people. Leave out real companies, real files and anything private.

## What the script touches

`wiki.py` reads and writes local files only. It uses no network and needs no key, so it runs in a chat app's sandbox and on a laptop alike.

## Run the checks

Run these from the repo root with Python 3.9 or later, using `python3` or `py` where that's the command. CI runs the same checks on every push and pull request.

```
python scripts/check_skill.py skills/company-wiki
python scripts/lint_prose.py
python scripts/check_links.py
python -m unittest discover -s tests -v
python scripts/build_zip.py
```
