import socket

client = socket.socket()
ip_port = ('127.0.0.1', 8880)
client.connect(ip_port)
name = client.recv(1024)
client.send('Names'.encode())
while True:
	data = client.recv(1024)
	print('{}: {}'.format(name.decode(), data.decode()))
	if data == b'exit':
		break
	msg = input('输入要发送的消息:')
	client.send(msg.encode())