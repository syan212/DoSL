import argparse
import sys
from .repl import start_repl, run_file
from .colour import red
def main():
    parser_arg = argparse.ArgumentParser(description="DoSL interpreter")
    parser_arg.add_argument('file', nargs='?', help='DoSL script file to execute (optional)')

    args = parser_arg.parse_args()
    if args.file:
        filename = args.file
        if not filename.lower().endswith(".dosl"):
            print(red("Invalid file extension: expected '.dosl'"))
            sys.exit(1)
        run_file(args.file)
    else:
        start_repl()
