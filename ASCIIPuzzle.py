firstRow =                      '   _( )__'   
secondRow =                     ' _|     _|'
thirdRow =                      '(_   _ (_'
fourthRow =                     ' |__( )_|'

firstRowWithoutLeft =           ' _( )__'
secondRowdWithoutLeft =         '     _|'
thirdRowWithoutLeft =           '   _ (_'
fourthRowWithoutLeft =          '__( )_|' 

firstMirrorRow =                '  __( )_'
secondMirrorRow =               ' |_     |_'
thirdMirrorRow =                '  _) _   _)'
fourthMirrorRow =               ' |__( )_|'

firstMirrorRowWithoutLeft =     ' __( )_'
secondMirrorRowdWithoutLeft =   '     |_'
thirdMirrorRowWithoutLeft =     ' _   _)'
fourthMirrorRowWithoutLeft =    '__( )_|'

elements = [firstRow, secondRow, thirdRow, fourthRow]
elementsWithoutLeft = [firstRowWithoutLeft, secondRowdWithoutLeft, thirdRowWithoutLeft, fourthRowWithoutLeft]
mirrorElements = [firstMirrorRow, secondMirrorRow, thirdMirrorRow, fourthMirrorRow]
mirrorElementsWithoutLeft = [firstMirrorRowWithoutLeft, secondMirrorRowdWithoutLeft, thirdMirrorRowWithoutLeft, fourthMirrorRowWithoutLeft]

def printRow(elements, elementsWithoutLeft, count):
    result = []
    for element in range(len(elements)):
        i = 0
        while i < count:
            if (i == 0):
                result.append(elements[element])
            else:
                result.append(elementsWithoutLeft[element])
            i += 1
        result.append('\n')
    return result  

def puzzle_tiles(width, height):
    result = []
    i = 1
    while i <= height:
        if (i % 2 == 0):
            result.extend(printRow(mirrorElements[1:], mirrorElementsWithoutLeft[1:], width))       
        elif (i == 1):
            result.extend(printRow(elements, elementsWithoutLeft, width))
        else:
            result.extend(printRow(elements[1:], elementsWithoutLeft[1:], width))
        if (i == height):
            result.pop()
        i += 1
    stringResult = ''.join(result)
    print(stringResult)
    return stringResult
puzzle_tiles(6,4)