# Checkpoint 5: Lab project

**The idea.** Show the brain what good looks like, as specific to your brand as possible. Talk about why it's good. Then give it a small test and grade it, as many rounds as it takes. Every grade becomes a rule, until it reliably makes a good ad. This also exposes what the brain still doesn't know: can it write a good headline, does it really know your offer, your customer?

---

## Part 1: Photos (into `photos/`)

- Ask for their real product and lifestyle photos, ideally the ones already on their site and in their ads. Drag them into `photos/`. Google Drive: right-click the folder, Download, unzip into `photos/`.
- **Website only:** pull product and lifestyle images from their product pages yourself (ask first). Skip images with text or badges baked in.
- **Any photo with text baked in** (theirs or pulled): crop the text out completely or don't use it, and check the text against off-limits: it's a claim.
- **Customer photos** (from reviews, DMs, tags): only with that customer's own words, and put "permission to use in ads?" on the facts to confirm until the founder says yes.
- **Cut-outs:** preview on the planned background; if a baked shadow shows as a glow, use a light background.
- **They already have a photo list:** reuse it; add your notes in `photos/photos-notes.md`.
- Minimum 3. 20 to 50 is great. **Look at them**, don't guess from file names: make a contact sheet (an HTML grid of thumbnails, rendered with `scripts/render.py`) and view it. Read each photo's shape from how it displays, not from file metadata (phone photos are often rotated).
- **Draft `photos/photos.md`:** one line per photo: file, what's in it, shape, best use (product hero, detail, in use, lifestyle, problem shot, before/after), where a crop works, and anything that makes it unsafe (a before/after that isn't a true pair, someone's face).
- **Hand back:** "Your strongest 5 for ads are ___. You're light on ___ (for example, the product in use)."

## Part 2: What good looks like (into `references/`)

1. **Their own best ads first.** If they have results, pull their top ads (from checkpoint 2). If not, look up their live ads in the Meta Ad Library yourself.
2. **Then brands they admire,** in the same category and price range. Ask: "Which brands' ads do you wish were yours?" Find those brands' live ads in the Meta Ad Library (same method as syllabus day part 1; check the advertiser name on every result). You open the search; they only screenshot (if you can't read it) and react. If they already use Foreplay or a swipe file, they can drop screenshots in `references/`.
3. **Sort them** into the format folders in `references/`. Not sure? Leave them in `references/` and sort later.
4. Say so out loud if a reference uses AI-generated scenes: fine to borrow its layout, not its imagery.

**The conversation (this is the checkpoint, don't skip it).** Pick their 3 favorites and ask about each, one at a time (one question each is enough if their answers are short):
- "What do you like about this one?"
- "Why do you think it works? What is it arguing?"
- "What do you see first, second and third?" (That's the visual hierarchy.)

Then add what you see: the format, the layout skeleton (photo where, headline where, how many words), and **what the format itself argues** (a Q&A says "you're wondering this"; a before/after says "look at the difference"; a phone-caption post says "a real person, not an ad").

- **Draft `references/layouts.md`:** each reference, its format, its skeleton, what it argues, and the founder's words about it.
- **Branded or native.** Point out that some ads are meant to look like the brand (logo, brand fonts, brand colors) and some are meant to look like a post (no logo, the platform's own type, a phone photo). Both are real choices. Ask which they like, and note it.

## Part 3: The small test, graded

1. Make **3 quick ads**, each on a different layout from `layouts.md`, from real photos and verbatim customer words (follow `templates/branded.html` and `templates/native.html`). Save them in `output/lab/round-1/`. Paths from `output/lab/round-N/` start with `../../../`. Render, **look at every PNG yourself** (same checks as `road/7-build.md` step 6, including: does a quote sit over a photo in a way that implies it's the customer's own?), fix what's off, run `python3 scripts/check_quotes.py output/lab/round-1`.
2. **The founder grades each one A to F**, with a few words why. Give them what to look at: the headline, the photo, is the offer clear, does it sound like your customer, does it look like you.
3. **Turn every "why" into a rule**, one plain line with where it came from:
   - Something they never want again: `brain/off-limits.md`.
   - How they like ads made (fonts, photos, claims, tone, layout): "Your rules" in `brain/house-rules.md`.
   - What earned an A or B: `brain/what-worked.md`.
4. Show them the new lines: "Here's what I added. You won't have to tell me again."
5. **Round 2:** remake the weakest with the new rules. Grade again. As many rounds as it takes, but two or three is usual. Stop when they give at least one A or B and say "that looks like us".

Save each round's grades to `output/lab/grades.md`.

- **Hand back:** the before and after of their lowest-graded ad, and the list of rules it earned.

**Done when:** `photos/photos.md` and `references/layouts.md` exist, and `output/lab/grades.md` has at least one graded round.
