import socket


def start_client(server_ip='127.0.0.1', server_port=5050):
    # 创建TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接到服务器
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server at {server_ip}:{server_port}")

    try:
        while True:
            # 从用户获取输入
            message = input("请输入要发送的消息：")
            # 发送消息到服务器
            client_socket.sendall(message.encode('utf-8'))

            # 接收服务器的回应
            data = client_socket.recv(1024)
            response = data.decode('utf-8')
            print(f"收到服务器应答: {response}，来自服务器 {server_ip}:{server_port}")

            # 如果用户输入的是'exit'或'EXIT'，则退出循环
            if message.lower() == 'exit':
                break
    finally:
        client_socket.close()


if __name__ == "__main__":
    start_client()