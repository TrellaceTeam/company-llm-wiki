# Ingest

Fold one source into the wiki. Run, backfill and fix send each source here, one at a time. Take it through steps 1 to 5, or step 6 for a deleted one, then record it in step 7, before you open the next source.

## 1. Read the source

Read all of it, comments too when the tool shows them. For a changed source, find the pages built from its earlier version, from its ledger row and a search of the wiki for its title, and read them. Read `company/structure.md`, `company/style.md` and `company/glossary.md`.

**Done when** you can list what the source says that a teammate would want later: facts, numbers, decisions and their reasons, commitments and their owners, risks, open questions, and who is who. Small talk, scheduling chatter, boilerplate and personal life stay off the list. A change that affects the work, such as someone leaving or taking time off, stays on it.

## 2. Triage

Find where the wiki already covers each item. Read the wiki's index and the folder indexes, and search the wiki for names, other words for the same thing, and numbers.

Transcripts need extra care. They mishear names, so check each person, company and product against the glossary, the meeting's attendee list and the wiki, and write the right name. Speaker labels can merge two people or swap between them, so check a label against what the words show, such as a speaker naming their own company. Credit a proposal, decision or task only to the person the words show, and keep who proposed, who decided and who was asked to act apart. An AI-written summary is a lead, and where it and the transcript disagree, the transcript wins.

Give each item one label:

- **New.** No page holds it.
- **Update.** A page holds it, and this source adds to it or changes it. When the claim on the page comes from a newer source, the page keeps the newer fact and gains the older detail as history.
- **Disputed.** A page says something this source contradicts, and this source doesn't supersede it.
- **Nothing new.** The wiki already says it, or it wouldn't help a future reader.

**Done when** every item has a label, and each New, Update or Disputed item has the page it goes on, existing or new. When every item is Nothing new, the source adds nothing, so go to step 7. A thin source earns no page.

## 3. Write

Edit existing pages in place, and create a page only when no page covers the subject, where the placement rules in `SKILL.md` put it. Put each Disputed item under "Open questions" on its page, with both claims credited, dated and cited. For a changed source, update the claims its new version changes, and remove the claims it dropped unless another source still supports them. Update the status line of every page you change.

**Done when** every New, Update and Disputed item sits on a page with its citation, and the source has an entry in that page's Sources list.

## 4. Link

Link each page you touched to its related pages, and add the link back on each of them. This is the step most often skipped. A page that gains only a link is still a page you changed, so update its status line too.

**Done when** every page you touched links to and from its related pages.

## 5. Check

Reread each claim you added beside the source, one by one:

- It says what the source says, with the source's scope, force and certainty. A hedge appears only where the source hedges, and the source's "only" or "highest" stays.
- Its number in square brackets matches the right entry in the page's Sources list, and that entry links to this source.
- Each person is named, with a pronoun only where the source uses one for them.

Then check each page you touched has every part of the page format, in order, and that each new page has its line in its folder index.

**Done when** every claim you added passes all three checks, and every page you touched passes the format check.

## 6. A deleted source

The file is gone, or it left the source folders, so claims that rest on it alone lose their support. Find the pages that cite it from its ledger row and a search. On each one, keep the claims another source supports, remove the rest, and remove its Sources entry. Then check as in step 5, and set its ledger Status to deleted.

**Done when** no page cites the file.

## 7. Record it

Update the source's ledger row: Last changed, Read on, the pages you created and changed, and its Status. Then add its line to the run's log entry: the pages you created and changed, and every Disputed item with the page that records it.

**Done when** the ledger row and the log line are written. Only then open the next source.
