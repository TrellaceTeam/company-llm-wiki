# Run

A scheduled run, or "update the wiki now". It fixes reported pages, queues what changed, reads what's in the queue, reviews the changes and logs what it did. A scheduled run asks no questions. Anything that needs the admin goes under "Held for {admin}" in the log, and into the report when the setup's Reports line says so.

## Steps

1. **Load.** Read every `company/` file, then the top of the log: the Running line, the Held and Setup suggestions sections, and the last few entries. The ledger can grow large, so read the rows you need, such as the due rows or one file's row.
2. **Take the lock.** When the log's top line says "Running since {time}" and that time is less than three hours ago, another run is still writing. Add an entry, "Skipped: {task} was running", and stop. Otherwise write "Running since {now}, {task}" as the log's top line, and remove it when you finish, including when you stop early.
3. **Check the tools.** Make sure you can reach every source and the home. When a tool is missing or a write stops to ask, log "Couldn't run: {what failed}", report it whatever the Reports line says, and stop. When the newest "Setup saved" entry in the log has no run entry after it, this is the first run since setup or a change to it. Run [the run check](homes.md#the-run-check), and read at most two sources this run, so the test is quick.
4. **Fix reported pages.** Take each open report, oldest first, from the corrections doc or the page comments the setup names, through [fix.md](fix.md).
5. **Queue what changed**, as [sources.md](sources.md#queueing-what-changed) says.
6. **Work through the queue.** Take the due rows, then the failed ones, oldest change first. When the backfill pace is "a little each run", add that many of the oldest backfill rows after them. Stop at the setup's Run size. Ingest each through [ingest.md](ingest.md), one at a time. When you can dispatch subagents, give each source a fresh one with `SKILL.md`, [ingest.md](ingest.md), the `company/` files and the source's link, and wait for it before the next. After each source, update its ledger row and add its line to the log.
7. **Review** after every ten sources and after the last one, through [review.md](review.md). When you can dispatch subagents, give the review a fresh one on the strongest model the app lets you pick.
8. **Update the indexes.** Add or update the line for every page you created, moved or renamed, in its folder index. Then update the wiki index's "Last updated" line and its page counts.
9. **Log and report.** Write the run's entry, as `company/home.md` says, with how many rows are still in the queue. Add any lesson for the setup under "Setup suggestions". Remove the Running line, then report as the Reports line says.

When the queue is empty and no report is open, write a one-line entry, "Nothing due", so the admin can see the run happened.

## Approval

The setup's Approval line decides how changes reach the wiki:

- **Live.** Write every change in place.
- **Hold some.** Write every change except the kinds the line names, by default a page about a person at the company, a merge or deletion of a page, and a conflict between sources. For each held change, add an entry under "Held for {admin}" in the log, with the page, the exact text to add, change or remove, the source and why it's held. [status.md](status.md) applies it after the admin says yes.
- **Draft first.** Write each changed page's new version as a copy in the Drafts folder, named "{page title}, draft {date}", and list it under Held. Create a new page in Drafts too. On the admin's yes, [status.md](status.md) copies each draft's text into its page, or moves a new page into place, then removes the draft.

Held changes and drafts are part of the wiki while they wait. Before you create a page, search Held and Drafts for it too. When a page already has a held change or a draft, add the new change to that entry or edit that draft, so applying them never drops one.

The ledger and the log update the same way in every mode, so a held change is never lost and its source is never read twice.

## What needs the admin

With "Only when something needs you", report these and nothing else:

- A held change or draft waiting for a yes.
- A setup suggestion waiting for a yes.
- A run that couldn't start, or a tool that stopped working.
- A source that failed three times.
- A source folder whose sharing got narrower since setup checked it. Skip the folder until the admin says what to do.
- Missed runs, which [tidy.md](tidy.md) finds.

## When a source fails

When you can't finish a source, such as a file that won't open, leave every page in a finished state: complete the claim you were writing, or take it back out. Then log the source as failed with the reason, and set its ledger Status to failed, with the count in Note. The next run tries it again, after the due rows. After three failures, mark it skipped, keep the reason, and report it.

A long file, such as a two-hour transcript, can be too long to read in one go. Read it in parts, keep a running list of what it says, then triage the list as one source.

## Size

Stop when you reach the Run size, or when the app warns that the session is nearly full. The rows you didn't reach stay in the queue, and the next run starts with them. Take every step at the same care for the last source as for the first, and leave more for the next run rather than rushing.
