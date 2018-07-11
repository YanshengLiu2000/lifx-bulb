import socket
import struct

def transfer(data_info):
    temp = ''
    result = b''
    for i in range(len(data_info)):
        temp += data_info[i]
        if len(temp) == 2:
            n = int(temp, 16)
            result += struct.pack('B', n)
            temp = ''
    return result


ip = '192.168.1.7'
# ip='255.255.255.255'
port = 56700
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 0))

for i in range(3):
    send_msg = transfer('2a00001401aef708d073d5018a1c00004c494658563200b8000000000000000075000000000000000000')
    s.sendto(send_msg, (ip, port))

# while(1):#alarm!!
#     send_msg = transfer('31000014c2caf301d073d5018a1c00004c494658563200320000000000000000660000000066ba09d7ffff28232c010000')#blue
#     s.sendto(send_msg, (ip, port))
#     time.sleep(1)
#     send_msg = transfer('31000014c2caf301d073d5018a1c00004c4946585632004c00000000000000006600000000a30f09d7ffff28232c010000')#red
#     s.sendto(send_msg, (ip, port))
#     time.sleep(1)

# with open('test.txt', 'r') as f:
#     lines=f.readlines()
#     line_num=0
#     for i in lines:
#         i=i.strip('\n')
#         print(i)
#         send_msg=transfer(i)
#         time.sleep(0.5)
#         print(line_num)
#         s.sendto(send_msg, (ip, port))
#         line_num+=1
