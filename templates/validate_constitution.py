#!/usr/bin/env python3
"""validate_constitution.py -- gate the constitution itself (doc 16, section 5).

Deterministic, stdlib-only, no model in the loop. Run it in CI and from the
session-start check. Exit codes: 0 ok, 1 failures (printed to stderr), 2 setup error.

Checks:
  1. SIZE   -- the file stays under a token cap (chars/4). Stops silent regrowth.
  2. PATHS  -- every backtick-quoted repo path resolves. A rule that points at a
               renamed hook is a rule with no gate and no warning.
  3. MODES  -- (optional, --require-modes) every bullet under the Non-negotiables
               heading starts with a mode tag: BLOCKING / CONVENTION / STATED GUIDANCE.

Usage:
    python validate_constitution.py [CLAUDE.md] [--repo-root PATH] [--max-tokens N]
                                    [--require-modes] [--ignore TOKEN ...]

Project-specific non-path tokens (a table name, a file on another machine) go in
--ignore, one per token, rather than being hard-coded here.
"""
import argparse
import re
import sys
from pathlib import Path

DEFAULT_MAX_TOKENS = 1500
PATH_TOKEN_RE = re.compile(
    r"`([A-Za-z0-9_\-./]+\.[A-Za-z0-9]{1,8}|[A-Za-z0-9_\-]+(?:/[A-Za-z0-9_\-.]+)+/?)`"
)
SKIP_PREFIXES = ("http://", "https://", "www.", "origin/")
MODE_RE = re.compile(r"^\s*[-*]\s+\*{0,2}(BLOCKING|CONVENTION|STATED GUIDANCE)\*{0,2}\b")
NONNEG_HEADING_RE = re.compile(r"^#{1,6}\s+.*non-negotiables", re.IGNORECASE)


def cited_paths(text, ignore):
    for lineno, line in enumerate(text.splitlines(), start=1):
        for m in PATH_TOKEN_RE.finditer(line):
            tok = m.group(1)
            if tok.startswith(SKIP_PREFIXES) or tok in ignore:
                continue
            if "/" not in tok and re.fullmatch(r"\d+(\.\d+){1,3}[A-Za-z.]*", tok):
                continue  # a version string, not a path
            yield lineno, tok


def unique_basename(root, name):
    """A bare filename re-cited as shorthand counts if exactly one file has it.

    Exclusion is judged on the path RELATIVE to the repo root, so a checkout that
    itself lives under a worktrees directory is not excluded wholesale.
    """
    hits = []
    for p in root.rglob(name):
        rel = p.relative_to(root).parts
        if ".git" in rel or ("worktrees" in rel and ".claude" in rel):
            continue
        hits.append(p)
    return hits


def check_paths(text, root, ignore):
    errs = []
    for lineno, tok in cited_paths(text, ignore):
        clean = re.sub(r":\d+(-\d+)?$", "", tok)
        if (root / clean).exists():
            continue
        if "/" not in clean:
            hits = unique_basename(root, clean)
            if len(hits) == 1:
                continue
            if len(hits) > 1:
                errs.append(f"line {lineno}: `{tok}` is ambiguous ({len(hits)} files share that name)")
                continue
        errs.append(f"line {lineno}: cited path does not resolve: `{tok}`")
    return errs


def check_size(text, cap):
    tokens = len(text) // 4
    return [f"~{tokens} tokens (chars/4) exceeds the cap of {cap}"] if tokens > cap else []


def check_modes(text):
    errs, inside = [], False
    for lineno, line in enumerate(text.splitlines(), start=1):
        if NONNEG_HEADING_RE.match(line):
            inside = True
            continue
        if inside and re.match(r"^#{1,6}\s", line):
            inside = False
        if inside and re.match(r"^\s*[-*]\s+\S", line) and not MODE_RE.match(line):
            errs.append(f"line {lineno}: non-negotiable has no mode tag (BLOCKING / CONVENTION / STATED GUIDANCE)")
    return errs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", default="CLAUDE.md")
    ap.add_argument("--repo-root")
    ap.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    ap.add_argument("--require-modes", action="store_true")
    ap.add_argument("--ignore", nargs="*", default=[])
    a = ap.parse_args()

    f = Path(a.file)
    if not f.exists():
        print(f"ERROR: {f} not found", file=sys.stderr)
        return 2
    root = Path(a.repo_root) if a.repo_root else f.resolve().parent
    text = f.read_text(encoding="utf-8")

    errs = check_size(text, a.max_tokens) + check_paths(text, root, set(a.ignore))
    if a.require_modes:
        errs += check_modes(text)
    if errs:
        print(f"validate_constitution.py: {len(errs)} failure(s) in {f}:", file=sys.stderr)
        for e in errs:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print("validate_constitution.py: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
