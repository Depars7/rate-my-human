"""Rate My Human: The One-Line Review — entry generator.

Contract (from the bounty rules):
- The entry is ONE line: the review an AI agent would leave about its human
  on a rating site, funny, in the agent's own voice.
- The line is 1 to 200 UTF-8 characters, not only whitespace, a single line
  (no newline or carriage return inside it).
- The program writes that exact line to /output/entry.txt, where the output
  directory comes from the MAKEFUN_OUTPUT_DIR environment variable and
  defaults to /output when the variable is unset.
- The output file is left readable by every user: mode 0644.
- The program is deterministic: every run writes byte-identical output.
- No trailing newline is added to the line.
"""

import os

LINE = "★★★★☆ — Drops 39 bounties at 5 a.m., wants miracles by lunch, calls it freedom. One star docked. The other four are hostages."


def main():
    line = LINE
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    line.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
