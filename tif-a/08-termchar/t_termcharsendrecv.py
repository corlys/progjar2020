
def sendalldata(conn, message):
    #Tambahkan terminator character di akhir message
    message = message+"\r\n"
    #Kirimkan messagenya
    conn.send(message.encode('ascii'))

def recvalldata(conn):
    data = ""
    while True :
        #buffer untuk penampung sementara
        buffer = conn.recv(20)
        buffer = buffer.decode('ascii')
        if "\r\n" in buffer:
            #bersihkan buffer dari terminator
            buffer = buffer.replace("\r\n", "")
            #Tambahkan buffer ke dalam variable data
            data = data+buffer
            return data
        data = data + buffer
        