class Position :
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def getUniqueVisitedTailPositions(file:str, nbOfKnots: int) -> int :
    input = open(file)
    lines = input.readlines()
    knotPositions = [Position(0,0)] * nbOfKnots
    tailPositions = [Position(0,0)]
    for line in lines :
        move = line.strip().split()
        for _ in range(0, int(move[1])) :
            knotPositions[0] = moveKnot(move[0], knotPositions[0])
            for i in (range(1,len(knotPositions))) :
                if(isAdjacent(knotPositions[i-1], knotPositions[i])) :
                    break
                knotPositions[i] = moveRope(knotPositions[i-1], knotPositions[i])
                if (i == nbOfKnots - 1) :
                    tailPositions.append(knotPositions[i])
    return len(set(tailPositions))

def moveKnot(move:chr, position: Position) -> Position:
    if move == 'R' :
        return Position(position.x + 1, position.y)
    if move == 'L' :
        return Position(position.x - 1, position.y)
    if move == 'U' :
        return Position(position.x, position.y + 1)
    if move == 'D' :
        return Position(position.x, position.y - 1)

def moveRope(headPosition: Position, tailPosition: Position) -> Position: 
    diffX = headPosition.x - tailPosition.x
    if abs(diffX) == 2:
        if tailPosition.y > headPosition.y :
            return Position(tailPosition.x + int(diffX/2), tailPosition.y - 1)
        elif tailPosition.y < headPosition.y :
            return Position(tailPosition.x + int(diffX/2), tailPosition.y + 1)
        return Position(tailPosition.x + int(diffX/2), tailPosition.y)
    
    diffY = headPosition.y - tailPosition.y
    if abs(diffY) == 2:
        if tailPosition.x > headPosition.x :
            return Position(tailPosition.x - 1, tailPosition.y + int(diffY/2))
        elif tailPosition.x < headPosition.x :
            return Position(tailPosition.x + 1, tailPosition.y + int(diffY/2)) 
        return Position(tailPosition.x, tailPosition.y + int(diffY/2)) 

def isAdjacent(headPosition: Position, tailPosition: Position) -> bool:
    return abs(headPosition.x - tailPosition.x) <= 1 and abs(headPosition.y - tailPosition.y) <= 1

def main() :
    print('The tail of the rope with two knots visits {} unique positions'.format(getUniqueVisitedTailPositions('input.txt', 2)))
    print('The tail of the rope with ten knots visits {} unique positions'.format(getUniqueVisitedTailPositions('input.txt', 10)))

main()
