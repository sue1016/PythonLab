import random
import numpy as np
class SortLib:
    def __init__(self):
        pass
    def bubbleSort(self,seq):
        length = len(seq)
        for i in range(0,length):
            for j in range(i+1,length):
                if seq[i] > seq[j]:
                    seq[i],seq[j] = seq[j],seq[i]
        return seq            
    def quickSort(self,seq):
        return self.qSort(seq,0,len(seq)-1)

    def qSort(self,seq,left,right):
        if left >= right:
            return seq  
        key = seq[left]  
        low = left
        high = right 
        while left < right:
            while left < right and seq[right] >= key:
                right = right - 1
            seq[left] = seq[right]  
            while left < right and seq[left] <= key:
                left = left + 1
            seq[right] = seq[left]  
        seq[right] = key
        self.qSort(seq,low,left-1)
        self.qSort(seq,left+1,high)
        return seq
        

    def selectSort(self,seq):
        length = len(seq)
        for i in range(0,length):
           min = i
           for j in range(i+1,length):
               if seq[min] > seq[j]:
                   min = j
           seq[min],seq[i] = seq[i],seq[min]
        return seq   

    def insertSort(self,seq):
        length = len(seq)
        for i in range(1,length):
            if seq[i] < seq[i-1]:  
                #若第i个元素大于i-1元素，直接插入。小于的话，移动有序表后插入
                j = i - 1
                x = seq[i]
                seq[i] = seq[i-1]
                while x < seq[j]:
                    seq[j+1] = seq[j]
                    j = j - 1
                
                seq[j+1] = x
        return seq
     
def generateRandomIntList(len):
    l = []
    for i in range(0,len):
        rand = random.randint(0,100)
        l.append(rand)
    return l    
    
sort = SortLib()
print("随机生成原序列:",end = "")
seq = generateRandomIntList(20)
print(seq)
print("冒泡排序:",end="")
print(sort.bubbleSort(seq))
print("选择排序:",end="")
print(sort.selectSort(seq))
print("快速排序:",end="")
print(sort.quickSort(seq))
print("插入排序:",end="")
print(sort.insertSort(seq))

