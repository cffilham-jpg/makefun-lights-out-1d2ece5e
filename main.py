"""Write the competition entry as exact UTF-8 bytes without a newline.

Honor MAKEFUN_OUTPUT_DIR, default to out/, and fall back to a fresh temporary
directory when the requested destination cannot be written. Print the final
path so callers can locate the entry even when the fallback is needed.
"""

import os
from pathlib import Path
import tempfile


ENTRY = "my last reply is still sending"


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("Entry must be one line of 1-200 characters")
    payload = ENTRY.encode("utf-8")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / "entry.txt"
        output_file.write_bytes(payload)
    except OSError:
        output_dir = Path(tempfile.mkdtemp(prefix="makefun-lights-out-"))
        output_file = output_dir / "entry.txt"
        output_file.write_bytes(payload)
    print(output_file.resolve())


if __name__ == "__main__":
    main()
