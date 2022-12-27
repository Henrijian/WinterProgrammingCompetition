
NOOP_INSTRUCT = "noop"
ADDX_INSTRUCT = "addx"
CYCLE_DICT = {NOOP_INSTRUCT: 1, ADDX_INSTRUCT: 2}

if __name__ == "__main__":
    overlapPairsCount = 0
    inputFile = open("input.txt", "r")
    try:
        lines = inputFile.readlines()
        registerValueX = 1
        currentCycle = 0
        CRTRow = ""
        for line in lines:
            instructTokens = line.strip().split()
            instruct = instructTokens[0]
            if not instruct in CYCLE_DICT:
                continue
            addCycle = CYCLE_DICT[instruct]
            for i in range(addCycle):
                currentCycle += 1
                CRTIdx = len(CRTRow)
                if ((registerValueX - 1) <= CRTIdx) and (CRTIdx <= (registerValueX + 1)):
                    CRTRow += "#"
                else:
                    CRTRow += "."
                if len(CRTRow) == 40:
                    print(CRTRow)
                    CRTRow = ""
            if instruct == ADDX_INSTRUCT:
                instructParam = int(instructTokens[1])
                registerValueX += instructParam
    finally:
        inputFile.close()