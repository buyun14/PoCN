import socket
import os


def start_server(host='127.0.0.1', port=65432):
    # 创建socket对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 绑定地址和端口
        server_socket.bind((host, port))

        # 开始监听，设置最大连接数为5
        server_socket.listen(5)
        print("服务器启动，等待客户端连接...")

        while True:
            # 接受一个新连接
            client_socket, addr = server_socket.accept()
            print(f"来自{addr}的连接已建立")

            # 接收文件名
            file_name_length = int.from_bytes(client_socket.recv(4), 'big')
            file_name = client_socket.recv(file_name_length).decode('utf-8')
            print(f"接收文件名: {file_name}")

            # 接收文件大小
            file_size = int.from_bytes(client_socket.recv(8), 'big')
            print(f"接收文件大小: {file_size} bytes")

            # 准备接收文件
            with open(file_name, 'wb') as f:
                received_size = 0
                while received_size < file_size:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    f.write(data)
                    received_size += len(data)

            print(f"文件{file_name}接收完成")

            # 发送确认消息
            client_socket.sendall(b'File received successfully')

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 关闭socket
        server_socket.close()


if __name__ == "__main__":
    start_server()