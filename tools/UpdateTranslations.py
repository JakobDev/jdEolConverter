#!/usr/bin/env python
import subprocess
import pathlib
import shutil
import sys


def main():
    if not shutil.which("pylupdate6"):
        print("pylupdate6 was not found", file=sys.stderr)
        sys.exit(1)

    for i in (pathlib.Path(__file__).parent.parent / "jdEolConverter" / "translations").iterdir():
        if i.suffix == ".ts":
            subprocess.run(["pylupdate6", "jdEolConverter", "--ts", str(i), "--no-obsolete"], cwd=pathlib.Path(__file__).parent.parent)


if __name__ == "__main__":
    main()
