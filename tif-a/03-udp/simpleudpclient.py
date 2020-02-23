# Import socket
import socket

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Kirim data ke server
server_addr = ("127.0.0.1", 9000)
data = "Selamat Sore"
sock.sendto(data.encode('ascii'), server_addr)

# Terima balasan dari server
data = sock.recv(65536)
data = data.decode('ascii')

print(data)
sock.close()