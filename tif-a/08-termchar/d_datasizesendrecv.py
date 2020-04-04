import struct

def sendalldata(conn, message):
    # Hitung ukuran data
    datasize = len(message)
    datasize = struct.pack("<I", datasize)
    #kirimkan data
    message = message.encode('ascii')
    #Tambahkan ukuran message berikut konten ke sebuah variable
    data = datasize + message
    conn.send(data)

def recvalldata(conn):
    #Baca dulu ukuran datanya
    datasize = conn.recv(4)
    #Unpack untuk membaca ukuran message
    datasize = struct.unpack("<I", datasize)[0]
    #Baca konten message
    message = conn.recv(datasize)
    message = message.decode('ascii')
    return message
