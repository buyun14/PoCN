from scapy.layers.l2 import Ether
from scapy.packet import Raw
from scapy.sendrecv import sendp


def send_ethernet_frame(file_path, interface):
    # 读取文件内容
    with open(file_path, 'rb') as file:
        data = file.read()

    # 分割数据，每个数据帧不超过1500字节
    max_frame_size = 1500
    frames = [data[i:i + max_frame_size] for i in range(0, len(data), max_frame_size)]

    for frame_data in frames:
        # 创建以太网帧
        ether = Ether()

        # 设置目的和源MAC地址
        ether.dst = "00:11:22:33:44:55"  # 目的MAC地址
        ether.src = "00:AA:BB:CC:DD:EE"  # 源MAC地址

        # 设置协议类型（0x0800表示IP协议）
        ether.type = 0x0800

        # 填充数据部分
        ether /= Raw(load=frame_data)

        # 发送以太网帧
        sendp(ether, iface=interface)
        print(f"发送数据帧: {len(frame_data)} 字节")


if __name__ == "__main__":
    file_path = "C:\\Users\\21354\\Videos\\asdf.mp4"  # 替换为你的视频文件路径
    interface = "WLAN"  # 替换为你的网络接口名称
    send_ethernet_frame(file_path, interface)
    print("所有数据帧发送完毕")