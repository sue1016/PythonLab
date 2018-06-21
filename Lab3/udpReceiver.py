#分别编写数据发送程序，数据接收程序。
#基于UDP协议实现。
#发送端发送的信息包括：发送时间，IP，端口，消息内容。
#接收端在接收到信息后将其显示出来，并保存在一个文件中。如果接收到“Bye”或“bye”，则退出。
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( ('127.0.0.1',8888) )
with open('receivedMsg.txt','w') as f:
    while True:
        data, addr = s.recvfrom(1024)
        f.write(str(data.decode())+str(addr[0])+str(addr[1])+'\n')
        print(data.decode(),addr[0],addr[1])
        if data.decode().lower().find('bye') != -1:
            break 
s.close()