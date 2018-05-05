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
    copyDigits.sort(reverse = True)
    discDigits = copyDigits
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


secretNum = 6174
for i in range(0,5):
    rand = randint(1000,10000)
    print(str(rand),end=': ')
    minus = rand
    while minus != secretNum:
        minus = getMinus(minus)
        print(str(minus),end = ' ')
    print('!!!!') 
    
'''
# 5 神秘的数
任意一个４位自然数，将组成该数的各位数字重新排列，形成一个最大数和一个最小数，之后两数相减，其差仍为一个自然数。重复进行上述运算，你会发现一个神秘的数。
要求：
（1）编程来找到这个神秘的数。
（2）随机生成5个4位自然数，打印中间结果并验证结论。

------
####  如何求“最大最小差”  
1.把每个数字转换成一个字符串  
2.将字符串的每一个字符提出来，按原来顺序存入一个list里  
3.用list[:]生成一个拷贝列表（注意不能单纯将源列表赋值给一个新的列表），将原列表和拷贝列表分别做降序升序排序后重组乘字符串，转化为int,后相减  


重复做差过程，发现经过数次之后一定会等于神秘数6174，并且再次操作差不会再变  


'''
