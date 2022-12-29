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
        self.__num = num
        self.__items = []
        self.__operationStr = ""
        self.__testStr = ""
        self.__trueActionStr = ""
        self.__falseActionStr = ""
        self.__inspectTimes = 0
        self.__operator = ""
        self.__operand = ""
        self.__divisor = 0
        self.__trueTarget = -1
        self.__falseTarget = -1

    @property
    def num(self):
        return self.__num

    @property
    def items(self):
        return self.__items

    @property
    def operationStr(self):
        return self.__operationStr

    @operationStr.setter
    def operationStr(self, value):
        if not isinstance(value, str):
            raise ValueError("value must be str type for operationStr")
        matches = re.search("Operation: new = old (.) (.*)", value)
        if matches is None:
            raise Exception("Cannot find operator and operand from operation string: {}".format(value))
        self.__operationStr = value
        self.__operator = matches[1]
        self.__operand = matches[2]

    @property
    def testStr(self):
        return self.__testStr

    @testStr.setter
    def testStr(self, value):
        matches = re.search("Test: divisible by (\d+)", value)
        if matches is None:
            raise Exception("Cannot find divisor from test string: {}".format(value))
        self.__testStr = value
        self.__divisor = int(matches[1])

    @property
    def trueActionStr(self):
        return self.__trueActionStr

    @trueActionStr.setter
    def trueActionStr(self, value):
        if not isinstance(value, str):
            raise ValueError("value must be str type for trueActionStr")
        matches = re.search("If true: throw to monkey (\d+)", value)
        if matches is None:
            raise Exception("Cannot find the monkey to throw from trueActionStr: {}".format(value))
        self.__trueActionStr = value
        self.__trueTarget = int(matches[1])

    @property
    def falseActionStr(self):
        return self.__falseActionStr

    @falseActionStr.setter
    def falseActionStr(self, value):
        if not isinstance(value, str):
            raise ValueError("value must be str type for falseActionStr")
        matches = re.search("If false: throw to monkey (\d+)", value)
        if matches is None:
            raise Exception("Cannot find the monkey to throw from falseActionStr: {}".format(value))
        self.__falseActionStr = value
        self.__falseTarget = int(matches[1])

    @property
    def inspectTimes(self):
        return self.__inspectTimes

    @inspectTimes.setter
    def inspectTimes(self, value):
        if not isinstance(value, int):
            raise ValueError("value must be int type for inspectTimes")
        self.__inspectTimes = value

    @property
    def trueTarget(self):
        return self.__trueTarget

    @property
    def falseTarget(self):
        return self.__falseTarget

    def operate(self, item):
        if not isinstance(item, int):
            raise ValueError("item must be int type")
        result = item
        if self.__operator == "+":
            if self.__operand == self.OLD_OPERAND:
                result += item
            else:
                result += int(self.__operand)
        elif self.__operator == "*":
            if self.__operand == self.OLD_OPERAND:
                result *= item
            else:
                result *= int(self.__operand)
        else:
            raise Exception("Unknown operator: {}".format(self.__operator))
        return result

    def test(self, item):
        if not isinstance(item, int):
            raise ValueError("item must be int type")
        self.__inspectTimes += 1
        return (item % self.__divisor) == 0

if __name__ == "__main__":
    overlapPairsCount = 0
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
                    monkey.items.append(int(itemToken))
            elif trimmedLine.startswith(Monkey.OPERATION_PREFIX):
                monkey.operationStr = trimmedLine
            elif trimmedLine.startswith(Monkey.TEST_PREFIX):
                monkey.testStr = trimmedLine
            elif trimmedLine.startswith(Monkey.TRUE_PREFIX):
                monkey.trueActionStr = trimmedLine
            elif trimmedLine.startswith(Monkey.FALSE_PREFIX):
                monkey.falseActionStr = trimmedLine

        for i in range(20):
            print("round {}".format(i+1))
            for monkey in monkeys:
                items = monkey.items
                for j in range(len(items)):
                    item = items.pop(0)
                    item = monkey.operate(item)
                    if monkey.test(item):
                        target = monkey.trueTarget
                    else:
                        target = monkey.falseTarget
                    targetMonkey = monkeys[target]
                    targetMonkey.items.append(item)

        monkeyInspectTimes = []
        for monkey in monkeys:
            monkeyInspectTimes.append(monkey.inspectTimes)
        monkeyInspectTimes.sort(reverse=True)
        monkeyBusiness = monkeyInspectTimes[0] * monkeyInspectTimes[1]
        print(monkeyBusiness)
    finally:
        inputFile.close()