import os

# The entry is one line, 1-200 chars, UTF-8, with no trailing newline:
# the gate rejects anything else, so the file is written exactly as-is.
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
