"""Run the student database Prolog program with SWI-Prolog."""

import shutil
import subprocess
import sys
from pathlib import Path


def main():
    swipl = shutil.which("swipl")
    if swipl is None:
        print("SWI-Prolog is required. Install it and ensure 'swipl' is on PATH.")
        return 1

    prolog_file = Path(__file__).with_name("student_database.pl")
    result = subprocess.run(
        [swipl, "-q", "-s", str(prolog_file), "-g", "main", "-t", "halt"],
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())