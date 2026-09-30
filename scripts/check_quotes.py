#!/usr/bin/env python3
"""Check that every quote in your ads is word for word from your customers.

Usage:
    python3 scripts/check_quotes.py output/batch-01
    python3 scripts/check_quotes.py customer/voice.md
    python3 scripts/check_quotes.py output/lab/round-1 --min-words 3

It reads the ads (.html) and batch.md in a folder, or any file you name, finds text inside
quotation marks, and looks for it in the files in customer/ (CSV, JSON,
JSONL, TXT, MD; not the voice.md summary Claude writes). A quote with "..."
in it is checked piece by piece. Case, curly vs straight quotes and extra
spaces don't matter. Everything else does, including typos.

Short quoted bits (under --min-words, default 3) are skipped, so a word in
scare quotes doesn't trip it.

Exit code 0 means every quote was found. 1 means at least one wasn't.
"""

import argparse
import csv
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CUSTOMER = ROOT / "customer"
SKIP_SOURCES = {"voice.md", "README.md"}

QUOTE_PATTERNS = [
    re.compile(r"“([^“”]+?)”"),  # curly double quotes
    re.compile(r'"([^"\n]+?)"'),                        # straight double quotes
]


def norm(text):
    text = html.unescape(text)
    text = (text.replace("’", "'").replace("‘", "'")
                .replace("“", '"').replace("”", '"')
                .replace("…", "...").replace(" ", " "))
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def strings_in(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from strings_in(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings_in(v)


def load_corpus():
    parts = []
    if not CUSTOMER.is_dir():
        return ""
    for f in sorted(CUSTOMER.rglob("*")):
        if not f.is_file() or f.name in SKIP_SOURCES:
            continue
        suffix = f.suffix.lower()
        try:
            if suffix == ".csv":
                with open(f, newline="", encoding="utf-8-sig", errors="replace") as fh:
                    for row in csv.reader(fh):
                        parts.extend(row)
            elif suffix == ".json":
                parts.extend(strings_in(json.loads(f.read_text(errors="replace"))))
            elif suffix == ".jsonl":
                for line in f.read_text(errors="replace").splitlines():
                    if line.strip():
                        try:
                            parts.extend(strings_in(json.loads(line)))
                        except json.JSONDecodeError:
                            parts.append(line)
            elif suffix in (".txt", ".md", ".tsv"):
                parts.append(f.read_text(errors="replace"))
        except Exception as e:
            print(f"  note: couldn't read {f.name} ({e})")
    return "\n".join(norm(p) for p in parts)


def visible_text(path):
    raw = path.read_text(errors="replace")
    if path.suffix.lower() in (".html", ".htm"):
        raw = re.sub(r"(?is)<(style|script)[^>]*>.*?</\1>", " ", raw)
        raw = re.sub(r"(?s)<!--.*?-->", " ", raw)
        raw = re.sub(r"(?i)<br\s*/?>", " ", raw)
        raw = re.sub(r"<[^>]+>", " ", raw)
    else:
        raw = re.sub(r"(?s)<!--.*?-->", " ", raw)
    return html.unescape(raw)


def quotes_in(text, min_words):
    found = []
    for pat in QUOTE_PATTERNS:
        for m in pat.finditer(text):
            q = m.group(1).strip()
            if len(q.split()) >= min_words:
                found.append(q)
    return found


def main():
    parser = argparse.ArgumentParser(description="Check quotes are verbatim.")
    parser.add_argument("paths", nargs="+", help="Files or folders to check")
    parser.add_argument("--min-words", type=int, default=3)
    args = parser.parse_args()

    corpus = load_corpus()
    if not corpus:
        sys.exit("No customer files found in customer/. Add reviews first.")

    targets = []
    for p in args.paths:
        p = Path(p)
        if p.is_dir():
            # In a folder: the ads themselves and batch.md. Plans and score notes
            # hold your own words in quotes, so they're only checked if named.
            targets += sorted(x for x in p.glob("*")
                              if x.suffix.lower() in (".html", ".htm") or x.name == "batch.md")
        elif p.is_file():
            targets.append(p)
        else:
            print(f"  note: can't find {p}")

    checked, problems = 0, []
    for t in targets:
        for q in quotes_in(visible_text(t), args.min_words):
            checked += 1
            pieces = [x for x in re.split(r"\.\.\.|…", q) if len(x.strip().split()) >= 2]
            pieces = pieces or [q]
            for piece in pieces:
                n = norm(piece).strip(" .,;:!?-")
                if n and n not in corpus:
                    problems.append((t, q))
                    break

    for t, q in problems:
        print(f'NOT FOUND  {t}:  "{q}"')
    print(f"{checked} quote(s) checked, {len(problems)} not found word for word in customer/.")
    ad_files = [t for t in targets if t.suffix.lower() in (".html", ".htm")]
    if ad_files and checked == 0:
        print("WARNING: no quoted text found in the ads. Customer words must sit inside quotation "
              "marks (curly or straight) so they can be checked. Unquoted lines are headlines you "
              "wrote: name their source in batch.md.")
        sys.exit(1)
    if problems:
        print("Fix each one: use the exact words from the review, or take the quote marks off "
              "a line that is a headline you tightened (and name its source in batch.md).")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
