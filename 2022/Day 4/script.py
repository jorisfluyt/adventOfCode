def getAssignmentsThatFullyOverlap(file:str) -> int :
    input = open(file)
    lines = input.readlines()
    count = 0
    for line in lines :
        elves = line.strip().split(',')
        elf1Tasks = elves[0].split('-')
        elf1Sections = range(int(elf1Tasks[0]), int(elf1Tasks[1])+1)
        elf2Tasks = elves[1].split('-')
        elf2Sections = range(int(elf2Tasks[0]), int(elf2Tasks[1])+1)
        if ((set(elf1Sections) - set(elf2Sections) == set() or set(elf2Sections) - set(elf1Sections) == set())) :
            count += 1
    return count
        
def getAssignmentsThatOverlap(file:str) -> int :
    input = open(file)
    lines = input.readlines()
    count = 0
    for line in lines :
        elves = line.strip().split(',')
        elf1Tasks = elves[0].split('-')
        elf1Sections = range(int(elf1Tasks[0]), int(elf1Tasks[1])+1)
        elf2Tasks = elves[1].split('-')
        elf2Sections = range(int(elf2Tasks[0]), int(elf2Tasks[1])+1)
        if ((set(elf1Sections) - set(elf2Sections) != set(elf1Sections) and set(elf2Sections) - set(elf1Sections) != set(elf2Sections))) :
            count += 1
    return count

print('The number of assignments where the sections fully overlap with the other is {}'.format(getAssignmentsThatFullyOverlap('input.txt')))
print('The number of assignments where the sections overlap with the other is {}'.format(getAssignmentsThatOverlap('input.txt')))