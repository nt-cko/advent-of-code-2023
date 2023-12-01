path = 'input.txt'

stringNumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

input = open(path)

def findFirstDigitCharacterOccurence(string):
    for index, character in enumerate(string):
        if character.isnumeric():
            return [index, int(character)]
    return 0
        
def findLastDigitCharacterOccurence(string):
    reversedString = string[::-1]
    for index, character in enumerate(reversedString):
        if character.isnumeric():
            return [len(reversedString) - 1  - index, int(character)]
    return 0

def findFirstAndLastStringOccurence(string):
    lowestIndex = len(string) + 1
    lowestNumber = ""
    highestIndex = -1
    highestNumber = ""
    for stringNumber in stringNumbers:
        firstIndex = string.find(stringNumber)
        lastIndex = string.rfind(stringNumber)
        if(firstIndex == -1): continue
        if(firstIndex < lowestIndex):
            lowestIndex = firstIndex
            lowestNumber = stringNumber
        if(lastIndex > highestIndex):
            highestIndex = lastIndex
            highestNumber = stringNumber
    if(lowestNumber != ""):
        lowestNumber = stringNumbers.index(lowestNumber) + 1
        highestNumber = stringNumbers.index(highestNumber) + 1 
        return [[lowestIndex, lowestNumber], [highestIndex, highestNumber]]
    return [[-1,-1], [-1,-1]]
    

def findDigits(string):
    firstStringOccurence, lastStringOccurence = findFirstAndLastStringOccurence(string)
    firstDigitOccurence = findFirstDigitCharacterOccurence(string)
    lastDigitOccurence = findLastDigitCharacterOccurence(string)
    firstNumber = 0

    print("string" , firstStringOccurence, "digit", firstDigitOccurence)
    if(firstStringOccurence[0] == -1 or firstStringOccurence[0] > firstDigitOccurence[0]):
        firstNumber = firstDigitOccurence[1]
    else:
        firstNumber = firstStringOccurence[1]
    lastNumber = 0
    print("string", lastStringOccurence, "digit", lastDigitOccurence)
    if(lastStringOccurence[0] == -1 or lastStringOccurence[0] < lastDigitOccurence[0]):
        lastNumber = lastDigitOccurence[1]
    else:
        lastNumber = lastStringOccurence[1]
        

    return firstNumber, lastNumber
    
sum = 0
for line in input:
    firstNumber, lastNumber = findDigits(line)
    print(line)
    print(firstNumber, lastNumber)
    value = int(str(firstNumber) + str(lastNumber))
    sum += value
        

print(sum)

input.close()