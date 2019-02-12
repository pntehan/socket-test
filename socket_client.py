import socket

client = socket.socket()
ip_port = ('127.0.0.1', 8880)
client.connect(ip_port)
while True:
	data = client.recv(1024)
	print(data.decode())
	msg = input('输入要发送的消息:')
	client.send(msg.encode())
	if msg == 'exit':
		break