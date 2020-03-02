# import library
import socket
import select

# Inisiasi objek socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind socket
sock.bind( ("", 9000) )
# Listen
sock.listen(10)

# List untuk menampung semua objek yang akan dimonitor aktifitas I/O-nya
list_monitor = [sock]

while True :
    # Monitor aktifitas I/O yang berhubungan dengan input
    input_ready, output_ready, error_ready = select.select(list_monitor, [], [])
    # Iterasi untuk input yang aktif
    for i in input_ready :
        # Cek apakah ini aktifitas socket atau koneksi?
        # - Jika ini adalah aktifitas yang berkaitan dengan socket
        if i == sock :
            # Terima permintaan koneksi dari client
            conn, client_addr = sock.accept()
            # Masukkan koneksi client ke list monitor
            list_monitor.append(conn)
        # - Jika ini adalah aktifitas koneksi
        else :
            try :
                data = i.recv(100)
                data = data.decode('ascii')
                data = "OK "+data
                i.send(data.encode('ascii'))
            except socket.error :
                # Hapus koneksi yang tidak terpakai agar tidak dimonitor
                list_monitor.remove(i)
                print("Client memutuskan koneksi")

