
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

        highestScenicScore = 0
        for row, trees in enumerate(map):
            for col, tree in enumerate(trees):
                treeHeight = map[row][col]
                # check left
                leftVisible = 0
                for i in range(col - 1, -1, -1):
                    leftVisible += 1
                    if map[row][i] >= treeHeight:
                        break
                # check top
                topVisible = 0
                for i in range(row - 1, -1, -1):
                    topVisible += 1
                    if map[i][col] >= treeHeight:
                        break
                # check right
                rightVisible = 0
                for i in range(col + 1, colCount):
                    rightVisible += 1
                    if map[row][i] >= treeHeight:
                        break
                # check bottom
                bottomVisible = 0
                for i in range(row + 1, rowCount):
                    bottomVisible += 1
                    if map[i][col] >= treeHeight:
                        break
                scenicScore = leftVisible * topVisible * rightVisible * bottomVisible
                if scenicScore > highestScenicScore:
                    highestScenicScore = scenicScore
        print(highestScenicScore)
    finally:
        inputFile.close()