# Tidy

Make the wiki cohere, so finding an answer stays quick as it grows, check that it's healthy, and review the recent changes with fresh eyes. A maintenance run comes here, and so does "tidy the wiki". Use the strongest model the app lets you pick. A scheduled tidy asks no questions, and anything that needs the admin goes under Held in the log. Take the lock and check the tools first, as [run.md](run.md#steps) says.

Start by listing every page in the wiki from the indexes, one item per page, and work through the list in each step. When the wiki has more pages than one session can read, tidy one fixed folder per run, in turn, and note in the log which folder is next. Information in two places is not a duplicate by itself: a customer page may apply a general method page, and each serves a different question. Two pages that answer the same question are a duplicate.

## 1. Check health

- **Missed runs.** Compare the log's entries with the schedules in `company/setup.md`. Report any run that didn't happen.
- **Moved-in files.** List each source folder in full and find files with no ledger row. A file moved into a folder keeps its old Last changed time, so runs miss it. Apply the skip rules and the sharing check, then add a due row for each one left. When the setup says "Backfill: not wanted", count only files changed since setup, since the admin chose to leave the history out.
- **Gone files.** Find ledger rows whose file is gone or left the source folders. Take each through [ingest.md](ingest.md#6-a-deleted-source).
- **Failures.** Report any source that failed three times, and any folder whose sharing got narrower.
- **Held changes.** Remind the admin of any held change older than a week.

**Done when** every gap is fixed, queued or reported.

## 2. Review the recent changes

Take every page created or changed since the last tidy, from the log, and review them through [review.md](review.md). Runs review their own batches, often on a faster model, so this is the stronger model's look at the same work.

**Done when** every page changed since the last tidy passes review.

## 3. Check each page

- **Format.** Every page has its title, question, status line, answer and Sources list. Every number in square brackets has its entry, every entry is cited, and every link opens.
- **Out of date.** For a page whose "Out of date after" date has passed, reread its sources, then update it or set the line to the next known end date.
- **Orphans.** Link each page no other page links to from the pages a reader would come from.
- **Indexes.** Every page has its line in its folder index, and every folder its line in the wiki's index.

**Done when** every page on your list passes.

## 4. Merge duplicates

Read the indexes and look for pages that answer the same question under different names. Merge each pair into the page with the better name, as `company/home.md` says: move every unique fact, with its citation and Sources entry, into the kept page, then point every link at it. Trash the one-line pages left by merges once no page links to them, or leave them for the admin when trashing needs a click.

**Done when** no two pages answer the same question.

## 5. Reconcile contradictions

Where pages disagree, read both sources.

- A newer source supersedes the older: update the older claim, with one dated sentence of history when the change matters.
- Each covers a different case: say so on both pages, with the conditions for each.
- The conflict is real: keep both claims, credited and dated, under "Open questions".

**Done when** every disagreement reads as superseded, two cases, or an open question.

## 6. Tighten the structure

- Give each person, company and product one name across the wiki: the fullest form a source gives.
- Give a subject mentioned on three or more pages its own page when the sources support one.
- Split a page that answers several unrelated questions. Fold a thin page into its neighbour. Fold a page named after one document, such as a single board update, into the pages for the subjects it covers.
- Move a misplaced page to where a reader would look for it. Reshape folders the same way, within the Flexibility line of `company/structure.md`: split a folder that mixes subjects a reader would look for separately, fold a thin one into its neighbour, rename one whose name no longer fits. Never change a fixed folder. Suggest that change to the admin under "Setup suggestions" in the log.

**Done when** every page sits where a reader would look for it.

## 7. Log it

Write the tidy's log entry: one line per change, what you merged, split, moved or fixed, and why. Remove the Running line, then report as the Reports line says.
