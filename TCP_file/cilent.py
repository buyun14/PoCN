import os
import socket


def send_file(file_path, host='127.0.0.1', port=65432):
    # 创建socket对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 连接到服务器
        client_socket.connect((host, port))
        print("连接到服务器成功")

        # 获取文件名和文件大小
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        # 发送文件名
        client_socket.sendall(len(file_name).to_bytes(4, 'big'))
        client_socket.sendall(file_name.encode('utf-8'))

        # 发送文件大小
        client_socket.sendall(file_size.to_bytes(8, 'big'))

        # 发送文件数据
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                client_socket.sendall(data)

        print("文件发送完成")

        # 接收服务器的确认消息
        response = client_socket.recv(1024)
        print(f"服务器回复: {response.decode('utf-8')}")

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 关闭socket
        client_socket.close()


if __name__ == "__main__":
    file_to_send = "C:\\Users\\21354\\Videos\\asdf.mp4"  # 替换为你想要发送的文件路径
    send_file(file_to_send)