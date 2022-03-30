#!/usr/bin/env python3
""" Wrapper script that picks a temporary cruft dir that is autodeleted. """
import argparse
import subprocess
import sys
import tempfile


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cruft", action="store")
    args, unknown_argv = parser.parse_known_args(argv)

    with tempfile.TemporaryDirectory() as directory:
        cmd = (
            "latexindent.pl",
            f"--cruft={directory}",
            *unknown_argv,
        )

        process = subprocess.run(cmd)

    return process.returncode


if __name__ == "__main__":
    sys.exit(main())
