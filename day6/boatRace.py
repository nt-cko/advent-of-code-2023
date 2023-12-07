path = 'input.txt'


def parseRaceRecordsFromTextInput(lines):
    rows = []
    for line in lines:
        line = line.replace("\n", "")
        rows.append(list(map(lambda value: int(value), filter(lambda parsed: parsed.isdigit(), line.split(":")[1].split(" ")))))
    
    races = []
    for i, row in enumerate(rows[0]):
        races.append([rows[0][i], rows[1][i]])
    return races

def calculateWinningTimesToHoldForRace(race):
    time = race[0] 
    distance = race[1]
    winningTimesToHold = []
    for i in range(1, time, 1):
        timeLeft = time - i
        travelledDistance = timeLeft*i
        if(travelledDistance > distance):
            winningTimesToHold.append(i)
    return winningTimesToHold

def part1(lines):
    races = parseRaceRecordsFromTextInput(lines)
    waysToWin = 1
    for race in races:
        waysToWin = len(calculateWinningTimesToHoldForRace(race)) * waysToWin
    print("--- Part 1 ---")
    print(f'Product of all number of ways to win: {waysToWin}')

def parseRaceFromTextInput(lines):
    time = int(lines[0].split(":")[1].replace(" ", "").replace("\n", ""))
    distance = int(lines[1].split(":")[1].replace(" ", "").replace("\n", ""))
    return [time, distance]

def calculateAmountOfWinningTimesToHoldForRace(race):
    time = race[0] 
    distance = race[1]
    numberOfWinningTimes = 0
    for i in range(1, time, 1):
        timeLeft = time - i
        travelledDistance = timeLeft*i
        if(travelledDistance > distance):
            numberOfWinningTimes += 1
    return numberOfWinningTimes

def part2(lines):
    race = parseRaceFromTextInput(lines)
    print('--- Part 2 ---')
    print(f'Record time: {race[0]} - Record distance: {race[1]}')
    print(f'Number of winning times: {calculateAmountOfWinningTimesToHoldForRace(race)}')

with open(path) as fp:
    lines = fp.readlines()
    part2(lines)
