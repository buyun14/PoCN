import socket
import os

# 服务器 IP 和端口
SERVER_IP = '127.0.0.1'
SERVER_PORT = 50512  # 与客户端保持一致
BUFFER_SIZE = 1024
FILE_NAME = 'received_file.mp4' # 接收到的文件保存名

def udp_server():
    # 创建 UDP 套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

    expected_seq = 0
    with open(FILE_NAME, 'wb') as file:
        while True:
            data, addr = server_socket.recvfrom(BUFFER_SIZE)
            if data == b'exit':
                print("File transfer complete")
                break

            seq, content = data[:4], data[4:]
            seq = int.from_bytes(seq, byteorder='big')

            if seq == expected_seq:
                file.write(content)
                expected_seq += 1
                print(f"Received and wrote sequence {seq}")
                server_socket.sendto(seq.to_bytes(4, byteorder='big'), addr)
            else:
                print(f"Out of order packet {seq}, expecting {expected_seq}")
                server_socket.sendto(expected_seq.to_bytes(4, byteorder='big'), addr)

    server_socket.close()
    print("Server closed")

if __name__ == "__main__":
    udp_server()