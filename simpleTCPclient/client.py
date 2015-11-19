import socket

ip = input("IP: ")
port = input("Port: ")  
msg = input("Message: ")

BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, int(port)))
s.send(msg.encode('utf-8'))

while msg != "exit":
  msg = input("Message: ")
  s.send(msg.encode('utf-8'))

s.close()

