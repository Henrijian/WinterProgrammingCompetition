#  First column:
#      A for Rock, B for Paper, and C for Scissors
# Second column:
#      X for Rock, Y for Paper, and Z for Scissors
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

def opponentCharToShape(char):
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

def myCharToShape(char):
    if not isinstance(char, str):
        return Shape.UNKNOWN
    result = Shape.UNKNOWN
    charLower = char.lower()
    if charLower == "x":
        result = Shape.ROCK
    elif charLower == "y":
        result = Shape.PAPER
    elif charLower == "z":
        result = Shape.SCISSORS
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

def play(opponentShape, myShape):
    if not isinstance(opponentShape, Shape):
        raise ValueError("opponentShape must be Shape type")
    if not isinstance(myShape, Shape):
        raise ValueError("myShape must be Shape type")
    result = Outcome.UNKNOWN
    if opponentShape == Shape.ROCK:
        if myShape == Shape.ROCK:
            result = Outcome.DRAW
        elif myShape == Shape.PAPER:
            result = Outcome.WIN
        elif myShape == Shape.SCISSORS:
            result = Outcome.LOSE
    elif opponentShape == Shape.PAPER:
        if myShape == Shape.ROCK:
            result = Outcome.LOSE
        elif myShape == Shape.PAPER:
            result = Outcome.DRAW
        elif myShape == Shape.SCISSORS:
            result = Outcome.WIN
    elif opponentShape == Shape.SCISSORS:
        if myShape == Shape.ROCK:
            result = Outcome.WIN
        elif myShape == Shape.PAPER:
            result = Outcome.LOSE
        elif myShape == Shape.SCISSORS:
            result = Outcome.DRAW
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
            myChar = token[1]
            opponentShape = opponentCharToShape(opponentChar)
            myShape = myCharToShape(myChar)
            outcome = play(opponentShape, myShape)
            shapePoint = shapeToPoint(myShape)
            outcomePoint = outcomeToPoint(outcome)
            point += (shapePoint + outcomePoint)
        print(point)
    finally:
        inputFile.close()