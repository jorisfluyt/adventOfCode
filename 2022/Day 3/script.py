import math
import string

alphabet = string.ascii_letters
def getCommonItemPrioritySum(file: str) :
    input = open(file)
    lines = input.readlines()
    priorityScore = 0
    for line in lines :
        splitForCompartiment = int(len(line) / 2)
        itemsFirstCompartiment = line[:splitForCompartiment]
        itemsSecondCompartiment = line[splitForCompartiment:].replace('\n','')
        duplicateItem = list(set(itemsFirstCompartiment).intersection(itemsSecondCompartiment))[0]
        priorityScore += alphabet.index(duplicateItem) + 1
    return priorityScore
          

def getBadgesPrioritySum(file: str) :
    input = open(file)
    lines = input.readlines()
    numberOfGroups = int(len(lines) / 3)
    priorityScore = 0
    for i in range(0,numberOfGroups) :
        group = lines[3*i:3*i+3]
        duplicateItem = list(set(group[0].replace('\n','')).intersection(group[1].replace('\n','')).intersection(group[2].replace('\n','')))[0]
        priorityScore += alphabet.index(duplicateItem) + 1
    return priorityScore

def main():
    sumPriorityItems = getCommonItemPrioritySum('input.txt')
    sumBadgesPriority = getBadgesPrioritySum('input.txt')
    print("The sum of priorities of the item types that appears in both compartmentsg is {}".format(sumPriorityItems))
    print("The sum of priorities of the item types that corresponds to the badges is {}".format(sumBadgesPriority))

if __name__ == "__main__" :
    main()
    