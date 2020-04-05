import socket
from d_datasizesendrecv import recvalldata, sendalldata

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("0.0.0.0", 9999))

#Listen sebanyak jumlah backlog
sock.listen(10)

while True:
    conn, client_addr = sock.accept()

    data = recvalldata(conn)
    print('datasize saat di client : '+str(len(str(data))))
    file = open('filebaruu.jpg', 'wb')
    file.write(data)
    file.close()
    
    #data = "OK "+data
    #sendalldata(conn, data)

