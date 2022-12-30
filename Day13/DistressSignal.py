
class Packet:
    def __init__(self, raw):
        if not isinstance(raw, str):
            raise ValueError("raw is not str type")
        self.__raw = raw
        self.__data = self.rawToData(raw)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, list):
            raise ValueError("value must be list type")
        self.__data = value
    def rawToData(self, raw):
        if not isinstance(raw, str):
            raise ValueError("raw is not str type")
        result = []
        raw = raw[1:-1] # remove square brackets
        token = ''
        i = 0
        while i < len(raw):
            char = raw[i]
            i += 1

            if char == ',':
                if isinstance(token, list):
                    result.append(token)
                else:
                    result.append(int(token))
                token = ''
            elif char == '[':
                rawToken = char
                leftBracketCount = 1
                rightBracketCount = 0
                for j in range(i, len(raw)):
                    subChar = raw[j]
                    rawToken += subChar
                    if subChar == '[':
                        leftBracketCount += 1
                    elif subChar == ']':
                        rightBracketCount += 1
                    if leftBracketCount == rightBracketCount:
                        i = j + 1
                        break
                token = self.rawToData(rawToken)
            else:
                token += char
        if isinstance(token, list):
            result.append(token)
        elif token != '':
            result.append(int(token))
        return result

    def compare(self, itemA, itemB):
        if isinstance(itemA, int) and isinstance(itemB, int):
            if itemA < itemB:
                result = -1
            elif itemA > itemB:
                result = 1
            else:
                result = 0
            return result

        if isinstance(itemA, list) and isinstance(itemB, int):
            itemB = [itemB]
        if isinstance(itemA, int) and isinstance(itemB, list):
            itemA = [itemA]
        countA = len(itemA)
        countB = len(itemB)
        compareSize = min(countA, countB)
        for i in range(compareSize):
            result = self.compare(itemA[i], itemB[i])
            if result != 0:
                return result
        if countA < countB:
            result = -1
        elif countA > countB:
            result = 1
        else:
            result = 0
        return result

    def lessThan(self, other):
        if not isinstance(other, Packet):
            raise ValueError("other muse be Packet type")
        compareResult = self.compare(self.data, other.data)
        return compareResult <= 0

if __name__ == "__main__":
    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
    packetPairs = []
    packetPair = []
    result = 0
    for line in lines:
        trimmedLine = line.strip()
        if trimmedLine == '':
            continue
        packet = Packet(trimmedLine)
        packetPair.append(packet)
        if len(packetPair) == 2:
            packetFirst = packetPair[0]
            packetSecond = packetPair[1]
            packetPairs.append([packetFirst, packetSecond])
            if packetFirst.lessThan(packetSecond):
                result += len(packetPairs)
            packetPair = []
    print(result)




