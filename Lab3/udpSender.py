#分别编写数据发送程序，数据接收程序。
#基于UDP协议实现。
#发送端发送的信息包括：发送时间，IP，端口，消息内容。
#接收端在接收到信息后将其显示出来，并保存在一个文件中。如果接收到“Bye”或“bye”，则退出。
import time
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    info = input("input your message: ")
    if info == 'quit':
        break 
    else:
        info = info + "  time :"
        info = info + str(time.asctime(time.localtime(time.time())))
        s.sendto(info.encode(),("127.0.0.1",8888)) 
s.close()