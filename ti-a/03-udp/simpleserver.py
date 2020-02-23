import socket

# Inisiasi objek socket IPv4 dan UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Address binding agar bisa berkomunikasi 
# dengan client IP manapun pada port 9000
sock.bind( ("", 9000) )

while True :
    # Receive data dari client dengan ukuran 64KB
    data, client_addr = sock.recvfrom(65536)

    # Tambah ok di depan data
    # - Konversi dari array of bytes ke string
    data = data.decode('ascii')
    # - Tambahkan string OK
    data = "OK "+data

    # Kirim balik ke client
    sock.sendto(data.encode('ascii'), client_addr )

# Tutup socket
sock.close()



