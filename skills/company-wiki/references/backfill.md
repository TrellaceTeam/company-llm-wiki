# Backfill

Fill the wiki from what the company already has: the files in the source folders that last changed before setup. It starts with a pilot, so the person sees real pages and shapes them before most of the history goes in. Then the person picks a pace.

## 1. Size it

List every file in the source folders, then apply the skip rules and the sharing check. Count what's left by folder, with the oldest and newest dates. The cutoff is the day setup ran. Files that change after it come in through runs.

Tell the person in two lines, such as "Your sources hold 1,240 files from April 2021 to today. 930 pass the skip rules." Then give a rough time: in our own runs a source took one to two minutes, plus a review every ten sources. So 930 files is about 15 to 30 hours of work, spread over as many runs as the pace allows.

**Done when** the person knows the count, the date range and the rough time.

## 2. Run the pilot

Ask: "How many files should the pilot read?" Options: "10 (recommended)", "20", "5".

Pick them from the last three months, so the person knows the facts and can judge the pages. Spread them across folders and kinds: at least one long transcript or call note, one decision or plan, one about a customer and one about the team. Ingest each through [ingest.md](ingest.md), oldest first, then review them through [review.md](review.md). The pilot's changes reach the wiki the way the setup's Approval line says.

Then show the person:

- The pages created and changed, each with its link.
- Three claims from different pages, each with its source's link: "Open these three and check them against their sources."
- Any open questions the sources raised.
- What was skipped, and why.
- How the folder plan held up, and any folder you'd add.

Ask for feedback, one question at a time:

1. "How's the level of detail?" Options: "About right", "Too much, keep pages shorter", "Too little, keep more detail".
2. "Is there anything here that shouldn't be in the wiki?" Options: "No", "Yes, I'll say what".
3. "Are the names and folders right?" Options: "Yes", "I'll fix some".
4. "Anything else you'd change about how pages read?"

Save each answer that should hold as a dated rule: style in `company/style.md`, folders in `company/structure.md`, names in `company/glossary.md`. Then ask: "Should I apply these rules to the pilot pages now?" Options: "Yes", "No, they're fine".

**Done when** the feedback is saved and the pilot pages follow it.

## 3. Pick a pace

Ask: "How should I fill in the other {n} files?" Options, each with its trade-off:

1. "A little each run (recommended)." Each run adds up to 15 of the oldest files, beside anything new. That's about {n / 15} runs. It's steady and easy on the plan's usage limits.
2. "All at once, now." In this chat, in batches of ten, with helpers reading side by side where this app has them. It's the fastest, about {hours} hours, and it uses a lot of the plan's usage at once. This chat has to stay open. It works best in a coding agent.
3. "Its own schedule until it's done." A separate scheduled task, every few hours or every night, that does as much as a run allows. It's faster than option 1, and it doesn't tie up this chat.

Save the choice on the Backfill line of `company/setup.md`. For option 3, setup schedules the task at its step 7.

Then queue the history. Add a backfill row to the ledger for every file that passed step 1 and isn't read yet, with its Last changed time. Adding the rows once means no run has to list every file again, and the ledger shows exactly how far the backfill has got. When there are too many rows to add in one go, add them a folder at a time, and note in the log which folders are still to add.

**Done when** the pace is saved and the history is queued.

## 4. Run it

Take the backfill rows oldest change first, so newer facts win. A backfill row becomes read, skipped or failed like any other row.

### A little each run

Each run adds up to the setup's number of backfill rows after the due rows, within the Run size, as [run.md](run.md) says.

### All at once

Work in batches of ten. With helpers, dispatch one per file in the batch, all at once, each with the reading brief below, and wait for every one. Then write the batch yourself, one source at a time, oldest first, through [ingest.md](ingest.md) steps 2 to 7. Use each helper's note in place of a first read, and open the source to check every claim before you write it. Review each batch through [review.md](review.md). Without helpers, ingest each file through [ingest.md](ingest.md) in turn.

Helpers read side by side but never write, since two writers at once overwrite each other's edits on shared pages, such as a person's page or the pricing page. In our own tests, two writers side by side saved no time and caused many retries.

The reading brief:

```text
Read {source title} in full: {link}. Write nothing in the wiki. Return a note in this shape.
Source: its title, link, date, and author when it states one.
Items: one line each. The claim, with the source's own scope, force and certainty. The names it uses. The page it belongs on: an existing page from the wiki's index, or a new page and its folder.
Questions: names you couldn't confirm, and speaker labels that look wrong.
```

### Its own schedule

Each backfill run takes the lock and checks the tools as [run.md](run.md#steps) says, then works through batches as in "All at once" until it reaches the Run size or the session is nearly full, then logs what's left.

**Done when** the ledger has no backfill rows and no folders still to add.

## 5. Finish

Log "Backfill done on {date}" and tell the admin. With its own schedule, give them the steps from [schedules.md](schedules.md) to turn that task off. Suggest a tidy now, since a backfill makes many pages at once. Save "Backfill: done {date}" in `company/setup.md`.
