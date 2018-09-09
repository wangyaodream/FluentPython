import socket

sk = socket.socket()
ip_port = ('127.0.0.1',9999)

conn = sk.accept()

