import socket

client = socket.socket()
ip_port = ('127.0.0.1', 8888)
client.connect(ip_port)
data = client.recv(1024)
print(data.decode())
while True:
    msg = input('输入要发送的消息:')
    client.send(msg.encode())
    if msg == 'quit':
        break

