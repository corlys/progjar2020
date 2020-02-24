import socket

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke IP dan port tertentu
sock.bind( ("", 9999) )

# Listen permintaan koneksi dari client
# - Param : berapa jumlah permintaan koneksi yang diterima
sock.listen(100)

while True :
    # Panggil fungsi accept untuk menerima permintaan koneksi dari client
    # Return : objek koneksi ke client dan alamat client
    conn, client_addr = sock.accept()
    # Terima data dari client
    data = conn.recv(100)
    data = data.decode('ascii')
    data = "OK "+data
    # Kirim balik ke client
    conn.send(data.encode('ascii'))
    # Tutup koneksi (opsional)
    #conn.close()

