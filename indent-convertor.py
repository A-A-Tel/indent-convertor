#!/usr/bin/env python3
from sys import exit, stderr
from argparse import ArgumentParser
from pathlib import Path
from shutil import copyfile

def convert(lines, to_tabs=True, size=4):
    converted = []
    for line in lines:
        stripped = line.rstrip("\n")

        if not stripped.strip():
            converted.append("\n")
            continue

        if to_tabs:
            spaces = len(stripped) - len(stripped.lstrip(" "))
            tabs = spaces // size
            new_line = "\t" * tabs + stripped[spaces:]
        else:
            tabs = len(stripped) - len(stripped.lstrip("\t"))
            new_line = " " * (size * tabs) + stripped[tabs:]

        converted.append(new_line + "\n")

    return converted


parser = ArgumentParser(description="Converts spaces into tabs, or tabs into spaces! Whitespace-only lines will be cleared entirely.")
parser.add_argument("type", choices=["tab", "space"], help="Type of indentation to convert to")
parser.add_argument("size", type=int, help="The number of spaces per indent")
parser.add_argument("file", type=str, help="The file to be converted")
parser.add_argument("-n", "--no-backup", help="Do not create a backup file", action="store_true")
args = parser.parse_args()

file_path = Path(args.file)
if not file_path.exists():
    print(f"Error: {file_path} does not exist!", file=stderr)
    exit(1)

if not args.no_backup:
    backup = file_path.with_suffix(file_path.suffix + ".bak")
    copyfile(file_path, backup)
    print(f"Backup created: {backup}")

with file_path.open("r") as f:
    lines = f.readlines()

converted = convert(lines, to_tabs=(args.type == "tab"), size=args.size)

with file_path.open("w") as f:
    f.writelines(converted)

print(f"Conversion to {args.type} complete.")
