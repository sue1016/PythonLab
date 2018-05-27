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
            print(self.__itemset)
        else:
            print("empty set")

    def getSet(self):
        return self.__itemset
set1 = Set([1,2,2,3])
set1.printAll()
set2 = Set([2,2,3,3,5])
set2.printAll()

print(set1.isMember(2))
print(set1.isMember(4))

set1.addElement(4)
set1.printAll()
set2.printAll()
print(set1.itersection(set2))
print(set1.union(set2))
print(set1.substract(set2))


set1.printAll()
set2.printAll()

