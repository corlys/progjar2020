import socket
import pyaudio
import threading


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while True:
            try:
                self.server_ip = input("Masukkan IP server   =>")
                self.server_port = int(input("Masukkan Port server =>"))
                self.sock.connect((self.server_ip, self.server_port))

                break
            except:
                print("Tidak dapat membuat koneksi ke server ... ")

        chunk_size = 1024
        audio_format = pyaudio.paInt16
        channels = 1
        rate = 20000

        self.microphone = pyaudio.PyAudio()
        self.playing_stream = self.microphone.open(
            format=audio_format,
            channels=channels,
            rate=rate,
            output=True,
            frames_per_buffer=chunk_size,
        )
        self.recording_stream = self.microphone.open(
            format=audio_format,
            channels=channels,
            rate=rate,
            input=True,
            frames_per_buffer=chunk_size,
        )

        print("Berhasil membuat koneksi ke server")

        thread_receive = threading.Thread(target=self.recv_data).start()
        self.send_data()

    def recv_data(self):
        while True:
            try:
                data = self.sock.recv(1024)
                self.playing_stream.write(data)
            except:
                pass

    def send_data(self):
        while True:
            try:
                data = self.recording_stream.read(1024)
                self.sock.sendall(data)
            except:
                pass


client = Client()
