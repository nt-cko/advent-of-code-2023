# path = 'input.txt'
path = 'testInput.txt'

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
handImages = [[1,1,1,1,1], [1,1,1,2],[1,2,2],[1,1,3],[2,3],[1,4],[5]]
#            0 high card  - 1 one pair - 2 two pair - 3 three of a kind - 4 full house - 5 four of a kind - 6 five of a kind
def parseHandAndBidFromLine(line):
    values = line.split(" ")
    return [values[0],int(values[1].replace("\n", ""))]

def getValueOfHand(hand):
    foundCards = {}
    for card in list(hand[0]):
        if(card in foundCards):
            foundCards[card] += 1
        else:
            foundCards[card] = 1

    return getImageOrder(foundCards)

def getValueOfHandWithJoker(hand):
    foundCards = {}
    for card in list(hand[0]):
        if(card in foundCards):
            foundCards[card] += 1
        else:
            foundCards[card] = 1
    return getImageOrderWithJoker(foundCards)

def getImageOrder(countedHand):
    for index, handImage in enumerate(handImages):
        if(handImage == sorted(countedHand.values())):
            return index+1


# 0 high card  - 1 one pair - 2 two pair - 3 three of a kind - 4 full house - 5 four of a kind - 6 five of a kind
def getImageOrderWithJoker(countedHand):
    if('J' not in countedHand):
        for index, handImage in enumerate(handImages):
            if(handImage == sorted(countedHand.values())):
                return index+1
    else:
        print(countedHand)
        numberOfJokers = countedHand['J']
        countedHand.pop('J')
        sortedValues = dict(sorted(countedHand.items(), key=lambda card: card[1], reverse=True))
        mostOccurences = sortedValues[list(sortedValues)[0]] 
        secondMostOccurences = sortedValues[list(sortedValues)[1]] 
        if(mostOccurences == 1):
            # X of a kind
            x = 1+numberOfJokers
            return xOfAKindToValue(x)
        elif (mostOccurences == 2):
            if(secondMostOccurences == 2):
                # Full house
                return 4
            else:
                # X of a kind
                return xOfAKindToValue(2 + numberOfJokers)
        elif (mostOccurences == 3):
            return xOfAKindToValue(3 + numberOfJokers)
        else:
            return 6  

def xOfAKindToValue(x):
    if(x) == 2:
        return 1
    elif(x) == 3:
        return 3
    elif(x) == 4: 
        return 5
    elif(x) == 5:
        return 6

def sortHandsByRank(hands):
    indexedHands = {1:[], 2:[], 3:[], 4:[],5:[],6:[],7:[]}
    countedHands = list(map(lambda hand: getValueOfHand(hand), hands))
    for countedHand in countedHands:
        indexedHands[getImageOrder(countedHand[0])].append(countedHand)
    bidsInOrder = []
    for index in indexedHands:
        for ordered in sorted(indexedHands[index], key=lambda hand: (cards.index(list(hand[0].keys())[0]))):
            print(ordered)
            bidsInOrder.append(ordered[1])   
    # for index in indexedHands
    # return sortedHands

def handToNumber(hand):
    number = ""
    for card in hand:
        number += str(cards.index(card))
    return int(number)

def sortHands(hands):
    indexedHands = {1:[], 2:[], 3:[], 4:[],5:[],6:[],7:[]}
    for hand in hands:
        indexedHands[getValueOfHand(hand)].append(hand)
    print(indexedHands)
    winnings = 0
    rankctr = 1
    for index in indexedHands:
        for hand in sorted(indexedHands[index], key=lambda hand: (cards.index(hand[0][0]), cards.index(hand[0][1]), cards.index(hand[0][2]), cards.index(hand[0][3]), cards.index(hand[0][4])), reverse=True):
            print(hand[0])
            winnings += rankctr * hand[1]
            rankctr += 1
    print(f'Total winnings: {winnings}')

    # for index in indexedHands
    # return sortedHands



def sortHandsWithJoker(hands):
    indexedHands = {1:[], 2:[], 3:[], 4:[],5:[],6:[],7:[]}
    for hand in hands:
        indexedHands[getValueOfHandWithJoker(hand)].append(hand)
    for index in indexedHands:
        print(f'index: {index} indexedHands[index] = {indexedHands[index]}')
        print(sorted(indexedHands[index], key=lambda hand: (hand[0].count('J'), )))

def part1(lines):
    print("--- Part 1 ---")
    hands = []
    for line in lines:
        hands.append(parseHandAndBidFromLine(line))
    sortHands(hands)

def part2(lines):
    print("--- Part 1 ---")
    hands = []
    for line in lines:
        hands.append(parseHandAndBidFromLine(line))
    sortHandsWithJoker(hands)

with open(path) as fp:
    lines = fp.readlines()
    # part1(lines)
    part2(lines)

