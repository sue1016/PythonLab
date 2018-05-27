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
        print(self.__items)

q = Queue()
q.printAll()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.printAll()
q.putfile('queue.txt')
print("dequeue:" + str(q.dequeue()))
q.printAll()
q.getfile('queue.txt')
q.printAll()
