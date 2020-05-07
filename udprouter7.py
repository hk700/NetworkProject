from socket import socket, AF_INET, SOCK_DGRAM
from packet import *
from threading import Thread
from variables import * # imports all the variables for the network
#Creates new router
class udprouter():

        # For sake of assignment I am letting each router know eachothers rt
        def __init__(self, id, port):
                self.port = port
                self.id = id
                self.rt = { 'routes': [{'id': 204, 'ip': '10.0.7.1', 'gateway': '10.0.7.2', 'port':8884},
                {'id': 102, 'ip': '192.168.2.1', 'gateway': '192.168.2.2', 'port':8888}] }

        # Using the dst received in packet finds the corresponding dst address
        def search_dst_addr(self, dst):
                for x in range(len(self.rt['routes'])):
                        if self.rt['routes'][x]['id'] == dst:
                                return (self.rt['routes'][x]['ip'], self.rt['routes'][x]['port'])
                return ('192.168.2.1', 8888)

        # Sends packet to dst address
        def handle_sending(self, packet, server):
                s = socket(AF_INET, SOCK_DGRAM)
                s.sendto( packet, server )
                print('Sending To: ', server)
                s.close()
                return 0

        # Waits to receive a packet and if the correct type starts new thread to sent that packet
        def handle_packets(self):
                s = socket(AF_INET, SOCK_DGRAM)
                s.bind(('0.0.0.0', self.port))
                while True:
                        packet, addr = s.recvfrom(1024)
                        print("Received From: ", addr)
                        pkttype, pktlen, dst, src, seq = read_header(packet)
                        if pkttype == 1 or pkttype == 2:
                                server = self.search_dst_addr(dst)
                                thread = Thread(target=self.handle_sending(packet,server))
                                thread.start()
                s.close()
                return 0

if __name__ == '__main__':
        print("Router Started...")
        udp_router = udprouter(r7.id, r6.port)
        udp_router.handle_packets()
