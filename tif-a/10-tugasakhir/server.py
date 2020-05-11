import threading
import socket


class Server:
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        while True:
            try:
                self.port = int(input("Masukkan port yang ingin digunakan =>"))

                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.bind((self.ip, self.port))

                break
            except socket.error:
                print("Binding gagal")

        self.koneksi = []
        self.accept_conns()

    def accept_conns(self):
        self.sock.listen(100)

        print("Menggunakan IP   = "+self.ip)
        print("Menggunakan port = "+str(self.port))

        while True:
            conn, addr = self.sock.accept()

            self.koneksi.append(conn)

            threading.Thread(target=self.handle_client,
                             args=(conn, addr,)).start()

    def broadcast(self, socket, data):
        for client in self.koneksi:
            if client != self.sock and client != socket:
                try:
                    client.send(data)
                except socket.error:
                    pass

    def handle_client(self, conn, addr):
        while True:
            try:
                data = conn.recv(1024)
                self.broadcast(conn, data)
            except socket.error:
                print('client putus')
                conn.close()


server = Server()
