import socket
from d_datasizesendrecv import recvalldata, sendalldata

#Inisialisasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Kirim permintaan koneksi
sock.connect(("127.0.0.1", 9999))

#Kirim data 
data = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
print('size di client : '+ str(len(data)))
sendalldata(sock, data)

#Terima balasan dari server
data = recvalldata(sock)
print(data)
