import random
import sys
from functools import reduce
#random lab

count = 0
diRandList = []
filteredList = []
while count < 20:
    rand = random.randint(0,200)
    if(rand not in diRandList):
        diRandList.append(rand)
        count = count + 1

print(diRandList)    

filtered = filter(lambda x: x%2==0 and x%3==0,diRandList)
for item in filtered:
        print(item,end=' ')
        filteredList.append(item)        

sum = reduce(lambda x,y: x+y,filteredList)

print('')    
print(str(sum))


