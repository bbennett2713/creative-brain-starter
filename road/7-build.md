# Checkpoint 7: Build the experiment

**The idea.** Every ad is tied to the plan and a reason. Real photos, real customer words, your brand, and only the variable the plan says to change.

---

1. **Read the whole brain first:** everything in `brain/`, `brand/brand.md`, `brand/product.md`, `photos/photos.md`, `customer/voice.md`, `references/layouts.md`, and this batch's `plan.md`.
2. **Propose the ads** in a short table (4 to 6 is usual; the plan says how many). For each:
   - what it tests (the one thing the plan varies, and this ad's version of it)
   - its job: grab attention, explain, or close the sale
   - functional or emotional (what it leads with)
   - **register:** branded (logo, brand fonts and colors) or native (looks like a post: no logo, platform-style type, a phone photo), and why
   - **the format, and what the format argues**
   - the photo (file name)
   - the headline, and the source quote or product fact it came from
   Check the batch against the plan: if two ads differ in more than the thing being tested, fix it. Ask: "Which one would you cut, and why?" (a sharper question than "any changes?")
3. **Make each ad** as an HTML file in `output/batch-NN/` (`ad-01.html` and so on) from `templates/branded.html` or `templates/native.html`: the real photo cropped with `object-fit: cover`, fonts via `@font-face` from `brand/`, sized with `vw`/`vh` so one file fits both shapes. Side-by-side layouts leave empty space at 1080x1350: add a `@media (max-aspect-ratio: 9/10) { ... }` block that stacks the photo above the copy in the tall size. Paths from `output/batch-NN/` start with `../../`.
4. **Render:** `python3 scripts/render.py output/batch-NN/*.html` (square and tall).
5. **Quote check:** `python3 scripts/check_quotes.py output/batch-NN`. Zero problems before they see anything.
6. **Look at every PNG yourself.** Text cut off or overlapping? Product cropped badly? Font loaded? Contrast readable at phone size? Does a before/after read correctly to a stranger (the after visibly better)? Does a quote sit over a photo of a different person or home in a way that implies it's theirs? Fix and re-render.
7. **Save `output/batch-NN/batch.md`:** the table from step 2, so every ad traces back to its sources and to the plan. Only customer words go in quotation marks in `batch.md`; describe what a format argues without quote marks.
8. **Hand back:** open the folder.
9. **Scores:** they score each ad 1 to 5 with a few words why. Save to `output/batch-NN/scores.md`, turn every why into a rule (same as the lab project), and remake anything scored 1 to 3: fix what they flagged, keep what the plan holds constant, and show the remakes before they launch. If the fix needs something the folder doesn't have (a real photo, a fact), say so, add it to "What's thin" in `status.md`, and don't remake it a second time. Show the new rules: "You won't have to tell me again."
10. Tell them: "Launch these together, as one test. When the results come in, drop the export in `results/` and type `start`. That's second semester."

**Done when:** the batch folder has PNGs, `batch.md` and `scores.md`.
