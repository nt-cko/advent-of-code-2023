path = 'testInput.txt'

maps = []

def getMapValues(mapAsText):
    mapOfValues = []
    for mapRow in mapAsText.split(':')[1].split('\n'):
        mapRowValues = []
        for value in mapRow.split(' '):
            mapRowValues.append(value)
        tmp = list(filter(lambda a: a.isdigit(), mapRowValues))
        mapOfValues.append(list(map(lambda digit: int(digit), tmp)))
    return mapOfValues

def part1(lines):
    mapsAsText = lines.split('\n\n')
    maps = []
    for mapAsText in mapsAsText:
        maps.append(getMapValues(mapAsText))
    source = maps[0][0]
    for map in maps[1::]:
        convertedRes = convert(source, map)
        source = convertedRes
    print(source)
        

def convert(source, map):
    dest = []
    source1 = source
    for row in map:
        if(row != []):
            hit = False
            dest_local = []
            destRangeStart = row[0]
            sourceRangeStart = row[1]
            rangeLength = row[2]
            for index, number in enumerate(source1):
                destMapping = number

                if(number >= sourceRangeStart and number < sourceRangeStart + rangeLength):
                    hit = True
                    numberDistanceToSourceStart = number - sourceRangeStart
                    destMapping = numberDistanceToSourceStart + destRangeStart  
                if(index == 1):
                    print("source start: " + str(sourceRangeStart))
                    print("dest start: " + str(destRangeStart))
                    print("range len: " + str(rangeLength))
                    
                    print("Number in: " + str(number) + " Number out " + str(destMapping))
                dest_local.append(destMapping)
                if(hit == True):
                    break
            source1 = dest_local
    dest = source1
    return dest

with open(path) as fp:
    lines = fp.read()
    part1(lines)
    
