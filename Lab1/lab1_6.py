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
while precise < 100000:
    print(getAreaOfOral(10,8,initDotsNum * precise))
    precise = precise * 10

'''
# 6 椭圆面积

已知一个椭圆的长轴长为10，短轴长为8，请设计算法求这个椭圆的面积，并编程实现。

要求1：利用特卡罗算法进行模拟。

要求2：分别打印在不同点数（至少设置4个不同的点数）情况下面积的近似值

------
### 特卡罗算法
1.在矩形范围内产生一个随机点  
               
    random函数的应用  

2.在随机点的x上进行椭圆函数计算得到对应的y  
               
    pow之类的数学函数的应用  

3.判断随机点的y在对应椭圆y的上面还是下面来判定该随机点是落在椭圆内还是椭圆外（且在矩形内）。
4.用落在椭圆的点数/总点数 近似 椭圆面积/矩形面积  
5.计算矩形面积，乘上比例，得到近似椭圆面积  



 



'''
