INPUT_FILE="input.txt"

from math import trunc

def get_priority_of(item):
    base_lower = ord('a')
    base_upper = ord('A')
    code_item = ord(item)
    if code_item < base_lower:
        return 27 + (code_item - base_upper)
    else:
        return 1 + (code_item - base_lower)
    return 0


def solve1(input):
    ruckstacks = input.split('\n')
    result = 0
    for ruckstack in ruckstacks:
        compartment_size = trunc(len(ruckstack) / 2)
        compartment1 = ruckstack[0:compartment_size]
        compartment2 = ruckstack[compartment_size:]
        appears_in_both = set([ item for item in compartment1 if item in compartment2 ])
        ruckstack_priority = 0
        for item in appears_in_both:
            ruckstack_priority += get_priority_of(item)
        result += ruckstack_priority
    return result


def solve2(input):
    ruckstacks = input.split('\n')
    result = 0
    for index in range(0, len(ruckstacks), 3):
        appears_in_group = set([ item for item in ruckstacks[index] if (item in ruckstacks[index + 1] and item in ruckstacks[index + 2]) ])
        for item in appears_in_group:
            result += get_priority_of(item)
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