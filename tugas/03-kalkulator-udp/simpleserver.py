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
    hasil = eval(data)
    # - Tambahkan string OK
    """
    data = data.split()

    angka = int(data[0])
    angkaDua = int(data[1])
    operator = data[2]
    hasil = 0
    
    if operator == "+":
        hasil = angka + angkaDua
    elif operator == "-":
        hasil = angka - angkaDua
    elif operator == "*":
        hasil = angka * angkaDua
    elif operator == "/":
        hasil = angka / angkaDua
    else :
        hasil = "Operator tidak dikenali"
    """
    hasil = str(hasil)
    # Kirim balik ke client
    sock.sendto(hasil.encode('ascii'), client_addr )

# Tutup socket
sock.close()



