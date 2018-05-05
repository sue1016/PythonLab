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
print("can both be divided by 2 and 3: ",end="")
for item in filtered:
        print(item,end=' ')
        filteredList.append(item)        

sum = reduce(lambda x,y: x+y,filteredList)

print('') 
print("The sum of them is:",end=" ")
print(str(sum))

'''
# 2.请实现满足以下三项要求的程序。  

#### (1) 随机生成20个[0, 200]范围内的整数，且每个数大小不同。 
* 用到了random.randint()函数  
值得注意的是这个函数的范围和range函数不同，是左闭右闭。（而range函数是左闭右开）
* 使用了一个列表来存储不同的随机数，列表中没有过的随机数放进去，把计数器加一，有过的不加进去，计数器不加，直到计数器到20。   

#### (2) 从这20个数中挑选出：奇数，且能够被3整除的数。 
* 注意到关键字挑选，虽然可以用遍历的方法来做，不过我决定练习新学的filter和lambda结合做挑选


#### (3) 给出（2）中挑选出来的数字的和。 
* 同样可以用reduce函数来做，我确定这不是最简单的方法，因为有求和函数sum(alist)，只是为了练习不熟的知识。  

'''
