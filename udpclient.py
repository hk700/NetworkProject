from socket import socket, AF_INET, SOCK_DGRAM
from packet import *
from variables import * # imports all the variables for the network
#Creates class for client
class udpclient():

        def __init__(self, id, ip, gateway, port):
                self.ip = ip
                self.id = id
                self.default_gateway = gateway
                self.port = port

#Initializes a new client and starts the ping
if __name__ == '__main__':
       # udp_client = udpclient(id=101, ip='192.168.1.1', gateway=('192.168.1.2',8881), port=8880)
       # ping(udp_client, c=100, dst=103)
        udp_client = udpclient(s1.id, ip=s1.ip, gateway=(r1.ip,s1.port), port=8880)
        ping(udp_client, c=100, dst=d2.id)
