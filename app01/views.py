from django.shortcuts import render , HttpResponse,redirect
from app01.models import UserInfo
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
            self.data = client_socket.recv(1024)
            print('recive:', self.data.decode())
            client_socket.sendall('Data received'.encode())
            # client_socket.close()

# Create your views here.

def login(request):
    # server = SocketServer('localhost', 8002)
    # server.start()
    if request.method == "GET":
        return render(request, "login.html")
    print(request.POST)
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    obj = UserInfo.objects.filter(name=user, password=pwd).count()
    print(obj)
    if  obj:
        return render(request, "charts.html",{"msg":"server.data.decode()"})
    return render(request, 'login.html',{"error_msg":"用户名或密码错误"})

def index(request):
    return render(request, "charts.html")

# def orm(request):
#     # if request.method == 'POST':
#     #     data = request.POST.get('data')
#     #     # 在这里可以将数据发送给socket服务器
#     #     # 例如，可以使用socket发送数据到指定的主机和端口
#     #     # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     #     # client_socket.connect((host, port))
#     #     # client_socket.sendall(data.encode())
#     #     # response = client_socket.recv(1024)
#     #     # client_socket.close()
#     #     return HttpResponse('Data sent')
#     # 在这里可以启动socket服务器
#     server = SocketServer('localhost', 8888)
#     server.start()
#     return render(request, "orm.html",{"msg":server.data.decode()})




