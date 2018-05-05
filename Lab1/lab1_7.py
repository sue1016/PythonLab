#red packet

import random
def sendPockets(total,patiNum):
    patitions = [1]*patiNum
    count = 0
    while count < total - patiNum:
        nextPocketToAdd = random.randint(0,patiNum - 1)              
        patitions[nextPocketToAdd] = patitions[nextPocketToAdd] + 1
        count = count + 1
    return patitions    
        
total = input("Input the total money you wanna give out: ")
patiNum = input("Input the patitions you wanna divide the money into:")
count = 0
while count < 10:
    print(sendPockets(int(total),int(patiNum)))
    count = count + 1

'''
# 7 微信红包

设计函数实现微信发红包的功能。

要求：

（1）输入：拟发红包的总额，拟派发的人数。

（2）输出：列表形式的派发方案。派发方案是随机的，要求给出10次模拟的结果。

（3）总额与每人得到的金额皆为整数。

（4）任何人不能得到0元的红包。

例：总额20元，派发人数：5

某次随机模拟的结果为：[3, 7, 8, 1, 1]

------
1.拟派发的人有多少就产生一个列表，长度等于派发人数，并把每一个都初始化为1（ 以保证任何人不会拿到0元红包）  
2.计数，随机投放 总金额 - 拟派发人数 次，每次投放一元（以保证每个人得到的金额结尾整数），投放时随机在list中找一个位置加一元（保证派发方案随机）
'''
