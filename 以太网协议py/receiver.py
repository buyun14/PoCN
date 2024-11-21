from scapy.layers.l2 import Ether
from scapy.packet import Raw
from scapy.sendrecv import sniff


def process_packet(packet):
    if Ether in packet:
        ether = packet[Ether]

        # 检查目的地址是否匹配
        if ether.dst == "00:11:22:33:44:55":
            # 打印帧首部和校验字段值
            print("帧首部:")
            print(f"目的MAC地址: {ether.dst}")
            print(f"源MAC地址: {ether.src}")
            print(f"类型: {ether.type}")

            # 打印数据部分
            if Raw in packet:
                print("数据部分:")
                print(packet[Raw].load.hex())

                # 将数据写入文件
                with open("received_video_file.mp4", 'ab') as file:
                    file.write(packet[Raw].load)
                print(f"接收数据帧: {len(packet[Raw].load)} 字节")


def receive_ethernet_frame(interface):
    # 开始捕获数据包
    print(f"开始捕获数据包，接口: {interface}")
    sniff(iface=interface, prn=process_packet, filter="ether dst 00:11:22:33:44:55")


if __name__ == "__main__":
    interface = "WLAN"  # 替换为你的网络接口名称
    receive_ethernet_frame(interface)
    print("数据包捕获结束")