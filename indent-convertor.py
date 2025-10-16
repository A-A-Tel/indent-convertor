#!/bin/env python3
import argparse
from argparse import ArgumentParser
from os.path import exists

parser = ArgumentParser()

parser.description = "Converts spaces into tabs, or tabs into spaces! Whitespace-only lines will be cleared entirely"

parser.add_argument("type", help="Type of indentation to convert to", choices=["tab", "space"], type=str)
parser.add_argument("size", help="The amount of spaces per indent", type=int)
parser.add_argument("file", help="The file to be converted", type=str)

args = parser.parse_args()

TYPE = args.type
SIZE = args.size
FILE = args.file


if not exists(FILE):
    print(f"File {FILE} does not exist!")
    exit(1)

with open(FILE, "r") as file:
    lines = file.readlines()


