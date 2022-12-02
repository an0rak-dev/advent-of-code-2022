INPUT_FILE = "input.txt"

def solve(input):
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
    return total_per_elves[0]


def main():
    input = ""
    with open(INPUT_FILE, "r") as input_fd:
        input = input_fd.read()
    result = solve(input)
    print(f"Solution is : {result}")


if __name__ == "__main__":
    main()