from sortedcontainers import SortedList

def getCalories(input: str):
    caloriesPerElf = SortedList()
    calories = 0

    input = open(input, 'r')
    lines = input.readlines()
    for line in lines :
        if line == '\n' :
            caloriesPerElf.add(calories)
            calories = 0
        else :
            calories += int(line)
    return caloriesPerElf

def getCaloriesOfTop(caloriesPerElf: SortedList, top: int):
    calories = 0
    for x in range(1,top+1) :
        calories += caloriesPerElf[len(caloriesPerElf) - x]
    return calories

def main() :
    caloriesPerElf = getCalories('input.txt')
    print('Highest total calories carried by an Elf is {}'.format(getCaloriesOfTop(caloriesPerElf, 1)))
    print('Sum of the top 3 total calories carried by the Elves is {}'.format(getCaloriesOfTop(caloriesPerElf, 3)))

if __name__ == "__main__":
    main()
