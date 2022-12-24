import sys


def charToPriority(char):
    if not isinstance(char, str):
        raise ValueError("char must be str type")
    if not len(char) == 1:
        raise ValueError("char must be a character")
    result = 0
    if char.islower():
        result = ord(char) - ord('a') + 1
    elif char.isupper():
        result = ord(char) - ord('A') + 1 + 26
    return result

def findDuplicatedChars(firstStr, secondStr):
    if not isinstance(firstStr, str):
        raise ValueError("firstStr must be str type")
    if not isinstance(secondStr, str):
        raise ValueError("secondStr must be str type")
    result = set()
    firstChars = set(firstStr)
    for char in secondStr:
        if char in firstChars:
            result.add(char)
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("I need a input file")
        sys.exit()
    sum = 0
    inputFilePath = sys.argv[1]
    inputFile = open(inputFilePath, "r")
    try:
        lines = inputFile.readlines()
        for line in lines:
            length = len(line.strip())
            midPoint = round(length / 2)
            firstHalf = line[:midPoint]
            secondHalf = line[midPoint:]
            duplicatedChars = findDuplicatedChars(firstHalf, secondHalf)
            for duplicatedChar in duplicatedChars:
                sum += charToPriority(duplicatedChar)
        print(sum)
    finally:
        inputFile.close()