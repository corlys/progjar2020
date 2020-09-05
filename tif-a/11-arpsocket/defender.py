import socket
import threading

rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
rawSocket.bind(("wlp2s0", socket.htons(0x0806)))

while True:
	arpdata = rawSocket.recv(65535)
	print(arpdata)