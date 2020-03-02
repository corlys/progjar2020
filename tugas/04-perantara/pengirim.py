import socket

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke server
sock.connect( ("127.0.0.1", 9999) )

while True :
    # Kirim data ke server
    data = input("Masukkan string yang akan dikirim : ")
    sock.send(data.encode('ascii'))