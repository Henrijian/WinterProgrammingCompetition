SAND_SOURCE_CHAR = '+'
ROCK_CHAR = '#'
AIR_CHAR = '.'
SAND_CHAR = 'O'


class Point:
    def __init__(self, x, y):
        if not isinstance(x, int):
            raise ValueError("x must be int type")
        if not isinstance(y, int):
            raise ValueError("y must be int type")
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError("value must be int type")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise ValueError("value must be int type")
        self.__y = value

    def __str__(self):
        return "({},{})".format(self.x, self.y)

def showGrid(grid):
    if not isinstance(grid, list):
        raise ValueError("grid must be list type")
    if not isinstance(grid[0], list):
        raise ValueError("grid[0] must be list type")
    for row in grid:
        print(' '.join(row))

def sandCount(grid):
    if not isinstance(grid, list):
        raise ValueError("grid must be list type")
    if not isinstance(grid[0], list):
        raise ValueError("grid[0] must be list type")
    result = 0
    for row in grid:
        result += ''.join(row).count(SAND_CHAR)
    return result

def isBlockedSquare(grid, row, col):
    if not isinstance(grid, list):
        raise ValueError("grid must be list type")
    if not isinstance(grid[0], list):
        raise ValueError("grid[0] must be list type")
    rowCount = len(grid)
    colCount = len(grid[0])
    if (0 <= row < rowCount) and (0 <= col < colCount):
        return (grid[row][col] == ROCK_CHAR) or (grid[row][col] == SAND_CHAR)
    else:
        return False

def solution(grid, sandSourceRow, sandSourceCol):
    if not isinstance(grid, list):
        raise ValueError("grid must be list type")
    if not isinstance(grid[0], list):
        raise ValueError("grid[0] must be list type")
    rowCount = len(grid)
    colCount = len(grid[0])
    if not (0 <= sandSourceRow < rowCount and 0 <= sandSourceCol < colCount):
        raise ValueError("source point of sand out of range, row = {}, col = {}".format(sandSourceRow, sandSourceCol))

    while (True):
        prevSandCount = sandCount(grid)
        sandCol = sandSourceCol
        for sandRow in range(sandSourceRow, rowCount):
            nextCol = sandCol
            nextRow = sandRow + 1
            if not isBlockedSquare(grid, nextRow, nextCol):
                continue
            nextCol = sandCol - 1
            if not isBlockedSquare(grid, nextRow, nextCol):
                sandCol = nextCol
                continue
            nextCol = sandCol + 1
            if not isBlockedSquare(grid, nextRow, nextCol):
                sandCol = nextCol
                continue
            grid[sandRow][sandCol] = SAND_CHAR
            break
        currSandCount = sandCount(grid)
        if currSandCount == prevSandCount:
            break
    return currSandCount

if __name__ == "__main__":
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
    sandSource = Point(500, 0)
    minX = sandSource.x
    maxX = sandSource.x
    minY = sandSource.y
    maxY = sandSource.y
    rockTraces = []
    for line in lines:
        trimmedLine = line.strip()
        rockTrace = []
        pathTokens = trimmedLine.split("->")
        for pathToken in pathTokens:
            pathToken = pathToken.strip()
            pointTokens = pathToken.split(',')
            pointX = int(pointTokens[0])
            pointY = int(pointTokens[1])
            point = Point(pointX, pointY)
            rockTrace.append(point)
            if pointX < minX:
                minX = pointX
            if pointX > maxX:
                maxX = pointX
            if pointY < minY:
                minY = pointY
            if pointY > maxY:
                maxY = pointY
        rockTraces.append(rockTrace)
    # define width and height of the grid
    maxY += 2 # 2 for the floor
    sourceToFloorHeight = maxY - sandSource.y + 1
    minX = min(minX, sandSource.x - sourceToFloorHeight + 1)
    maxX = max(maxX, sandSource.x + sourceToFloorHeight - 1)
    width = maxX - minX + 1
    height = maxY - minY + 1
    # init empty grid
    grid = [[AIR_CHAR] * width for _ in range(height)]
    # add sand source
    grid[sandSource.y - minY][sandSource.x - minX] = SAND_SOURCE_CHAR
    # add rocks
    for rockTrace in rockTraces:
        prevPoint = rockTrace.pop(0)
        while len(rockTrace) > 0:
            currPoint = rockTrace.pop(0)
            if prevPoint.x == currPoint.x:
                fromY = min(prevPoint.y, currPoint.y)
                toY = max(prevPoint.y, currPoint.y)
                for i in range(fromY, toY + 1):
                    grid[i - minY][prevPoint.x - minX] = ROCK_CHAR
            elif prevPoint.y == currPoint.y:
                fromX = min(prevPoint.x, currPoint.x)
                toX = max(prevPoint.x, currPoint.x)
                for i in range(fromX, toX + 1):
                    grid[prevPoint.y - minY][i - minX] = ROCK_CHAR
            else:
                raise ValueError("invalid rock trace!")
            prevPoint = currPoint
    for i in range(width):
        grid[height - 1][i] = ROCK_CHAR
    result = solution(grid, sandSource.y - minY, sandSource.x - minX)
    showGrid(grid)
    print(result)
