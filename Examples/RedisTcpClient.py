import socket

TCP_IP = 'localhost'
TCP_PORT = 6379
BUFFER_SIZE = 1024
MESSAGE = "HEAD / HTTP/1.1\r\nHost: webcode.me\r\nAccept: text/html\r\n\r\n"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (TCP_IP, TCP_PORT)
sock.connect(server_address)
print('send')
sock.sendto('PING'.encode('utf8'), server_address)
print('recived')
data, address = sock.recvfrom(4096)
data = data.decode('utf8')
print('close')
sock.close()

print("received data:", data)
