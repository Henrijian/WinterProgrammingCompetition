
NOOP_INSTRUCT = "noop"
ADDX_INSTRUCT = "addx"
CYCLE_DICT = {NOOP_INSTRUCT: 1, ADDX_INSTRUCT: 2}

if __name__ == "__main__":
    overlapPairsCount = 0
    inputFile = open("input.txt", "r")
    try:
        lines = inputFile.readlines()
        wantedSignalStrength = 0
        wantedCycles = {20, 60, 100, 140, 180, 220}
        registerValueX = 1
        currentCycle = 0
        for line in lines:
            instructTokens = line.strip().split()
            instruct = instructTokens[0]
            if not instruct in CYCLE_DICT:
                continue
            addCycle = CYCLE_DICT[instruct]
            for i in range(addCycle):
                currentCycle += 1
                if currentCycle in wantedCycles:
                    wantedSignalStrength += (currentCycle * registerValueX)
            if instruct == ADDX_INSTRUCT:
                instructParam = int(instructTokens[1])
                registerValueX += instructParam

        print(wantedSignalStrength)
    finally:
        inputFile.close()