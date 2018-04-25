import numpy as np
import matplotlib.pyplot as plt 
import random
from pylab import *
def getDigits(num):
    post1 = int(num%10)
    post2 = int((num%100 - post1)/10)
    post3 = int((num%1000 - num%100)/100)
    post4 = int((num%10000 - num%1000)/1000)
    return [post4,post3,post2,post1]

def getMinus(num):
    digits = getDigits(num)
    copyDigits = digits[:]
    digits.sort()
    ascDigits = digits
#    print(ascDigits)
    copyDigits.sort(reverse = True)
    discDigits = copyDigits
#    print(discDigits)
    max = discDigits[0]*1000 + discDigits[1]*100 + discDigits[2]*10 + discDigits[3]
#    print(max)
    min = ascDigits[0]*1000 + ascDigits[1]*100 + ascDigits[2]*10 + ascDigits[3]
#    print(min)
    minus = max - min
    return minus


bag = {}
for num in range(1000,10000):
    minus = getMinus(num)
    if minus not in bag.keys():
        bag[minus] = 0
    else:
        bag[minus] = bag[minus] + 1
print(bag)        

for i in range(0,5):
    rand = random.randint(1000,9999)
    print(getMinus(rand))

