
if __name__ == "__main__":
    overlapPairsCount = 0
    inputFile = open("input.txt", "r")
    try:
        lines = inputFile.readlines()
        colCount = len(lines[0].strip())
        rowCount = len(lines)
        map = []
        for line in lines:
            row = []
            line = line.strip()
            for char in line:
                row.append(char)
            map.append(row)

        visibleTreeCount = 0
        for row, trees in enumerate(map):
            for col, tree in enumerate(trees):
                if (row == 0) or (row == rowCount - 1) or (col == 0) or (col == colCount - 1):
                    visibleTreeCount += 1
                    continue
                treeHeight = map[row][col]
                # check left
                leftBlock = False
                for i in range(col):
                    if map[row][i] >= treeHeight:
                        leftBlock = True
                        break
                if not leftBlock:
                    visibleTreeCount += 1
                    continue
                # check top
                topBlock = False
                for i in range(row):
                    if map[i][col] >= treeHeight:
                        topBlock = True
                        break
                if not topBlock:
                    visibleTreeCount += 1
                    continue
                # check right
                rightBlock = False
                for i in range(col + 1, colCount):
                    if map[row][i] >= treeHeight:
                        rightBlock = True
                        break
                if not rightBlock:
                    visibleTreeCount += 1
                    continue
                # check bottom
                bottomBlock = False
                for i in range(row + 1, rowCount):
                    if map[i][col] >= treeHeight:
                        bottomBlock = True
                        break
                if not bottomBlock:
                    visibleTreeCount += 1
                    continue
        print(visibleTreeCount)
    finally:
        inputFile.close()