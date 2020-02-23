# Import library socket
import socket

# Inisiasi objek socket UDP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind server agar bisa menerima data 
# dari semua IP pada port 9000
sock.bind( ("0.0.0.0", 9000) )

while True :
    # Terima data dari client
    data, client_addr = sock.recvfrom(65536)

    # Konversi array of bytes jadi string
    data = data.decode('ascii')
    # Tambah "OK" di depan data
    data = "OK "+data

    # Kirim balik ke client
    sock.sendto(data.encode('ascii'), client_addr)

# Tutup socket
sock.close()