import socket
import struct
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("0.0.0.0", 9999))

#Listen sebanyak jumlah backlog
sock.listen(10)

while True:
    conn, client_addr = sock.accept()

    data = conn.recv(8)
    data = struct.unpack('<ii', data)
    jumlah = data[0] + data[1]

    #kirim balik ke client
    jumlah = struct.pack('<i', jumlah)
    conn.send(jumlah)

