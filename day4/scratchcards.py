path = "input.txt"

def sumUpPointsOfAll(cards):
    sum = 0
    for card in cards:
        winningNumbers = getWinningNumbersOfCard(card)
        ownNumbers = getOwnNumbersOfCard(card)
        print(winningNumbers, ownNumbers)
        winners = list(filter(lambda number: ownNumbers.count(number) > 0, winningNumbers))
        print("winners:", winners)
        sum += calcPoints(len(winners))
    return sum

def calculateMatchesOfACard(card):
        winningNumbers = getWinningNumbersOfCard(card)
        ownNumbers = getOwnNumbersOfCard(card)
        winners = list(filter(lambda number: ownNumbers.count(number) > 0, winningNumbers))
        return len(winners)

def getWinningNumbersOfCard(card):
    numberContent = card.split("|")[0].split(":")[1].split(" ")
    numberContent = list(filter(lambda number: number != '', numberContent))
    numberContent = list(map(lambda number: int(number), numberContent))
    return numberContent


def getOwnNumbersOfCard(card):
    numberContent = card.split("|")[1].split(" ")
    numberContent = list(filter(lambda number: number != '', numberContent))
    numberContent = list(map(lambda number: int(number), numberContent))
    return numberContent

def calcPoints(matchCount):
    base = 0
    for i in range(0,matchCount):
        print(i)
        if(base == 0):
            base = 1
        else:
            base = base*2
    return base

def sumOfAllCards(cards):
    sumOfAllCopies = 0
    for index in range(len(cards)):
        print(index)
        sumOfAllCopies += calcSumOfAllCopies(cards, index) + 1
    return sumOfAllCopies

def calcSumOfAllCopies(cards, index):
    sumMatches = calculateMatchesOfACard(cards[index])
    for i in range(1, sumMatches+1):
        if(index+i <= len(cards)):
            sumMatches += calcSumOfAllCopies(cards, index+i)
    return sumMatches


with open(path) as fp:
    cards = fp.readlines()
    # print("--- Part 1 ---")
    # print("The sum of all points is: ", str(sumUpPointsOfAll(cards)))
    print("--- Part 2 ---")
    print("The sum of all copies won: ", sumOfAllCards(cards))
