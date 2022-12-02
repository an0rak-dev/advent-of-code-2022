INPUT_FILE="input.txt"


def solve(input):
    # TODO: Code here
    pass


def main():
    input = ""
    with open(INPUT_FILE, "r") as input_fd:
        input = input_fd.read()
    result = solve(input)
    print(f"Solution is : {result}")


if __name__ == "__main__":
    main()