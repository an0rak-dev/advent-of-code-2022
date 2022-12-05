INPUT_FILE="example.txt"

import re


def get_stacks(input):
    end_stacks = input.find("\n\n")
    stack_repr = input[0:end_stacks].split('\n')
    indices = stack_repr[len(stack_repr) - 1]
    column_names = indices.strip().split('   ')
    stacks = [ [] for i in range(len(column_names)) ]
    for line_idx in range(len(stack_repr)-2, -1, -1):
        line = stack_repr[line_idx]
        stack_idx = 0
        for i in range(1, len(line)-1, 4):
            if line[i] != ' ':
                stacks[stack_idx].append(line[i])
            stack_idx += 1
        stack_idx = 0
    return stacks


def get_instructions(input):
    end_stacks = input.find("\n\n")
    instructions = input[end_stacks+2:].split('\n')
    result = []
    for instruction in instructions:
        if len(instruction) < 1:
            continue
        words = instruction.split(' ')
        qty = int(words[1])
        src = int(words[3])
        dest = int(words[5])
        result.append((qty, src, dest))
    return result



def solve1(input):
    stacks = get_stacks(input)
    instructions = get_instructions(input)
    for instruction in instructions:
        qty, src, dest = instruction
        for i in range(qty):
            elt = stacks[src-1].pop()
            stacks[dest-1].append(elt)
    result = ""
    for stack in stacks:
        result += stack.pop()
    return result


def solve2(input):
    stacks = get_stacks(input)
    instructions = get_instructions(input)
    for instruction in instructions:
        qty, src, dest = instruction
        tmp = []
        for i in range(qty):
            elt = stacks[src-1].pop()
            tmp.append(elt)
        for i in range(qty):
            elt = tmp.pop()
            stacks[dest-1].append(elt)
    result = ""
    for stack in stacks:
        result += stack.pop()
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