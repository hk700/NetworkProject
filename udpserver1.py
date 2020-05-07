from socket import socket, AF_INET, SOCK_DGRAM
from packet import *
from variables import * # imports all the variables for the network
#Creates to new server
class udpserver():

        def __init__(self, id, ip, gateway, port):
                self.ip = ip
                self.id = id
                self.default_gateway = gateway
                self.port = port

#Initializes new server and sets it up to receive packets
if __name__ == '__main__':
        print("Server Start...")
        udp_server = udpserver(id=102, ip='192.168.2.1', gateway=('192.168.2.2',8884), port=8888)
        #udp_server = udpserver(d1.id, d1.ip, gateway=(r7.ip,r6.port), port=r7.port)
        receive_packet(udp_server, None)
