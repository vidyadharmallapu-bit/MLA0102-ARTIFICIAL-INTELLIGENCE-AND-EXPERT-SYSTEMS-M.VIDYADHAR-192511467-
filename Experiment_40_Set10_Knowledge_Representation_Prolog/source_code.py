"""Run the knowledge-representation rule chain with SWI-Prolog."""

import shutil
import subprocess
import sys
from pathlib import Path


def main():
    executable = shutil.which("swipl")
    if executable is None:
        print("SWI-Prolog is required. Install it and add 'swipl' to PATH.")
        return 1
    source = Path(__file__).with_name("knowledge_representation.pl")
    return subprocess.run([executable, "-q", "-s", str(source), "-g", "main", "-t", "halt"], check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())