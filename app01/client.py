import socket
import time
import random
# 连接到服务端的主机名和端口号
host = '0.0.0.0'  # 服务端的主机名或IP地址
port = 8002     # 服务端的端口号

# 建立TCP连接
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        client_socket.connect((host, port))
        break
    except:
        client_socket.close()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
i=0
# 循环向服务端发送数据
while True:
    hum = random.randint(20.0, 80.0)
    temper=random.randint(20.0,40.0)
    data = str(hum)+','+str(temper)
    try:
        client_socket.sendall(data.encode())
        print(data)
        response = client_socket.recv(1024)
        print(response.decode())
        time.sleep(1)
        i += 1
    except:
        while True:
            try:
                client_socket.connect((host, port))
                break
            except:
                client_socket.close()
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 关闭连接
client_socket.close()
