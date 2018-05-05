#to print 99 mutifing table

for num1 in range(1,10):
    for num2 in range(1,num1+1):
        print(str(num1)+'*'+str(num2)+'='+str(num1*num2),end='  ')
    print('')


    '''
# 1 打印九九乘法表

1.两重嵌套循环实现九九乘法表
2.注意range函数是左闭右开
3.注意print()默认要换行
4.在Python3中print()要想不换行，在后面加,end='要追加的内容，并且不会换行'

    '''
