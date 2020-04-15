# Import socket
import socket
import threading

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
sock.bind( ("0.0.0.0", 9999) )

# Listen sebanyak jumlah backlog
sock.listen(10)

# Fungsi yang akan dieksekusi pada setiap thread
def handle_thread(conn):
    try : 
        #Baca header
        body = ""
        bodylen = ""
        headers = ""
        while True :
            #Baca setiap 4 byte
            temp = conn.recv(4)
            temp = temp.decode('ascii')
            headers = headers + temp
            if '\r\n\r\n' in headers:
                headers = headers.replace('\r\n\r\n', '')
                splits = headers.split('Content-Length: ')
                bodylen = bodylen+splits[1].replace('\r\n\r\n', '')
                temp = conn.recv(int(bodylen))
                temp = temp.decode('ascii')
                body = body + temp
                break
        headers = headers.replace('\r\n\r\n', '')
        #debug
        print(headers)
        print(bodylen)
        print(body)
        #kembalikan response ke client
        #response = ('HTTP/1.1 200 OK\r\n'+
        #           'Content-Type: text/html\r\n'+
        #           'Content-Length: 5\r\n'
        #           'Connection: close\r\n'
        #           '\r\n'+
        #           str(body))
        suplement = ' pleasework\r\n\r\n'
        suplength = len(suplement)
        length = int(bodylen)+suplength
        response = ('HTTP/1.1 200 OK\r\n'+
                    'Content-Type: text/html\r\n'+
                    'Content-Length: '+str(length)+'\r\n'
                    'Connection: close\r\n'
                    '\r\n'+
                    body+suplement)
        print(response)           
        conn.send(response.encode('ascii'))
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
    
    
