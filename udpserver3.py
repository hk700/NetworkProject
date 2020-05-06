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
        udp_server = udpserver(d3.id, d3.ip, gateway=(r6.ip,r5.port), port=d2.port)
        receive_packet(udp_server, None)
