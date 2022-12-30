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
        if not ((currHeight - nextHeight) <= 1):
            continue
        result.append([nextRow, nextCol])
    return result

if __name__ == "__main__":
    grid = []
    visited = []
    endRow = -1
    endCol = -1
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
    for row, line in enumerate(lines):
        trimmedLine = line.strip()
        gridRow = []
        for col, char in enumerate(trimmedLine):
            if char == 'E':
                endRow = row
                endCol = col
            gridRow.append(char)
        grid.append(gridRow)
        visited.append([False] * len(gridRow))
    colCount = len(grid[0])
    rowCount = len(grid)

    heap = [(0, endRow, endCol)]
    while True:
        steps, row, col = heappop(heap)

        if visited[row][col]:
            continue
        visited[row][col] = True

        if height(grid[row][col]) == height('a'):
            print(steps)
            break

        neighbors = getNeighbors(grid, row, col)
        for neighbor in neighbors:
            heappush(heap, (steps + 1, neighbor[0], neighbor[1]))



