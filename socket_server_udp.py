import socket

#创建实例，使用UDP的通讯方式
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8888)
sk.bind(ip_port)
while True:
    print('等待接受信息...')
    data = sk.recv(1024)
    print('所接受的信息是:', data.decode())
    if data == b'exit':
        break