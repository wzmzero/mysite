from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
import socket
import threading
import time

data =b''
class SocketServer(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)
        print('init')

    def run(self):
        self.client_socket, client_address = self.server_socket.accept()
        print(self.client_socket, client_address)
        global data
        while True:
            data = self.client_socket.recv(1024)
            # print('recive:', data.decode())
            self.client_socket.sendall('Data received'.encode())
        client_socket.close()

class ChatConsumer(WebsocketConsumer):

    def websocket_connect(self, message):

        print("连接")
        server = SocketServer('0.0.0.0', 8002)
        server.start()
        self.accept()

    def websocket_receive(self, message):
        print('接收到消息', message)
        # text = message['text']
        # res = "{}SB".format(text)
        time.sleep(1)
        t = time.strftime('%H:%M:%S', time.localtime(time.time()))
        print('recive:', t+','+data.decode())
        self.send(t+','+data.decode())

    def websocket_disconnect(self, message):

        print('客户端断开连接了')
        raise StopConsumer()

