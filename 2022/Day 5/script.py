import re
from typing import Callable

def rearrangeCrates(file:str, machine:Callable) -> str:
    input = open(file)
    lines = input.readlines()
    numberOfStacks = int(len(lines[0]) / 4)
    stacks = dict()
    for i in range(0,numberOfStacks) :
        stacks[i] = []
    
    parsingCrates = True
    for line in lines :
        if line == '\n' :
            parsingCrates = False
            continue
        if  parsingCrates :
            for i in range(0,numberOfStacks) :
                stack = line[4*i:4*i+3]
                match = re.search('\[(.*)\]',stack)
                if match != None :
                    stacks[i].append(match.group(1))
        else :
            match = re.search('move (.*) from (.*) to (.*)', line)
            nbOfCratesToMove = int(match.group(1))
            fromStackPos = int(match.group(2))-1
            toStackPos = int(match.group(3))-1
            machine(stacks,fromStackPos,toStackPos,nbOfCratesToMove)
    return "".join([stacks[i][0] for i in range(0,numberOfStacks)])

def useCrateMover9000(stacks:dict, fromStackPos:int, toStackPos:int, nbOfCrates: int ) -> None :
    fromStack = stacks[fromStackPos]
    toStack = stacks[toStackPos]
    cratesToMove = fromStack[0:nbOfCrates]
    cratesToMove.reverse()
    stacks[fromStackPos] = fromStack[nbOfCrates:]
    stacks[toStackPos] = cratesToMove + toStack

def useCrateMover9001(stacks:dict, fromStackPos:int, toStackPos:int, nbOfCrates: int ) -> None :
    fromStack = stacks[fromStackPos]
    toStack = stacks[toStackPos]
    cratesToMove = fromStack[0:nbOfCrates]
    stacks[fromStackPos] = fromStack[nbOfCrates:]
    stacks[toStackPos] = cratesToMove + toStack
    
print('The crates that end up on top of each stack using CrateMover9000 is {}'.format(rearrangeCrates('input.txt', useCrateMover9000)))
print('The crates that end up on top of each stack using CrateMover9001 is {}'.format(rearrangeCrates('input.txt', useCrateMover9001)))
