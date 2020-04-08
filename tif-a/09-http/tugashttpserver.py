# Import socket
import socket
import threading

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
sock.bind( ("0.0.0.0", 9922) )

# Listen sebanyak jumlah backlog
sock.listen(10)

# Fungsi yang akan dieksekusi pada setiap thread
def handle_thread(conn):
    try : 
        #Baca header
        headers = ""
        while True :
            #print(fileopen.read())
            #Baca setiap 4 byte
            temp = conn.recv(4)
            temp = temp.decode('ascii')
            headers = headers + temp
            if '\r\n\r\n' in headers:
                headers.replace('\r\n\r\n', '')
                break;
        fileopen = open('testo.html', 'r')
        #debug
        print(headers)
        #kembalikan response ke client
        response = ('HTTP/1.1 200 OK\r\n'+
                   'Content-Type: text/html\r\n'+
                   'Content-Length: '+str(len(fileopen.read()))+'\r\n'
                   'Connection: close\r\n'
                   '\r\n'+
                   fileopen.read())
        print(response)
        conn.send(response.encode('ascii'))
        fileopen.close()
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
    
    
