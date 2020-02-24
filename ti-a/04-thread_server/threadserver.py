import socket
import threading

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke IP dan port tertentu
sock.bind( ("", 9999) )

# Listen permintaan koneksi dari client
# - Param : berapa jumlah permintaan koneksi yang diterima
sock.listen(100)

# Definisikan fungsi yang akan dieksekusi pada setiap thread
def handleThread(conn):
    try :
        while True :
            # To do : buat thred baru
            # Terima data dari client
            data = conn.recv(100)
            data = data.decode('ascii')
            data = "OK "+data
            # Kirim balik ke client
            conn.send(data.encode('ascii'))
    except (socket.error, KeyboardInterrupt) :
        conn.close()
        print("Client menutup koneksi")

try :
    while True :
        # Panggil fungsi accept untuk menerima permintaan koneksi dari client
        # Return : objek koneksi ke client dan alamat client
        conn, client_addr = sock.accept()
        # Buat thread baru
        clientThread = threading.Thread(target=handleThread, args=(conn,))
        clientThread.start()
except KeyboardInterrupt :
    print("Server mati")
    

