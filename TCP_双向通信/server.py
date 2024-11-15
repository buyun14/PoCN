import socket


def start_server(host='127.0.0.1', port=5050):
    # 创建TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定地址
    server_socket.bind((host, port))
    # 开始监听
    server_socket.listen(5)
    print(f"Server started on {host}:{port}")

    while True:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        while True:
            # 接收客户端消息
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"Received from {client_address}: {message}")

            # 向客户端发送应答
            response = f"{message} 已经收到"
            client_socket.sendall(response.encode('utf-8'))

        # 关闭连接
        client_socket.close()
        print(f"Connection with {client_address} closed")


if __name__ == "__main__":
    start_server()