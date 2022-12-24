import re
class Stack(list):
    def push(self, item):
        self.insert(0, item)

    def pile(self, item):
        self.insert(len(self), item)

    def top(self):
        return self[len(self)-1]

    def bottom(self):
        return self[0]

if __name__ == "__main__":
    overlapPairsCount = 0
    inputFile = open("input.txt", "r")
    try:
        stacksEnd = False
        stacks = []
        lines = inputFile.readlines()
        for line in lines:
            if not stacksEnd:
                charCount = len(line)
                chunkSize = 3
                chunks = [line[i:i+chunkSize] for i in range(0, charCount, chunkSize+1)]
                for i, chunk in enumerate(chunks):
                    while len(stacks) <= i:
                        stacks.append(Stack())
                    chunk = chunk.strip()
                    if chunk.isdecimal():
                        stacksEnd = True
                    elif chunk != "":
                        stack = stacks[i]
                        stack.push(chunk)
            else:
                matches = re.search("move (\d+) from (\d+) to (\d+)", line.strip())
                if matches is None:
                    continue
                count = int(matches[1])
                fromIdx = int(matches[2]) - 1
                toIdx = int(matches[3]) - 1
                fromStack = stacks[fromIdx]
                toStack = stacks[toIdx]
                for i in range(count):
                    item = fromStack.pop()
                    toStack.pile(item)
        result = ""
        for stack in stacks:
            if len(stacks) > 0:
                result += stack.top()
        print(result.replace("[", "").replace("]", ""))
    finally:
        inputFile.close()