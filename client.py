import socket

client = socket.socket()
client.connect(("localhost", 9090))
data = client.recv(2048)
print(data.decode())
