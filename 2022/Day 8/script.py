from typing import List

def parse(file:str) -> List[List[int]] :
    input = open(file)
    lines = input.readlines()
    return [[int(t) for t in line.strip()] for line in lines]

def numberOfVisibleTrees(grid: List[List[int]]) -> int :
    return sum(1 for column in range(0,len(grid[0])) for row in range(0,len(grid)) if isVisibleTree(grid, row, column))

def isVisibleTree(grid:List[List[int]], row:int, column:int) -> int :
    # All of the trees around the edge of the grid are visible
    if row == 0 or row == len(grid) - 1:
        return True
    if column == 0 or column == len(grid) - 1:
        return True
 
    value = grid[row][column]
    leftVisible = [t for t in grid[row][0:column] if t >= value] == []
    rightVisible = [t for t in grid[row][column+1:len(grid[row])] if t >= value] == []   
    topVisible = [r[column] for r in grid[0:row] if r[column] >= value] == []
    bottomVisible = [t[column] for t in grid[row+1:len(grid)] if t[column] >= value] == []
    return leftVisible or rightVisible or topVisible or bottomVisible

def getHighestScenicScore(grid: List[List[int]]) -> int :
    return max([getScenicScore(grid,i,j) for j in range(0,len(grid[0])) for i in range(0,len(grid))])

def getScenicScore(grid: List[List[int]], row:int, column:int) :
    value = grid[row][column]
    left = [t for t in grid[row][0:column]]
    right = [t for t in grid[row][column+1:len(grid[row])]]
    top = [r[column] for r in grid[0:row]]
    bottom = [t[column] for t in grid[row+1:len(grid)]]
    left.reverse()
    top.reverse()
   
    leftCountr = getNbOfVisibleTrees(left, value)
    rightCountr = getNbOfVisibleTrees(right, value)
    topCountr = getNbOfVisibleTrees(top, value)
    bottomCountr = getNbOfVisibleTrees(bottom, value)
    return leftCountr * rightCountr * topCountr * bottomCountr

def getNbOfVisibleTrees(trees: List[int], threshold: int) -> int :
    bottomCountr = 0
    for i in range(0,len(trees)) :
        bottomCountr += 1
        if trees[i] >= threshold :
            break
    return bottomCountr

def main():
    grid = parse('input.txt')
    print('There are {} trees visible from outside the grid'.format(numberOfVisibleTrees(grid)))
    print('The highest scenic score possible for any tree is {}'.format(getHighestScenicScore(grid)))

main()
