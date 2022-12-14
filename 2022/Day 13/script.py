import functools
from typing import List, Union

def parse(file: str) -> List :
    pairs = []
    input = open(file)
    for line in input.readlines():
        if line != "\n":
            pairs.append(eval(line))
    return pairs

def getSumIndexesOfIncorrectPairs(pairs: List) -> int :
    sumOfIndexes = 0
    index = 1
    for i in range(0, len(pairs), 2):
        if isValid(pairs[i], pairs[i+1]) > 0 :
            sumOfIndexes += index
        index += 1
    return sumOfIndexes

def isValid(packetOne: Union[List, int], packetTwo: Union[List,int]) -> int :
    if isinstance(packetOne, int) and isinstance(packetTwo, int) :
        return packetTwo - packetOne
    if isinstance(packetTwo, int) :
        return isValid(packetOne, [packetTwo])
    if isinstance(packetOne, int) and isinstance(packetTwo, list) :
        return isValid([packetOne], packetTwo)
    for pair in zip(packetOne, packetTwo): 
        valid = isValid(*pair)
        if valid != 0 :
            return valid
    return len(packetTwo) - len(packetOne)
 
def getDecoderKey(pairs: List) -> int :
    pairs.append([[2]])
    pairs.append([[6]])
    pairs.sort(key=functools.cmp_to_key(isValid), reverse=True)
    return (pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1)

def main() -> None :
    pairs = parse('input.txt')
    print('The sum of the indices of the pairs that are in he right order is {}'.format(getSumIndexesOfIncorrectPairs(pairs)))
    print('The decoder key for the distress signal is {}'.format(getDecoderKey(pairs)))

main()
