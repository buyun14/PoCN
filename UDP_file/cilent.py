import socket
import os
import time

# 服务器 IP 和端口
SERVER_IP = '127.0.0.1'
SERVER_PORT = 50512  # 与服务器端保持一致
BUFFER_SIZE = 1024
FILE_NAME = r"C:\Users\21354\Videos\asdf.mp4"  # 使用原始字符串
TIMEOUT = 5  # 重传超时时间 s

def udp_client():
    # 创建 UDP 套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(TIMEOUT)

    # 检查文件是否存在
    if not os.path.exists(FILE_NAME):
        print(f"File {FILE_NAME} not found")
        return

    # 获取文件大小
    file_size = os.path.getsize(FILE_NAME)
    print(f"File size: {file_size} bytes")

    with open(FILE_NAME, 'rb') as file:
        seq = 0
        while True:
            data = file.read(BUFFER_SIZE - 4)
            if not data:
                break

            packet = seq.to_bytes(4, byteorder='big') + data
            client_socket.sendto(packet, (SERVER_IP, SERVER_PORT))
            print(f"Sent sequence {seq}")

            try:
                ack, _ = client_socket.recvfrom(4)
                ack_seq = int.from_bytes(ack, byteorder='big')
                if ack_seq == seq:
                    print(f"ACK received for sequence {seq}")
                    seq += 1
                else:
                    print(f"Unexpected ACK {ack_seq}, resending sequence {seq}")
            except socket.timeout:
                print(f"Timeout, resending sequence {seq}")

    # 发送结束标志
    client_socket.sendto(b'exit', (SERVER_IP, SERVER_PORT))
    print("File transfer complete")

    client_socket.close()
    print("Client closed")

if __name__ == "__main__":
    udp_client()