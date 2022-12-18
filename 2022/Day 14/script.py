from typing import Tuple

class Point :
    def __init__(self, x: int, y: int) -> None:
        self.x = x 
        self.y = y

    def __eq__(self, other: "Point") -> bool:
        if other == None :
            return False
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

def parse(file: str) -> Tuple[dict, int] :
    input = open(file)
    mapPositions = dict()
    lowestRockPosition = 0
    for line in input.readlines() :
        rockPositions = line.split('->')
        currentPosition = None
        for position in rockPositions :
            coordinates = position.strip().split(',')
            point = Point(int(coordinates[0]), int(coordinates[1]))
            mapPositions[point] = '#'
            if point.y > lowestRockPosition :
                lowestRockPosition = point.y
            if currentPosition != None :
                if point.x == currentPosition.x :
                    yDiff = point.y - currentPosition.y
                    pointsRange = range(yDiff, 0) if yDiff < 0 else range(0, yDiff)
                    for i in pointsRange :
                        mapPositions[Point(currentPosition.x, currentPosition.y + i)] = '#'
                else :
                    xDiff = point.x -  currentPosition.x
                    pointsRange = range(xDiff, 0) if xDiff < 0 else range(0, xDiff)
                    for i in pointsRange :
                        mapPositions[Point(currentPosition.x + i, currentPosition.y )] = '#'
            currentPosition = point
    return mapPositions, lowestRockPosition

def iterationsToFlowInAbyss(mapPositions: dict, lowestRockPosition: int) -> int :
    numberOfIterations = 0
    while(True) :
        sandPoint = Point(500,0)
        hasReachedFloor = False
        while(not hasReachedFloor) :
            if sandPoint.y + 1 > lowestRockPosition :
                return numberOfIterations

            nextSandPoint = Point(sandPoint.x, sandPoint.y + 1)
            if nextSandPoint in mapPositions :
                if not Point(nextSandPoint.x - 1, nextSandPoint.y) in mapPositions :
                    nextSandPoint = Point(nextSandPoint.x - 1, nextSandPoint.y)
                elif not Point(nextSandPoint.x + 1, nextSandPoint.y) in mapPositions :
                    nextSandPoint = Point(nextSandPoint.x + 1, nextSandPoint.y)
                else :
                    mapPositions[sandPoint] = 'O'
                    hasReachedFloor = True
            sandPoint = nextSandPoint
        numberOfIterations += 1

def iterationsTillSandRests(mapPositions: dict, lowestRockPosition: int) -> int :
    numberOfIterations = 0
    while(True) :
        sandPoint = Point(500,0)
        hasReachedFloor = False
        while(not hasReachedFloor) :
            if sandPoint.y == lowestRockPosition + 1 :
                mapPositions[sandPoint] = 'O'
                hasReachedFloor = True
                
            nextSandPoint = Point(sandPoint.x, sandPoint.y + 1)
            if nextSandPoint in mapPositions :
                if not Point(nextSandPoint.x - 1, nextSandPoint.y) in mapPositions :
                    nextSandPoint = Point(nextSandPoint.x - 1, nextSandPoint.y)
                elif not Point(nextSandPoint.x + 1, nextSandPoint.y) in mapPositions :
                    nextSandPoint = Point(nextSandPoint.x + 1, nextSandPoint.y)
                else :
                    if sandPoint == Point(500,0) :
                        return numberOfIterations + 1
                    mapPositions[sandPoint] = 'O'
                    hasReachedFloor = True
            sandPoint = nextSandPoint
        numberOfIterations += 1

def main() :
    mapPositions, lowestRockPosition = parse('input.txt')
    nbOfiterationsToFlowInAbyss = iterationsToFlowInAbyss(mapPositions, lowestRockPosition)
    nbOfiterationsTillSandRests = iterationsTillSandRests(mapPositions, lowestRockPosition)
    print('It takes {} units of sand come to rest before sand starts flowing into the abyss below'.format(nbOfiterationsToFlowInAbyss))
    print('It takes {} units of sand come to rest'.format(nbOfiterationsTillSandRests))
