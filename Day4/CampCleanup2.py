import sys

class Sections:
    _startSection = -1
    _endSection = -1

    def __init__(self, startSection, endSection):
        if not isinstance(startSection, int):
            raise ValueError("startSection must be int type")
        if not isinstance(endSection, int):
            raise ValueError("endSection must be int type")
        if not (startSection <= endSection):
            raise ValueError("startSection must be less than or equal to endSection")
        self._startSection = startSection
        self._endSection = endSection

    @classmethod
    def fromString(cls, rangeStr):
        if not isinstance(rangeStr, str):
            raise ValueError("rangeStr must be int type")
        rangeTokens = rangeStr.split("-")
        if not (len(rangeTokens) >= 2):
            raise ValueError("rangeTokens must have at least 2 tokens")
        start = int(rangeTokens[0])
        end = int(rangeTokens[1])
        return cls(start, end)

    def startSection(self):
        return self._startSection

    def endSection(self):
        return self._endSection

    def contains(self, other):
        if not isinstance(other, Sections):
            raise ValueError("other must be Sections type")
        return (self.startSection() <= other.startSection()) and (other.endSection() <= self.endSection())

    def overlap(self, other):
        if not isinstance(other, Sections):
            raise ValueError("other must be Sections type")
        if self.startSection() <= other.startSection():
            leftSection = self
            rightSection = other
        else:
            leftSection = other
            rightSection = self
        return rightSection.startSection() <= leftSection.endSection()

if __name__ == "__main__":
    overlapPairsCount = 0
    inputFile = open("input.txt", "r")
    try:
        lines = inputFile.readlines()
        for line in lines:
            pair = line.strip().split(",")
            sections1 = Sections.fromString(pair[0])
            sections2 = Sections.fromString(pair[1])
            if sections1.overlap(sections2):
                overlapPairsCount += 1
        print(overlapPairsCount)
    finally:
        inputFile.close()