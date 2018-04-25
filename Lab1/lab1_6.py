#oral area
import random

longAxis = 10
shortAxis = 8

def getAreaOfOral(longAxis,shortAxis,dotsNum):
    countAll = 0
    countIn = 0
    halfLongAxis = 0.5 * longAxis
    halfShortAxis = 0.5 * shortAxis
    while countAll < dotsNum:
        randomX = random.random() * halfLongAxis
        randomY = random.random() * halfShortAxis
        y = pow((1 - pow(randomX,2)/pow(halfLongAxis,2)) * pow(halfShortAxis,2),0.5)
        if randomY < y:
            countIn = countIn + 1
        countAll = countAll + 1
    squareArea = halfLongAxis * halfShortAxis
    oralRatio = countIn / countAll
    oralArea = (squareArea * oralRatio) * 4
    return oralArea

precise = 1
initDotsNum = 1000
while precise < 100000000:
    print(getAreaOfOral(10,8,initDotsNum * precise))
    precise = precise * 10
