import socket
import threading

class SocketServer(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.data = bytes()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)
        print('init')

    def run(self):
        client_socket, client_address = self.server_socket.accept()
        print(client_socket, client_address)
        while True:
            try:
                self.data = client_socket.recv(1024)
                client_socket.sendall('Data received'.encode())
                print('recive:', self.data.decode())
            except:
                print('客户端连接被强制断开，等待重新连接')
                client_socket, client_address = self.server_socket.accept()
                print(client_socket, client_address)
            # client_socket.close()

def main():
    server = SocketServer('0.0.0.0', 8002)
    server.start()


if __name__ == '__main__':
    main()