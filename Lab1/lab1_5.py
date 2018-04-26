import numpy as np
import matplotlib.pyplot as plt 
from random import randint
from pylab import *
def getDigits(num):
    strNum = str(num)
    digits = []
    for digit in strNum:
        digits.append(digit)     
    return digits

def getMinus(num):
    digits = getDigits(num)
    copyDigits = digits[:]
    digits.sort()
    ascDigits = digits
#    print(ascDigits)
    copyDigits.sort(reverse = True)
    discDigits = copyDigits
#    print(discDigits)
    max = ''
    min = ''
    for digit in discDigits:
        max = max + digit
    for digit in ascDigits:
        min = min + digit
    max = int(max)
    min = int(min)
    minus = max - min
    return minus
'''
bag = {}
minusList = []
x = np.arange(1000,10000,1)
for num in range(1000,10000):
    minus = getMinus(num)
    minusList.append(minus)
    if minus not in bag.keys():
        bag[minus] = 0
    else:
        bag[minus] = bag[minus] + 1
print(bag)   
minusList = np.array(minusList)
plt.rcParams['lines.color'] = 'r'
plt.hist(minusList,bins = range(1000,10000))
plt.title("minus")
plt.show()
'''
secretNum = 6174
for i in range(0,5):
    rand = randint(1000,10000)
    print(str(rand),end=': ')
    minus = rand
    while minus != secretNum:
        minus = getMinus(minus)
        print(str(minus),end = ' ')
    print('!!!!') 
    
        
