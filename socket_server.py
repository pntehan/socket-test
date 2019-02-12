import socket

sk = socket.socket()
ip_port = ('127.0.0.1', 8880)
sk.bind(ip_port)
sk.listen(5)
while True:
	print("正在等待接受数据请求...")
	print('输入quit退出...')
	conn, address = sk.accept()
	print("请求地址为: {}".format(address))
	msg = "pntehan"
	conn.send(msg.encode())
	name = conn.recv(1024)
	while True:
		msg = input('输入你有发送的消息:')
		conn.send(msg.encode())
		data = conn.recv(1024)
		print("{}: {}".format(name.decode(), data.decode()))
		if msg == 'exit':
			break
		# msg = input('输入你有发送的消息:')
		# conn.send(msg.encode())
	info = input()
	if info == 'quit':
		break
	conn.close()
