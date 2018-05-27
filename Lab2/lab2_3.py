class Set:

    def __init__(self,alist):
         self.__itemset = set(alist)

    def addElement(self,x):
        self.__itemset.add(x)

    def deleteElement(self,x):
        self.__itemset.remove(x)

    def isMember(self,x):
        if x in self.__itemset:
            return True
        else:
            return False

    def itersection(self,set2):
        return self.__itemset.intersection(set2.getSet())

    def union(self,set2):
        return self.__itemset.union(set2.getSet())

    def substract(self,set2):
        return self.__itemset.difference(set2.getSet())

    def printAll(self):
        if(len(self.__itemset) > 0):
            print("输出集合："+str(self.__itemset))
        else:
            print("输出集合：空集")

    def getSet(self):
        return self.__itemset
set1 = Set([1,2,2,3])
print("集合1")
set1.printAll()
print("集合2")
set2 = Set([2,2,3,3,5])
set2.printAll()

print("2在集合1中吗")
print(set1.isMember(2))
print("4在集合1中吗") 
print(set1.isMember(4))

print("向集合1中加入4")
set1.addElement(4)
print("集合1")
set1.printAll()
print("集合2")
set2.printAll()
print("集合1交集合2")
print(set1.itersection(set2))
print("集合1并集合2")
print(set1.union(set2))
print("集合1减集合2")
print(set1.substract(set2))


'''
使用python的set数据结构实现set类  
构造函数可传入list对象，可能包含重复元素，使用set(list)将list转换成不重复无序的set对象  
使用set.add(),set.remove()实现在集合中添加删除元素  
使用if x in set:实现判断是否是集合中的元素  
使用set.intersection(set),union(set),difference(set)实现交并差  

'''
