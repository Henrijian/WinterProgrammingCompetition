import re

class Monkey:
    NUM_PREFIX = "Monkey"
    STARTING_ITEMS_PREFIX = "Starting items:"
    OPERATION_PREFIX = "Operation:"
    TEST_PREFIX = "Test:"
    TRUE_PREFIX = "If true:"
    FALSE_PREFIX = "If false:"
    OLD_OPERAND = "old"
    def __init__(self, num):
        if not isinstance(num, int):
            raise ValueError("num must be int type")
        self._num = num
        self._items = []
        self._operationStr = ""
        self._testStr = ""
        self._trueActionStr = ""
        self._falseActionStr = ""
        self._inspectTimes = 0

    def num(self):
        return self._num

    def items(self):
        return self._items

    def operationStr(self):
        return self._operationStr

    def testStr(self):
        return self._testStr

    def trueActionStr(self):
        return self._trueActionStr

    def falseActionStr(self):
        return self._falseActionStr

    def inspectTimes(self):
        return self._inspectTimes

    def appendItem(self, item):
        if not isinstance(item, int):
            raise ValueError("item must be int type")
        self._items.append(item)

    def operate(self, item):
        if not isinstance(item, int):
            raise ValueError("item must be int type")
        operationStr = self.operationStr()
        matches = re.search("Operation: new = old (.) (.*)", operationStr)
        if matches is None:
            raise Exception("Cannot find operator and operand from operation string: {}".format(operationStr))
        operator = matches[1]
        operand = matches[2]
        result = item
        if operator == "+":
            if operand == self.OLD_OPERAND:
                result += item
            else:
                result += int(operand)
        elif operator == "*":
            if operand == self.OLD_OPERAND:
                result *= item
            else:
                result *= int(operand)
        else:
            raise Exception("Unknown operator: {}".format(operator))
        return result

    def test(self, item):
        if not isinstance(item, int):
            raise ValueError("item must be int type")
        self._inspectTimes += 1
        testStr = self.testStr()
        matches = re.search("Test: divisible by (\d+)", testStr)
        if matches is None:
            raise Exception("Cannot find divisor from test string: {}".format(testStr))
        divisor = int(matches[1])
        return (item % divisor) == 0

    def trueThrowMonkey(self):
        trueActionStr = self.trueActionStr()
        matches = re.search("If true: throw to monkey (\d+)", trueActionStr)
        if matches is None:
            raise Exception("Cannot find the monkey to throw from trueActionStr: {}".format(trueActionStr))
        target = int(matches[1])
        return target

    def falseThrowMonkey(self):
        falseActionStr = self.falseActionStr()
        matches = re.search("If false: throw to monkey (\d+)", falseActionStr)
        if matches is None:
            raise Exception("Cannot find the monkey to throw from falseActionStr: {}".format(falseActionStr))
        target = int(matches[1])
        return target

if __name__ == "__main__":
    inputFile = open("input.txt", "r")
    try:
        monkeys = []
        monkey = None
        lines = inputFile.readlines()
        for line in lines:
            trimmedLine = line.strip()
            if trimmedLine.startswith(Monkey.NUM_PREFIX):
                tokens = trimmedLine.split()
                monkeyNum = int(tokens[1][:-1])
                monkey = Monkey(monkeyNum)
                monkeys.append(monkey)
            elif trimmedLine.startswith(Monkey.STARTING_ITEMS_PREFIX):
                itemsTokens = trimmedLine[len(Monkey.STARTING_ITEMS_PREFIX):].split(",")
                for itemToken in itemsTokens:
                    monkey.appendItem(int(itemToken))
            elif trimmedLine.startswith(Monkey.OPERATION_PREFIX):
                monkey._operationStr = trimmedLine
            elif trimmedLine.startswith(Monkey.TEST_PREFIX):
                monkey._testStr = trimmedLine
            elif trimmedLine.startswith(Monkey.TRUE_PREFIX):
                monkey._trueActionStr = trimmedLine
            elif trimmedLine.startswith(Monkey.FALSE_PREFIX):
                monkey._falseActionStr = trimmedLine

        for i in range(20):
            for monkey in monkeys:
                items = monkey.items()
                for j in range(len(items)):
                    item = items.pop(0)
                    item = int(monkey.operate(item) / 3)
                    if monkey.test(item):
                        target = monkey.trueThrowMonkey()
                    else:
                        target = monkey.falseThrowMonkey()
                    targetMonkey = monkeys[target]
                    targetMonkey.appendItem(item)

        monkeyBusinesses = []
        for monkey in monkeys:
            monkeyBusinesses.append(monkey.inspectTimes())
        monkeyBusinesses.sort(reverse=True)
        print(monkeyBusinesses[0] * monkeyBusinesses[1])
    finally:
        inputFile.close()