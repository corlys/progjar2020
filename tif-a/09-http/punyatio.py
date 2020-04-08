# Import socket
import socket
import threading
import os

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
sock.bind( ("0.0.0.0", 9998) )

# Listen sebanyak jumlah backlog
sock.listen(10)

def getfilesize(filename):
    return os.stat(filename).st_size

# Fungsi yang akan dieksekusi pada setiap thread
def handle_thread(conn):
    try :
        # Baca header
        headers = ""
        while True :
            temp = conn.recv(100)
            temp = temp.decode('ascii')
            headers = headers + temp
            if "\r\n\r\n" in headers :
                headers = headers.replace("\r\n\r\n", "")
                break
        # Cetak header yang diterima
        selectFile = open("index.html", 'r')
        print(headers)
        # Kembalikan respons ke client
        reponse = ("HTTP/1.1 200 OK\r\n"
                   "Content-Type: text/html\r\n"+
                   "Content-Length: "+str(len(selectFile.read()))+"\r\n"+
                   "Connection: close\r\n"+
                   "\r\n"+ 
                   selectFile.read())
        print(reponse)
        conn.send(reponse.encode('ascii'))
        selectFile.close()
    except (socket.error, KeyboardInterrupt):
        conn.close()
        print("Client menutup koneksi")

try :
    while True :
        # Terima permintaan koneksi
        conn, client_addr = sock.accept()
        # Buat thread baru setiap ada permintaan koneksi dari client
        clientThread = threading.Thread(target=handle_thread, args=(conn,))
        clientThread.start()
except KeyboardInterrupt :
    print("Server mati")
    
    