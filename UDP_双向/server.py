import socket


def start_server(host='127.0.0.1', port=50520):
    # 创建UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定地址
    sock.bind((host, port))
    print(f"Server started on {host}:{port}")

    while True:
        # 接收客户端消息
        data, addr = sock.recvfrom(1024)
        message = data.decode('utf-8')
        print(f"Received from {addr}: {message}")

        # 向客户端发送应答
        response = f"{message} 已经收到"
        sock.sendto(response.encode('utf-8'), addr)


if __name__ == "__main__":
    start_server()