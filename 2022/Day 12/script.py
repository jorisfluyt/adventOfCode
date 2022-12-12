from typing import List
import math
import string
alphabet = string.ascii_letters

class Position :
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def getNeighbours(self) :
        return [Position(self.x - 1, self.y), Position(self.x + 1, self.y), Position(self.x, self.y - 1), Position(self.x, self.y + 1)]

def findShortestPath(map: List[str], lowestElevationLevel: List[chr]) -> int:
    nodeSteps = [[math.inf for _ in range(0,len(map[row]))] for row in range(0,len(map))]
    letterPositions = [Position(i,j) for i in range(0,len(map)) for j in range(0,len(map[0])) if map[i][j] in lowestElevationLevel]
    for position in letterPositions :
        nodeSteps[position.x][position.y] = 0
    
    unvisited_nodes = [Position(row, column) for column in range(0, len(map[0])) for row in range(0, len(map))]
    while unvisited_nodes != [] :
        node = None
        for unvisited in unvisited_nodes :
            if node == None :
                node = unvisited
            elif nodeSteps[unvisited.x][unvisited.y] < nodeSteps[node.x][node.y] :
                node = unvisited

        if map[node.x][node.y] == 'E' :
            return nodeSteps[node.x][node.y]
        
        steps = nodeSteps[node.x][node.y]
        elevationLevel = getElevationLevel(map[node.x][node.y])
        for neighbour in node.getNeighbours() :
            if neighbour.x < 0 or neighbour.x > len(map) - 1 or neighbour.y < 0 or neighbour.y > len(map[0]) - 1 :
                continue
            nextElevationLevel = getElevationLevel(map[neighbour.x][neighbour.y])
            if nextElevationLevel - elevationLevel <= 1:
                nextPositionSteps = nodeSteps[neighbour.x][neighbour.y]
                if steps + 1 < nextPositionSteps :
                    nodeSteps[neighbour.x][neighbour.y] = steps + 1
        unvisited_nodes.remove(node)

def getElevationLevel(letter: chr) :
    if letter == 'E' :
        return alphabet.index('z')
    if letter == 'S' :
        return 0
    return alphabet.index(letter)

def parse(file: str) :
    input = open(file)
    map = input.readlines()
    for i in range(0,len(map)) :
        map[i] = map[i].strip()
    return map

def main() :
    map = parse('input.txt')
    print('The fewest steps required to move from your current position to the location that should get the best signal is {}'.format(findShortestPath(map, ['S'])))
    print('The fewest steps required to move from from any square with elevation \'a\' to the location that should get the best signal is {}'.format(findShortestPath(map, ['S', 'a'])))
main()