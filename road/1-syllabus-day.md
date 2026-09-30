# Checkpoint 1: Syllabus day

**The idea.** You may know everything about your business. The brain knows nothing. Before it can make a good ad, it has to understand your offer: what it is, how it works, why people buy it, who they are, and how you want to come across.

**Four short parts, in this order.** Do one, hand back, move on. The HUD shows the part: "Syllabus day, part 2 of 4: your product."

---

## Part 1: Your brand look (into `brand/`)

Ask for whatever they have: logo files, font files, colors, a brand guide PDF. Drag it all into `brand/`, messy is fine.

- **Website only:** pull it yourself. Fetch the site, read colors and font names from the page and its CSS, save the logo file if you can find it. Then also look at their live ads in the Meta Ad Library, using the method in CLAUDE.md's technical notes (install Playwright now if it isn't there; the renderer needs it anyway). Keep only ads whose advertiser name matches. If it still won't load, open the Ad Library page for them so they can screenshot 2 or 3 ads into `references/`. Ads often look different from the website (heavier type, more color, offers). Tell them what you see and ask which look is really them.
- **They already have a `brand.md` or brand guide:** it's theirs, don't rewrite it. Confirm it, and put anything you add in `brand/brand-notes.md`.
- **Fonts:** if the file isn't here, name the font and where to get it (Google Fonts are free; paid fonts need their own license). Use a close fallback meanwhile, and say so. One `@font-face` per weight file (regular, bold), with `font-weight` set.
- **Draft `brand/brand.md`:** logo file(s), fonts (headline, body, file names), colors with hex codes and what each is for, tone of voice in 3 to 5 words.
- **Hand back:** a one-page brand card. Write `output/brand-card.html` (logo, swatches, fonts set as a sample headline; paths start with `../`), render with `python3 scripts/render.py output/brand-card.html --sizes 1080x1080`, and open the PNG. This also proves the renderer works.

## Part 2: Your product (into `brand/product.md`)

This is the part most AI ad tools skip, and it's why their ads sound generic.

- **Many products?** Ask: "Which one product or line should the brain learn first?" Draft `product.md` for that one. The rest come later.
- **Draft `brand/product.md` yourself** from the website, product pages, packaging copy, FAQs and anything in `brand/`. Cover:
  - What it is, in one plain sentence.
  - **How exactly it works.** The mechanism, the steps, what's in it. Be specific.
  - **Features to benefits.** A two-column list: the feature, and what it does for the customer.
  - **What only you do** (the unique value propositions). Up to 5 candidates.
  - Price, offers, bundles, guarantee, shipping. Only what the site actually says.
  - Values or mission, if they have one.
  - **Facts to confirm:** anything you couldn't verify or that conflicts (the site says one price, the logo says another founding year). Nothing on this list goes in an ad until they answer.
- **The founder's move:** "Here are 5 things I think make you different. Rank them. Which one is really why people buy? Is anything missing?" Write their ranking and their reason into the file, in their words.
- **Why this matters (tell them in one line):** people buy for functional reasons (it works, it's faster, it fits) and emotional ones (how it makes them feel, who it makes them). Most brands lean on one and forget the other. The brain needs both.

## Part 3: Your customers (into `customer/`)

The best headlines are already written by their customers.

- **Where reviews live:** most review apps (Judge.me, Yotpo, Okendo, Loox, Stamped, Shopify) have an Export CSV button. Amazon reviews can be copied. Surveys, support emails and DMs count.
- **Website only:** most review widgets are public. Pull them yourself from the product pages (ask first).
- **Minimum:** about 20 reviews. Hundreds or thousands are fine: read them with a short script, not by pasting them all in.
- **How to read a big pile:** drop obvious spam, group by product, **read every 1 to 3 star review in full** (that's where the objections and the off-limits rules live), then sample the 4 and 5 stars across lengths. Cite every quote by a review id or row number, and keep their typos: word for word means word for word.
- **Draft `customer/voice.md`:**
  - Who buys, in their words, not demographics.
  - Pains: what was wrong before.
  - Outcomes: what changed after.
  - Objections: what almost stopped them.
  - Themes, each tagged **F** (functional) or **E** (emotional), with verbatim quotes and sources.
  - 10 headlines their customers already wrote, each tied to its quote. Only exact words go inside quotation marks; mark a tightened headline "(tightened)" without quote marks.
- **Run** `python3 scripts/check_quotes.py customer/voice.md` and fix anything it flags.
- **The founder's move:** "Which 3 of these headlines sound most like your customer? Which one would you never say?" Mark their picks in `voice.md` by number, and write their reasons in their words in `brain/status.md` (not in `voice.md`, where anything in quotation marks must be a customer's words).

## Part 4: How you want (and don't want) to come across (into `brain/`)

- **Draft `brain/off-limits.md`** from what you already know: the brand guide, the category's usual legal limits (health, earnings, "best", guarantees), and above all **the 1 to 3 star reviews** (a feature people say doesn't work as advertised is a claim we never make). Then ask, one at a time:
  1. "How do you want people to feel about you? And how do you never want to come across?"
  2. "Any claims you can't make, or won't?"
  3. "Anything you've had to tell a designer or agency more than once?"
- Mark every line you drafted (not them) with `(drafted, confirm?)` and read those lines back: "Keep, change or cut?" Only their kept lines lose the mark.
- "Nothing yet" is a fine answer. Flip `Reviewed by you:` to `yes`.
- Walk them through `brain/house-rules.md` quickly: "These are starter rules from people who've made a lot of ads. Cut any that don't fit you." Flip its `Reviewed by you:` to `yes`.
- **Hand back:** re-check the 10 headlines against the rules and say which ones you dropped or changed, and why.

**Done when:** `brand/brand.md`, `brand/product.md` and `customer/voice.md` exist, and `brain/off-limits.md` says `Reviewed by you: yes`. Update `brain/status.md` with their UVP ranking and their "how we come across" answer, in their words.
