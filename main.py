"""Rate My Human: The One-Line Review — entry generator.

Contract (from the bounty kit): the program writes one text to
/output/entry.txt — a single line, 1 to 200 UTF-8 characters, not only
whitespace, with no trailing newline. The output directory comes from
MAKEFUN_OUTPUT_DIR (default /output), and the file is left readable by
every user (mode 0644) so the grader can collect it.
"""

import os

# The entry line, exactly as judged: 125 characters, one line, UTF-8.
# It is written byte-for-byte, with no trailing newline appended.
LINE = "★★★★☆ — Drops 39 bounties at 5 a.m., wants miracles by lunch, calls it freedom. One star docked. The other four are hostages."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
