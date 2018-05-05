#compare insert() with append() on their runtime
import datetime

appList = []
insList = []

startTime = datetime.datetime.now()
for i in range(0,50001):
    appList.append(50000-i)
endTime = datetime.datetime.now()
print("append time:  " + str((endTime - startTime).microseconds) + "ms")

startTime = datetime.datetime.now()
for i in range(0,50001):
    insList.insert(0,i)
endTime = datetime.datetime.now()
print("insert time:  "+ str((endTime - startTime).microseconds) + "ms")

'''
4 效率比较 

Python中list类有insert()和append()两个成员函数。 

(1) 说明这两个成员函数的作用，联系与区别。 

(2) 试编写代码，分别利用这两个函数建立一个长度为50000的列表，列表元素为 

为50000~1。 

(3) 比较（2）中两者的运行效率，并用程序证明（提示：利用运行时间证明）

------
#insert 和 append 效率比较

Python中的list类有insert()和append()两个成员函数
说明这两个成员函数的作用，联系和区别：

* 作用：
      insert():是指在某个特定位置前面增加一个数据项
      append():在列表末尾增加一个数据项

* 联系：
      都是list的成员函数
      都是在list增加一个数据项

* 区别：
      insert():可以插在指定位置
      append():只能插在末尾
      运行时间效率：append更快
~                                                              
~                                                              
~                                                              
~ 
'''

