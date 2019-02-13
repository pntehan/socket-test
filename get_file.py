import socket

sk = socket.socket()
ip_port = ('127.0.0.1', 8888)
sk.bind(ip_port)
sk.listen(5)
# print('输入quit退出服务器...')
while True:
    conn, address = sk.accept()
    print('连接主机{}\n接受文件...'.format(address))
    file_name = conn.recv(1024).decode()
    name = file_name.split('\\')[-1]
    print(name)
    while True:
        with open(name, 'ab') as f:
            data = conn.recv(1024)
            # print(data)
            if not data:
                print('接受完毕!')
                break
            f.write(data)
    info = input('输入quit退出服务器:')
    if info == 'quit':
        break
sk.close()
