import socket

sk = socket.socket()
ip_port = ('127.0.0.1', 8880)
sk.bind(ip_port)
sk.listen(5)
while True:
	print("正在等待接受数据请求...")
	conn, address = sk.accept()
	print("请求地址为: {}".format(address))
	msg = "Hello World!"
	conn.send(msg.encode())
	while True:
		data = conn.recv(1024)
		print("所接受的消息是: {}".format(data.decode()))
		if data == b'exit':
			break
		msg = input('输入你有发送的消息:')
		conn.send(msg.encode())
	conn.close()
