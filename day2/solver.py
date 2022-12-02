INPUT_FILE="input.txt"

class HandShape:
    def getBaseScore(self):
        return 0

    def getName(self):
        return ""
    
    def createCopy(self):
        return None

    def createEnemy(self):
        return None 

    def createVictim(self):
        return None

    def resolve(self, shapeAgainst):
        return 0


class Rock(HandShape):
    def getBaseScore(self):
        return 1

    def getName(self):
        return "rock"
    
    def createCopy(self):
        return Rock()

    def createEnemy(self):
        return Paper() 

    def createVictim(self):
        return Scissor()

    def resolve(self, shapeAgainst):
        if shapeAgainst.getName() == "scissor":
            return 6
        elif shapeAgainst.getName() == "rock":
            return 3
        return 0


class Paper(HandShape):
    def getBaseScore(self):
        return 2

    def getName(self):
        return "paper"
        
    def createCopy(self):
        return Paper()

    def createEnemy(self):
        return Scissor() 

    def createVictim(self):
        return Rock()

    def resolve(self, shapeAgainst):
        if shapeAgainst.getName() == "rock":
            return 6
        elif shapeAgainst.getName() == "paper":
            return 3
        return 0


class Scissor(HandShape):
    def getBaseScore(self):
        return 3

    def getName(self):
        return "scissor"

    def createCopy(self):
        return Scissor()

    def createEnemy(self):
        return Rock() 

    def createVictim(self):
        return Paper()

    def resolve(self, shapeAgainst):
        if shapeAgainst.getName() == "paper":
            return 6
        elif shapeAgainst.getName() == "scissor":
            return 3
        return 0


def convert_to_shape(letter):
    if letter == "A" or letter == "X":
        return Rock()
    elif letter == "B" or letter == "Y":
        return Paper()
    elif letter == "C" or letter == "Z":
        return Scissor()
    else:
        return None


def predict(letter, shape):
    if letter == "X":
        return shape.createVictim()
    elif letter == "Y":
        return shape.createCopy()
    elif letter == "Z":
        return shape.createEnemy()
    else:
        return None


def solve1(input):
    rounds = input.split("\n")
    total = 0
    for round in rounds:
        parts = round.split(" ")
        if len(parts) != 2:
            continue
        opponent = convert_to_shape(parts[0])
        elf = convert_to_shape(parts[1])
        total += elf.getBaseScore() + elf.resolve(opponent)
    return total


def solve2(input):
    rounds = input.split("\n")
    total = 0
    for round in rounds:
        parts = round.split(" ")
        if len(parts) != 2:
            continue
        opponent = convert_to_shape(parts[0])
        elf = predict(parts[1], opponent)
        total += elf.getBaseScore() + elf.resolve(opponent)
    return total


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