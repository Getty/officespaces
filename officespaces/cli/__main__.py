from .. import *

import argparse


def run(args):
    L_INFO("Starting CLI")


def main():
    parser = argparse.ArgumentParser(description="OfficeSpaces CLI client")

    # Define known arguments
    # parser.add_argument('--input', help="Input file", required=True)
    # parser.add_argument('--output', help="Output file", required=True)

    # Parse the known and unknown arguments
    args, unknown_args = parser.parse_known_args()

    if unknown_args:
        L_DEBUG(f"Unknown arguments: {unknown_args}")

    run(args)


if __name__ == "__main__":
    main()
