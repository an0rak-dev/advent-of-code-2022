import argparse
import urllib.request

BASE_URL="https://adventofcode.com"
YEAR="2022"


def get_cmdline_args():
    parser = argparse.ArgumentParser(
        prog = "aoc-prepare-problem",
        description = "Create a new solution skeleton for an \
        Advent of Code day and download the problem's text")
    parser.add_argument("day", help="The day to solve")
    return parser.parse_args()


def main():
    args = get_cmdline_args()
    riddle_url = f"{BASE_URL}/{YEAR}/day/{args.day}"
    try:
        with urllib.request.urlopen(riddle_url) as ptr:
            page_bytes = ptr.read()
            # TODO : Retrieve only the riddle from the webpage.
    except urllib.error.URLError as e: 
        print(f"Unable to open the AdventOfCode riddle ({riddle_url}): {e}")

    
if __name__ == "__main__":
    main()
