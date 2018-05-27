class Stack(object):
    def __init__(self):
         self.__items = []

    def pushstack(self,inItem):
        self.__items.append(inItem)

    def popstack(self):
        outItem = self.__items.pop()
        return outItem

    def isempty(self):
        if len(self.__items) > 0:
            return False
        else:
            return True

    def peekstack(self):
        return self.__items[-1]
    
    def printAll(self):
        if self.isempty():
            print("输出栈，（左边为栈底）：空栈")
        else:  
            print("输出栈，（左边为栈底）："+str(self.__items))

stack = Stack()
stack.printAll()
print("现在栈空吗:"+str(stack.isempty()))
print("push1")
stack.pushstack(1)
print("push2")
stack.pushstack(2)
print("push3")
stack.pushstack(3)
stack.printAll()
print("输出栈顶元素",end=":")
print(stack.peekstack())
print("弹出栈顶元素")
stack.popstack()
stack.printAll()
'''
用list实现栈结构   
用__防止外部获得栈内部内容  
用list的append实现在栈顶添加元素   
用list的pop实现在栈顶删除函数  
用len > 0判断是否为空   
用list[-1]来获取顶部元素  


'''


