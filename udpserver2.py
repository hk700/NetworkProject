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
        udp_server = udpserver(id=103, ip='192.168.3.1', gateway=('192.168.3.2',8886), port=8889)

        #udp_server = udpserver(d2.id, d2.ip, gateway=(r5.ip,r4.port), port= d1.port)
        receive_packet(udp_server, None)
