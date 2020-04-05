import struct

def sendalldata(conn, message):
    # Hitung ukuran data
    datasize = len(message)
    print('datasize saat di sendalldata : '+str(datasize))
    datasize = struct.pack("<I", datasize)
    #Tambahkan ukuran message berikut konten ke sebuah variable
    data = datasize + message
    conn.send(data)

def recvalldata(conn):
    #Baca dulu ukuran datanya
    datasize = conn.recv(4)
    #Unpack untuk membaca ukuran message
    datasize = struct.unpack("<I", datasize)[0]
    #Baca konten message
    print('datasize saat di recvalldata : '+str(datasize))
    message = conn.recv(datasize)
    return message
