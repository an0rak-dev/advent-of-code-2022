from bs4 import BeautifulSoup
from markdownify import markdownify as md
from os import path
import argparse
import os
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


def scrap_riddle(day_number):
    riddle_url = f"{BASE_URL}/{YEAR}/day/{day_number}"
    try:
        with urllib.request.urlopen(riddle_url) as ptr:
            page_bytes = ptr.read()
            dom = BeautifulSoup(page_bytes.decode("utf8"), "html.parser")
            riddle_content = dom.body.main.article
            # Reformat the title : remove the '---' with is translated as a MD comment, and increase the title size.
            title = str(riddle_content.h2.string)
            riddle_content.h2.string.replace_with(title.replace("---", ""))
            riddle_content.h2.name = 'h1'
            return str(riddle_content)
    except urllib.error.URLError as e: 
        print(f"Unable to open the AdventOfCode riddle ({riddle_url}): {e}")
        return ""


def copy_solver(dest_folder):
    solver_code = ""
    solver_path = path.join(dest_folder, "solver.py")
    if path.exists(solver_path):
        return
    with open("template-solver.py", "r") as template:
        solver_code = template.read()
    with open(solver_path, "w") as solver:
        solver.write(solver_code)


def main():
    args = get_cmdline_args()
    print(f"Scraping the riddle of day {args.day} from the website")
    riddle_html = scrap_riddle(args.day)
    if len(riddle_html) == 0:
        return
    print("Converting the riddle in markdown")
    riddle_md = md(riddle_html)
    print("Creating the solution skeleton")
    dirname = f"day{args.day}"
    if not path.exists(dirname):
        os.mkdir(dirname)
    with open(path.join(dirname, "problem.md"), "w") as problem_file:
        problem_file.write(riddle_md)
    copy_solver(dirname)
    

    
if __name__ == "__main__":
    main()
