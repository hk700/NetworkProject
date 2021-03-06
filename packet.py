#/usr/bin/python
#Comnetsii APIs for Packet. Rutgers ECE423/544
#Author: Sumit Maheshwari
import time
from socket import socket, AF_INET, SOCK_DGRAM
import struct
import select
import random
import asyncore
import numpy as np
import os
from variables import * # imports all the variables for the network
'''
from nodes import Nodes

def makeNode(ip,id,port):
    n = Nodes(ip,id,port)
    return n

s1 =makeNode("192.168.1.1","s1",8881)
r1 =makeNode(("192.168.1.2","10.0.1.0","10.0.2.0"),"r1",8882)
r2 =makeNode(("10.0.1.1","10.0.3.1","10.0.4.1"),"r2",8883)
r3 =makeNode(("10.0.2.1","10.0.3.2","10.0.5.1","10.0.6.1"),"r3",8884)
r4 =makeNode(("10.0.4.2","10.0.7.1"),"r4",8885)
r5 =makeNode(("10.0.5.2","192.168.3.2"),"r5",8886)
r6 =makeNode(("10.0.6.2","192.168.4.2"),"r6",8887)
r7 =makeNode(("10.0.7.2","192.168.2.2"),"r7",8888)

d1 =makeNode("192.168.2.1","d1",8889)
d2 =makeNode("192.168.3.1","d2",8890)
d3 =makeNode("192.168.4.1","d3",8891)
'''
def read(src,dest):
    fileDir = os.path.dirname(os.path.abspath(__file__))
    f = open(fileDir+'/'+'graphs'+'/'+src+"_"+dest+".txt", "r")
    re= f.readline()
    print(re)
   # new_str = re.replace('->', '') 
    array = re.split("->")

    print('The Next Hop is ' + array[1])
    return array[1]

def create_packet(pkttype, src, dst, seq, data):
    """Create a new packet based on given id"""
    # Type(1),  LEN(4), SRCID(1),  DSTID(1), SEQ(4), DATA(1000)
    pktlen = len(data)
    header = struct.pack('BLBBL', pkttype, pktlen, dst, src, seq)
    return header + bytes(data,'utf-8')

def read_header(pkt):
    #Change the bytes to account for network encapsulations
    header = pkt[0:32]
    #pktFormat = "BLBBL"
    #pktSize = struct.calcsize(pktFormat)
    pkttype, pktlen, dst, src, seq = struct.unpack('BLBBL', header)
    return pkttype, pktlen, dst, src, seq

def read_data(pkt):
        #Change the bytes to account for network encapsulations
    data = pkt[32:]
    return data


#Note only thing changed above was the number of bits accounted for in header 16 --> 32 

###################################
####   Assignment Code Below   ####
###################################

#Starts a ping from current host (src) to desired destination (dst)
def ping(h, c, dst):
    seq_num, nor, rtt = 0, 0, []
    #count = 0
    for x in range(c):
        #count += 1
        # Creates and sends the request packet 
        packet = create_packet(1, h.id, dst, seq=seq_num, data='This is the Project!')
        send_packet(h, packet)
        send_time = time.time()

        # Waits to receive a reply packet to move onto next ping
        seq_failed = receive_packet(h, packet)
        if seq_failed == -1:
            rtt.append(time.time()-send_time)
            seq_num += 1
        else:
            x -= 1
            nor += 1
            print("Retransmitting packet with seq num: ", seq_num)
    rtt = np.array(rtt)
    #print(count)
    print(c, " packets transmitted, ", nor, " packets retransmitted, ", (nor/c)*100, "% packet loss",
         "\n round-trip min/avg/max/stddev = ", np.min(rtt),"/",np.mean(rtt),"/",np.max(rtt),"/",np.std(rtt), " s" )
    return 0

# Sends a packet across UDP socket the corresponding router gateway for that host
def send_packet(h, packet):
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(packet, h.default_gateway)
    s.close()
    print("Sending: ", packet, " To: ", h.default_gateway)
    return 0

# Receives packets across UDP socket
def receive_packet(h, sent_packet):
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind((h.ip, h.port))
    seq_failed = -1

    #Waits to receive packet on h.ip/h.port 
    while True:
        try:
            if sent_packet != None:
                s.settimeout(0.007)
            packet,addr = s.recvfrom(1024)
            pkttype, pktlen, dst, src, seq = read_header(packet)
        except OSError:
            pkttype, pktlen, dst, src, seq = read_header(sent_packet)
            seq_failed = seq
            break

        if(pkttype == 1 and dst == h.id):
            print("Received: ", packet, " From: ", src)

            # Creates reply packet
            packet = create_packet(2, h.id, src, 0, 'This is a reply!')
            send_packet(h, packet)

        # Checks for reply packet (Note this is not very flexable and would break the server if it receives reply packet)
        elif(pkttype == 2 and dst == h.id):
            #data = read_data(packet)
            print("Receved: ", packet, " From: ", src)
            break

    s.close()
    return  seq_failed




