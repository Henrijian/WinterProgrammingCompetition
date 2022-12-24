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

def findDuplicatedChars(str1, str2, str3):
    if not isinstance(str1, str):
        raise ValueError("str1 must be str type")
    if not isinstance(str2, str):
        raise ValueError("str2 must be str type")
    if not isinstance(str3, str):
        raise ValueError("str3 must be str type")
    result = set()
    chars1 = set(str1)
    chars1and2 = set()
    for char in str2:
        if char in chars1:
            chars1and2.add(char)
    for char in str3:
        if char in chars1and2:
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
        groupLines = []
        for line in lines:
            groupLines.append(line.strip())
            if len(groupLines) == 3:
                duplicatedChars = findDuplicatedChars(groupLines[0], groupLines[1], groupLines[2])
                for duplicatedChar in duplicatedChars:
                    sum += charToPriority(duplicatedChar)
                groupLines = []
        print(sum)
    finally:
        inputFile.close()