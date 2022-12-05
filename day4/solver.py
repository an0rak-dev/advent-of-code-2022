INPUT_FILE="input.txt"


def to_range(sections):
    parts = sections.split('-')
    begin = int(parts[0])
    end = int(parts[1])
    return range(begin, end +1)


def solve1(input):
    pairs = input.split('\n')
    result = 0
    for pair in pairs:
        elves = pair.split(',')
        elf1 = to_range(elves[0])
        elf2 = to_range(elves[1])
        overlap1 = [ section for section in elf1 if section in elf2 ]
        overlap2 = [ section for section in elf2 if section in elf1 ]
        if len(elf1) == len(overlap1) or len(elf2) == len(overlap2):
            result += 1
    return result


def solve2(input):
    pairs = input.split('\n')
    result = 0
    for pair in pairs:
        elves = pair.split(',')
        elf1 = to_range(elves[0])
        elf2 = to_range(elves[1])
        overlap1 = [ section for section in elf1 if section in elf2 ]
        overlap2 = [ section for section in elf2 if section in elf1 ]
        if len(overlap1) > 0 or len(overlap2) > 0:
            result += 1
    return result


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