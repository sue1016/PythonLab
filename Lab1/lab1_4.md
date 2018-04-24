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
