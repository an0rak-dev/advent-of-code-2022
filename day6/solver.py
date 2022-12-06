INPUT_FILE="input.txt"


def count(input, char):
    result = 0
    for c in input:
        if c == char:
            result += 1
    return result


def solve1(input):
    for idx in range(3, len(input), 1):
        to_analyse = input[idx-3:idx+1]
        is_datastream_start = True
        for char in to_analyse:
            if count(to_analyse, char) > 1:
                is_datastream_start = False
                break
        if is_datastream_start:
            return idx + 1
    return -1
    

def solve2(input):
    for idx in range(14, len(input), 1):
        to_analyse = input[idx-13:idx+1]
        is_message_start = True
        for char in to_analyse:
            if count(to_analyse, char) > 1:
                is_message_start = False
                break
        if is_message_start:
            return idx + 1
    return -1


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