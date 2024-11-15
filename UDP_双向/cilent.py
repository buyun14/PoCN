import socket


def start_client(server_ip='127.0.0.1', server_port=50520):
    # 创建UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            # 从用户获取输入
            message = input("请输入要发送的消息：")
            # 发送消息到服务器
            sock.sendto(message.encode('utf-8'), (server_ip, server_port))

            # 接收服务器的回应
            data, server_addr = sock.recvfrom(1024)
            response = data.decode('utf-8')
            server_ip, server_port = server_addr
            print(f"收到服务器应答: {response}，来自服务器 {server_ip}:{server_port}")

            # 如果用户输入的是'exit'或'EXIT'，则退出循环
            if message.lower() == 'exit':
                break
    finally:
        sock.close()


if __name__ == "__main__":
    start_client()