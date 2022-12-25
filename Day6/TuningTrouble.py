if __name__ == "__main__":
    overlapPairsCount = 0
    inputFile = open("input.txt", "r")
    try:
        startOfPacketMarker = []
        lines = inputFile.readlines()
        for line in lines:
            for i, char in enumerate(line):
                startOfPacketMarker.append(char)
                if len(startOfPacketMarker) > 4:
                    startOfPacketMarker.pop(0)
                if len(set(startOfPacketMarker)) == 4:
                    print(i + 1)
                    break
    finally:
        inputFile.close()