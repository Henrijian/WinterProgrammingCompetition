import re
from functools import cmp_to_key
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
        return "{}: ({},{})".format(self.__class__.__name__, self.x, self.y)

class Sensor(Point):
    def __str__(self):
        return "{}: ({},{})".format(self.__class__.__name__, self.x, self.y)

class Beacon(Point):
    def __str__(self):
        return "{}: ({},{})".format(self.__class__.__name__, self.x, self.y)

class Range:
    def __init__(self, fromScale, toScale):
        if not isinstance(fromScale, int):
            raise ValueError("fromScale must be int type")
        if not isinstance(toScale, int):
            raise ValueError("toScale must be int type")
        validatedFrom = min(fromScale, toScale)
        validatedTo = max(fromScale, toScale)
        self.__fromScale = validatedFrom
        self.__toScale = validatedTo

    @property
    def fromScale(self):
        return self.__fromScale

    @fromScale.setter
    def fromScale(self, value):
        if not isinstance(value, int):
            raise ValueError("value must be int type")
        self.__fromScale = value

    @property
    def toScale(self):
        return self.__toScale

    @toScale.setter
    def toScale(self, value):
        if not isinstance(value, int):
            raise ValueError("value must be int type")
        self.__toScale = value

    def __str__(self):
        return "{}: {} -> {}".format(self.__class__.__name__, self.fromScale, self.toScale)

    def isIntersect(self, other):
        if not isinstance(other, Range):
            raise ValueError("other must Range type")
        if self.fromScale <= other.fromScale:
            return self.toScale >= other.fromScale
        else:
            return self.fromScale <= other.toScale

    def union(self, other):
        if not isinstance(other, Range):
            raise ValueError("other must Range type")
        minScale = min(self.fromScale, other.fromScale)
        maxScale = max(self.toScale, other.toScale)
        return Range(minScale, maxScale)

class Pair:
    def __init__(self, sensor, beacon):
        if not isinstance(sensor, Sensor):
            raise ValueError("sensor must be Sensor type")
        if not isinstance(beacon, Beacon):
            raise ValueError("beacon must be Beacon type")
        self.__sensor = sensor
        self.__beacon = beacon

    @property
    def sensor(self):
        return self.__sensor

    @property
    def beacon(self):
        return self.__beacon

    def __str__(self):
        return "{} - {}".format(self.sensor, self.beacon)

    def waveXRangeAt(self, y):
        if not isinstance(y, int):
            raise ValueError("y must be int type")
        deltaX = abs(self.sensor.x - self.beacon.x)
        deltaY = abs(self.sensor.y - self.beacon.y)
        waveDistance = deltaX + deltaY
        yDistance = abs(self.sensor.y - y)
        if not (yDistance <= waveDistance):
            return None
        xDistance = waveDistance - yDistance
        return Range(self.sensor.x - xDistance, self.sensor.x + xDistance)

def compareRanges(rangeA, rangeB):
    if not isinstance(rangeA, Range):
        raise ValueError("rangeA must be Range type")
    if not isinstance(rangeB, Range):
        raise ValueError("rangeB must be Range type")
    return rangeA.fromScale - rangeB.fromScale

if __name__ == "__main__":
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
    scanY = 2000000
    xRanges = []
    scanYBeacons = []
    for line in lines:
        trimmedLine = line.strip()
        matches = re.search("Sensor at x=([-]*\d+), y=([-]*\d+): closest beacon is at x=([-]*\d+), y=([-]*\d+)", trimmedLine)
        if not matches:
            raise ValueError("input is invalid, line = {}".format(line))
        sensor = Sensor(int(matches[1]), int(matches[2]))
        beacon = Beacon(int(matches[3]), int(matches[4]))
        pair = Pair(sensor, beacon)
        xRange = pair.waveXRangeAt(scanY)
        if xRange is None:
            continue
        xRanges.append(xRange)
        if beacon.y == scanY:
            duplicated = False
            for scanYBeacon in scanYBeacons:
                if scanYBeacon.x == beacon.x:
                    duplicated = True
                    break
            if not duplicated:
                scanYBeacons.append(beacon)
    # union ranges in xRanges
    xRanges.sort(key=cmp_to_key(compareRanges), reverse=True)
    separatedXRanges = []
    while len(xRanges) > 0:
        xRange = xRanges.pop()
        for i in range(len(xRanges) - 1, -1, -1):
            checkXRange = xRanges[i]
            if not checkXRange.isIntersect(xRange):
                continue
            xRange = xRange.union(checkXRange)
            xRanges.pop(i)
        separatedXRanges.append(xRange)
    # get the infected range of x
    result = 0
    for xRange in separatedXRanges:
        result += (xRange.toScale - xRange.fromScale + 1)
    result -= len(scanYBeacons) # do not count beacon occupations
    print(result)