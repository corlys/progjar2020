import threading
import socket
import binascii
import struct
import time
import sys


rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))

while True:
   packet = rawSocket.recv(65535)
#   print(packet)
#   print(sys.getsizeof(packet))
   arppacket = struct.unpack("!2s2s1s1s2s6s4s6s4s", packet[14:42])
   print(binascii.hexlify(arppacket[4]))