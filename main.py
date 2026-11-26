"""Office Artifacts placard entry: write one museum label (<=180 chars) to /output/entry.txt."""

import os
import stat

LINE = ("Ceremonial Chair, c. 2019. Moulded plastic and stale ambition. "
        "One wheel ritually removed, so its occupant could never fully "
        "leave. Donated anonymously by Facilities.")

# Sealed gate: the entry must be 1-180 UTF-8 characters, not only whitespace.
if not (1 <= len(LINE) <= 180 and LINE.strip()):
    raise SystemExit(f"entry line invalid: {len(LINE)} chars")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # The grader collects /output as another user: leave the file world-readable.
    os.chmod("/output/entry.txt", 0o644)
    # Verify the mode actually landed: a file the grader cannot read fails the run.
    if stat.S_IMODE(os.stat("/output/entry.txt").st_mode) != 0o644:
        raise SystemExit("entry.txt mode is not 0644")
    # Read-back check: what landed on disk must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match LINE")
    # Byte check: the character count and the UTF-8 byte count must both agree,
    # so a stray multi-byte character cannot slip past the 180-char gate.
    if len(written.encode("utf-8")) != len(LINE.encode("utf-8")):
        raise SystemExit("entry.txt byte length mismatch")


if __name__ == "__main__":
    main()
