import socketserver

class Myserver(socketserver.BaseRequestHandler):
    #handle方法出错将会跳过，但setup与finish一定会执行
    #首先执行setup
    def setup(self):
        pass

    #然后执行handle
    def handle(self):
        conn = self.request
        msg = 'Hello World!'
        conn.send(msg.encode())
        print('链接建立...')
        while True:
            data = conn.recv(1024)
            if data == b'quit':
                print('链接关闭...')
                break
            else:
                print('接受消息:', data.decode())
        conn.close()

    #最后执行finish
    def finish(self):
        pass

if __name__ == '__main__':
    #创建多线程实例
    sk = socketserver.TCPServer(('127.0.0.1', 8888), Myserver)
    print('开启异步多线程，等待链接')
    sk.serve_forever()

