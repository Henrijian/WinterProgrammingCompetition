from heapq import heapify, heappop, heappush

def height(char):
    if char == 'S':
        return ord('a')
    if char == 'E':
        return ord('z')
    return ord(char)

def getNeighbors(grid, currRow, currCol):
    if not (isinstance(grid, list) and isinstance(grid[0], list)):
        raise ValueError("grid is not a matrix")
    rowCount = len(grid)
    colCount = len(grid[0])
    if not isinstance(currRow, int):
        raise ValueError("currRow must be int type")
    if not isinstance(currCol, int):
        raise ValueError("currCol must be int type")
    if not (0 <= currRow < rowCount and 0 <= currCol < colCount):
        raise ValueError("current row and col are not in grid")
    currHeight = height(grid[currRow][currCol])

    directions = [[0, 1], # right
                  [0, -1], # left
                  [1, 0], # down
                  [-1, 0]] # up
    result = []
    for direction in directions:
        nextRow = currRow + direction[0]
        nextCol = currCol + direction[1]
        if not (0 <= nextRow < rowCount and 0 <= nextCol < colCount):
            continue
        nextHeight = height(grid[nextRow][nextCol])
        if not ((nextHeight - currHeight) <= 1):
            continue
        result.append([nextRow, nextCol])
    return result

def stepsToEnd(grid, startRow, startCol, endRow, endCol):
    if not (isinstance(grid, list) and isinstance(grid[0], list)):
        raise ValueError("grid is not a matrix")
    rowCount = len(grid)
    colCount = len(grid[0])
    if not isinstance(startRow, int):
        raise ValueError("startRow must be int type")
    if not isinstance(startCol, int):
        raise ValueError("startCol must be int type")
    if not (0 <= startRow < rowCount and 0 <= startCol < colCount):
        raise ValueError("start row and col are not in the grid")
    if not isinstance(endRow, int):
        raise ValueError("endRow must be int type")
    if not isinstance(endCol, int):
        raise ValueError("endCol must be int type")
    if not (0 <= endRow < rowCount and 0 <= endCol < colCount):
        raise ValueError("end row and col are not in the grid")
    result = rowCount * colCount
    visited = [[False] * colCount for _ in range(rowCount)]
    heap = [(0, startRow, startCol)]
    while len(heap) > 0:
        steps, row, col = heappop(heap)

        if visited[row][col]:
            continue
        visited[row][col] = True

        if (row == endRow) and (col == endCol):
            result = steps
            break

        neighbors = getNeighbors(grid, row, col)
        for neighbor in neighbors:
            heappush(heap, (steps + 1, neighbor[0], neighbor[1]))
    return result

if __name__ == "__main__":
    grid = []
    startRows = []
    startCols = []
    endRow = -1
    endCol = -1
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
    for row, line in enumerate(lines):
        trimmedLine = line.strip()
        gridRow = []
        for col, char in enumerate(trimmedLine):
            if char == 'S' or char == 'a':
                startRows.append(row)
                startCols.append(col)
            elif char == 'E':
                endRow = row
                endCol = col
            gridRow.append(char)
        grid.append(gridRow)
    rowCount = len(grid)
    colCount = len(grid[0])

    minSteps = rowCount * colCount
    for i in range(len(startRows)):
        startRow = startRows[i]
        startCol = startCols[i]
        steps = stepsToEnd(grid, startRow, startCol, endRow, endCol)
        if steps < minSteps:
            minSteps = steps
    print(minSteps)



