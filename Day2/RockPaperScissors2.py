#  First column:
#      A for Rock, B for Paper, and C for Scissors
# Second column:
#      X for Lost, Y for Draw, and Z for Win
# Scores:
#     1 for Rock, 2 for Paper, and 3 for Scissors
#     0 if you lost, 3 if the round was a draw, and 6 if you won
import sys
from enum import Enum

class Shape(Enum):
    UNKNOWN = 0
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Outcome(Enum):
    UNKNOWN = 0
    LOSE = 1
    DRAW = 2
    WIN = 3

def charToShape(char):
    if not isinstance(char, str):
        return Shape.UNKNOWN
    result = Shape.UNKNOWN
    charLower = char.lower()
    if charLower == "a":
        result = Shape.ROCK
    elif charLower == "b":
        result = Shape.PAPER
    elif charLower == "c":
        result = Shape.SCISSORS
    return result

def charToOutcome(char):
    if not isinstance(char, str):
        return Outcome.UNKNOWN
    result = Outcome.UNKNOWN
    charLower = char.lower()
    if charLower == "x":
        result = Outcome.LOSE
    elif charLower == "y":
        result = Outcome.DRAW
    elif charLower == "z":
        result = Outcome.WIN
    return result

def shapeToPoint(shape):
    if not isinstance(shape, Shape):
        raise ValueError("shape must be Shape type")
    point = 0
    if shape == Shape.ROCK:
        point = 1
    elif shape == Shape.PAPER:
        point = 2
    elif shape == Shape.SCISSORS:
        point = 3
    return point

def outcomeToPoint(outcome):
    if not isinstance(outcome, Outcome):
        raise ValueError("outcome must be Outcome type")
    point = 0
    if outcome == Outcome.LOSE:
        point = 0
    elif outcome == Outcome.DRAW:
        point = 3
    elif outcome == Outcome.WIN:
        point = 6
    return point

def playGame(opponentShape, expectOutcome):
    if not isinstance(opponentShape, Shape):
        raise ValueError("opponentShape must be Shape type")
    if not isinstance(expectOutcome, Outcome):
        raise ValueError("expectOutcome must be Outcome type")
    result = Shape.UNKNOWN
    if expectOutcome == Outcome.LOSE:
        if opponentShape == Shape.ROCK:
            result = Shape.SCISSORS
        elif opponentShape == Shape.PAPER:
            result = Shape.ROCK
        elif opponentShape == Shape.SCISSORS:
            result = Shape.PAPER
    elif expectOutcome == Outcome.DRAW:
        result = opponentShape
    elif expectOutcome == Outcome.WIN:
        if opponentShape == Shape.ROCK:
            result = Shape.PAPER
        elif opponentShape == Shape.PAPER:
            result = Shape.SCISSORS
        elif opponentShape == Shape.SCISSORS:
            result = Shape.ROCK
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("I need a input file")
        sys.exit()
    point = 0
    inputFilePath = sys.argv[1]
    inputFile = open(inputFilePath, "r")
    try:
        lines = inputFile.readlines()
        for line in lines:
            token = line.strip().split(" ")
            opponentChar = token[0]
            outcomeChar = token[1]
            opponentShape = charToShape(opponentChar)
            outcome = charToOutcome(outcomeChar)
            myShape = playGame(opponentShape, outcome)
            shapePoint = shapeToPoint(myShape)
            outcomePoint = outcomeToPoint(outcome)
            point += (shapePoint + outcomePoint)
        print(point)
    finally:
        inputFile.close()