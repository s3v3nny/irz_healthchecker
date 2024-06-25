import socket

client = socket.socket()
client.connect(("10.0.2.15", 9090))
data = client.recv()
print(data.decode())
