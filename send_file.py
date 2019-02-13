import socket
from tqdm import *

client = socket.socket()
ip_port = ('127.0.0.1', 8888)
client.connect(ip_port)
#文件上传操作
aim_file = input('输入要上传的文件路径:')
client.send(aim_file.encode())
with open(r'%s'%aim_file, 'rb') as f:
    print('文件发送中...')
    for i in tqdm(f):
        client.send(i)
# client.send('quit'.encode())