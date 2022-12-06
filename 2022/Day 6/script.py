def getLastCharPositionStartOfPacketMarker(file:str, nbOfCharSequence:int) -> int :
    input = open(file)
    line = input.readlines()[0]
    nbOfChars = len(line.strip())
    position = 0
    while(position + nbOfCharSequence < nbOfChars) :
        possibleStartOfPacketMarker = line[position:position+nbOfCharSequence]
        if(len(set(possibleStartOfPacketMarker)) == nbOfCharSequence) :
            return position + nbOfCharSequence
        else :
            position += 1

print('It took {} characters to be processed before the first 4 char start-of-packet marker is detected'.format(getLastCharPositionStartOfPacketMarker('input.txt',4)))
print('It took {} characters to be processed before the first 4 char start-of-packet marker is detected'.format(getLastCharPositionStartOfPacketMarker('input.txt',14)))
