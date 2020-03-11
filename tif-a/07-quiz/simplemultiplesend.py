import socket
import threading

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke server
sock.connect( ("127.0.0.1", 9999) )

# Definisikan fungsi yang akan dieksekusi pada setiap thread
def handleThread(conn):
    try :
        while True :
            # To do : buat thred baru
            # Terima data dari client
            data = conn.recv(100)
    except (socket.error, KeyboardInterrupt) :
        conn.close()
        print("Client menutup koneksi")

while True :
    # Thread handling
    clientThread = threading.Thread(target=handleThread, args=(sock,))
    clientThread.start()
    # Kirim data ke server
    data = input("Masukkan string yang akan dikirim : ")