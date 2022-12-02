INPUT_FILE = "input.txt"

def sort_elves_harvests_desc(input):
    harvest_per_elves = input.split("\n\n")
    total_per_elves = []
    for elf_harvest in harvest_per_elves:
        total = 0
        harvest = elf_harvest.split("\n")
        for qty in harvest:
            if (len(qty) > 0):
                total += int(qty)
        total_per_elves.append(total)
    total_per_elves.sort(reverse=True)
    return total_per_elves

def solve1(input):
    total_per_elves = sort_elves_harvests_desc(input)
    return total_per_elves[0]


def solve2(input):
    total_per_elves = sort_elves_harvests_desc(input)
    return total_per_elves[0] + total_per_elves[1] + total_per_elves[2]

def main():
    input = ""
    with open(INPUT_FILE, "r") as input_fd:
        input = input_fd.read()
    result1 = solve1(input)
    result2 = solve2(input)
    print(f"Solution for part 1 is : {result1}")
    print(f"Solution for part 2 is : {result2}")


if __name__ == "__main__":
    main()