import operator
import re
import math
import copy
from typing import List

ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, '**': operator.pow }

class Monkey :
    def __init__(self, name: int, startItems: List[int], operator: str, operatorValue: int, divisor: int, monkeyTestPassed: int, monkeyTestFailed: int) -> None:
        self.name = name
        self.items = startItems
        self.operator = operator
        self.operatorValue = operatorValue
        self.divisor = divisor
        self.monkeyTestPassed = monkeyTestPassed
        self.monkeyTestFailed = monkeyTestFailed
        self.inspectedItems = 0

    def inspectItem(self, item: int, optimizedRule: int) -> int:
        self.inspectedItems += 1
        value = int(self.operatorValue) if self.operatorValue != 'old' else item
        resultOperation = ops[self.operator](item, value)
        return resultOperation % optimizedRule if optimizedRule else int(resultOperation / 3)

    def throwsTo(self, value: int) -> int :
        return self.monkeyTestPassed if value % self.divisor == 0 else self.monkeyTestFailed

def parse(file: str) -> dict :
    name = 0
    items = []
    operator = None
    operatorValue = 0
    divisor = 0
    monkey1 = None
    monkey2 = None

    monkeys = dict()
    input = open(file)
    while True :
        line = input.readline()
        if not line :
            monkey = Monkey(name, items, operator, operatorValue, divisor, monkey1, monkey2)
            monkeys[monkey.name] = monkey
            break 
        if line == '\n' :
            monkey = Monkey(name, items, operator, operatorValue, divisor, monkey1, monkey2)
            monkeys[monkey.name] = monkey
        else :
            line = line.strip().split(':')
            property = line[0]
            if 'Monkey' in property :
                name = int(re.match('Monkey (.*)', line[0].strip()).group(1))
            if property == 'Starting items' :
                items = [int(i) for i in line[1].strip().split(',')]
            if property == 'Operation' :
                match = re.match('new = old (.) (.*)', line[1].strip())
                operator = match.group(1)
                operatorValue = match.group(2)
                operatorValue ==  int(operatorValue) if operatorValue != 'old' else operatorValue
            if property == "Test" :
                divisor = int(re.match('divisible by (.*)', line[1].strip()).group(1))
                trueCase = input.readline().strip()
                monkey1 = int(re.match('If true: throw to monkey (.*)', trueCase).group(1))
                falseCase = input.readline().strip()
                monkey2 = int(re.match('If false: throw to monkey (.*)', falseCase).group(1))
    return monkeys

def playKeepAway(monkeys: dict, rounds: int, optimizedRule: int) -> int :
    for _ in range(0, rounds) :
        for monkey in monkeys.values() :
            for item in monkey.items :
                rateAfterInspection = monkey.inspectItem(item, optimizedRule)
                throwsTo = monkey.throwsTo(rateAfterInspection)
                monkeys[throwsTo].items.append(rateAfterInspection)
            monkey.items = []

    inspectedItems = [i.inspectedItems for i in monkeys.values()]
    inspectedItems.sort()
    return math.prod(inspectedItems[-2:])

def main() -> None :
    monkeys = parse('input.txt')
    print('The level of monkey business after 20 rounds with worry levels is {}'.format(playKeepAway(copy.deepcopy(monkeys), 20, None)))
    
    lcm = math.prod([monkey.divisor for monkey in monkeys.values()]) 
    print('The level of monkey business after 10000 rounds without worry levels is {}'.format(playKeepAway(copy.deepcopy(monkeys), 10000, lcm)))

main()
