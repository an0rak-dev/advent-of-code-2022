INPUT_FILE="input.txt"


def solve1(input):
    # TODO: Code here
    pass


def solve2(input):
    # TODO: Code here
    pass

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