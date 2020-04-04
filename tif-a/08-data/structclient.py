import socket
import struct 

#Inisialisasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Kirim permintaan koneksi
sock.connect(("127.0.0.1", 9999))

#Kirim data 
#Definisikan data
a = 200
b = 210

#representasikan data a dan b sebagai binary
data = struct.pack('<ii', a, b)
sock.send(data)
#Terima balasan dari server
data = sock.recv(4)
data = struct.unpack("<i", data)
print(data[0])
