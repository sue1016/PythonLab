class Queue:
    def __init__(self):
        self.__items = []
      
    def enqueue(self,inItem):
        self.__items.append(inItem)

    def dequeue(self):
        outItem = self.__items[0]
        self.__items.pop(0)
        return outItem

    def putfile(self,filename):
        with open(filename,'w') as f:
            f.write(str(self.__items))

    def getfile(self,filename):
        with open(filename,'r') as f:
           self.__items =  f.read()

    def printAll(self):
        if len(self.__items) > 0:
            print("输出队列（左边为队头，右边为队尾）:"+str(self.__items))
        else:
            print("输出队列（左边为队头，右边为队尾）:空队列")

q = Queue()
q.printAll()
print("加入队列:1")
q.enqueue(1)
print("加入队列:2")
q.enqueue(2)
print("加入队列:3")
q.enqueue(3)
q.printAll()
print("写出到文件")
q.putfile('queue.txt')
print("出队列")
print("dequeue:" + str(q.dequeue()))
q.printAll()
print("从刚才的文件里读入")
q.getfile('queue.txt')
q.printAll()
'''
使用list实现队列结构  
使用__保护队列内部元素不被获取  
使用list.append实现在队尾添加元素  
使用list.pop(0)实现删除队头的元素  
文件操作用with open

'''
