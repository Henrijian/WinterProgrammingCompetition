if __name__ == "__main__":
    overlapPairsCount = 0
    inputFile = open("input.txt", "r")
    try:
        startOfMessageMarker = []
        lines = inputFile.readlines()
        for line in lines:
            for i, char in enumerate(line):
                startOfMessageMarker.append(char)
                if len(startOfMessageMarker) > 14:
                    startOfMessageMarker.pop(0)
                if len(set(startOfMessageMarker)) == 14:
                    print(i + 1)
                    break
    finally:
        inputFile.close()