import socket

# Inisiasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Kirim data
server_addr = ("127.0.0.1", 9000)
data = "Selamat siang"
sock.sendto( data.encode('ascii'), server_addr  )

# Baca data dari server
data = sock.recv(65536)
data = data.decode('ascii')
print(data)