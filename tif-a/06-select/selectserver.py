# import library yang dibutuhkan
import socket
import select

# socket tcp/ipv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binding
sock.bind( ("", 9999) )
# Listen
sock.listen(10)

# List yang berisi aktifitas input apa saja yang akan saya monitor
list_monitor = [sock]

while True :
    # Cek aktifitas I/O
    inready, outready, errready = select.select(list_monitor, [], [])
    # Iterasi semua aktifitas input yang siap untuk dieksekusi
    for s in inready :
            # Jika aktifitas input berhubungan dengan socket -> fungsi accept()
            if s == sock :
                # Terima permintaan koneksi
                conn, client_addr = s.accept()
                # Tambahkan koneksi baru ke list yang dimonitor
                list_monitor.append(conn)
            # Jika aktifitas input berhubungan dengan koneksi -> fungsi recv()
            else :
                try :
                    data = s.recv(100)
                    data = data.decode('ascii')
                    data = "OK "+data
                    s.send(data.encode('ascii'))
                except socket.error :
                    list_monitor.remove(s)
                    print("Client memutuskan koneksi")
