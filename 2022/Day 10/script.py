def getSumOfSignalStrengths(file:str) -> int:
    X = 1
    numberOfCycles = 0
    strengthValue = 0

    input = open(file)
    for line in input.readlines() :
        numberOfCycles += 1
        strengthValue += getStrengthValue(X, numberOfCycles)
        if line == 'noop' : 
            continue

        signal = line.strip().split(' ')
        if signal[0] == 'addx' :
            numberOfCycles += 1
            strengthValue += getStrengthValue(X, numberOfCycles)
            X += int(signal[1])
    return strengthValue

def getStrengthValue(value: int, numberOfCycles: int) -> int :
    if numberOfCycles == 20 or (numberOfCycles - 20) % 40 == 0 :
        return value * numberOfCycles
    return 0

def showCrtScreen(file:str) -> None :
    sprite = 1
    numberOfCycles = 0
    crt = ['' for i in range(0,6)]

    input = open(file)
    for line in input.readlines() :
        numberOfCycles += 1
        updateCrt(crt, sprite, numberOfCycles)
        if line == 'noop' : 
            continue
        
        signal = line.strip().split(' ')
        if signal[0] == 'addx' :
            numberOfCycles += 1
            updateCrt(crt, sprite, numberOfCycles)
            sprite += int(signal[1])

    for i in range(0,len(crt)) :
        print(crt[i])

def updateCrt(crt, sprite, position) :
    row = int((position-1) / 40)
    column = position % 40
    crt[row] += '#' if sprite <= column and sprite + 2 >= column else '.'

def main() :
    print('The sum of the signal strengths is {}'.format(getSumOfSignalStrengths('input.txt')))
    print()
    print('The output of the CRT screen : ')
    showCrtScreen('input.txt')

main()
