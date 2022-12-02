def playRockPaperScissors(input: str) :
    input = open(input, 'r')
    lines = input.readlines()
    score = 0
    elfScore = 0
    for line in lines :
        moves = line.split()
        move = moves[1]
        opponentMove = moves[0]
        moveToPlay = moveForOutcome(moves[1], opponentMove)
        score += outcome(move, opponentMove) + getScoreForMove(move)
        elfScore += outcome(moveToPlay, opponentMove) + getScoreForMove(moveToPlay)
    return {score, elfScore}

def moveForOutcome(outcome: str, opponentMove: str) :
    possibleMoves = ['X', 'Y', 'Z']
    for move in possibleMoves :
        if outcome == 'Z' and isWin(move, opponentMove):
            return move
        if outcome == 'Y' and isDraw(move, opponentMove):
            return move
        if outcome == 'X' and not(isWin(move, opponentMove)) and not(isDraw(move, opponentMove)):
            return move
        
def outcome(move: str, opponentMove: str) :
    if isWin(move, opponentMove) :
        return 6
    if isDraw(move, opponentMove) :
        return 3
    return 0

def isWin(move: str, opponentMove: str) :
    if move == 'X' and opponentMove == 'C' :
        return True
    if move == 'Y' and opponentMove == 'A' :
        return True
    if move == 'Z' and opponentMove == 'B' :
        return True
    return False

def isDraw(move:str, opponentMove: str) :
    if move == 'X' and opponentMove == 'A' :
        return True
    if move == 'Y' and opponentMove == 'B' :
        return True
    if move == 'Z' and opponentMove == 'C' :
        return True
    return False

def getScoreForMove(move: str):
    if move == 'X' :
        return 1
    if move == 'Y' :
        return 2
    if move == 'Z' :
        return 3
    return 0

def main() :
    score, elfScore = playRockPaperScissors('input.txt')
    print("Sum of the scores according to your strategy is {}".format(score))
    print("Sum of the scores according to the Elf's strategy is {}".format(elfScore))
    
if __name__ == "__main__":
    main()
