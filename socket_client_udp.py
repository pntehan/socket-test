import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8888)
while True:
    # print('请输入要发送的信息...')
    msg = input('请输入要发送的信息:')
    client.sendto(msg.encode(), ip_port)
    if msg == 'exit':
        break


