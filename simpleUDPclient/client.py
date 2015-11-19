import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("IP: ")
port = input("Port: ")  
msg = input("Message: ")

s.sendto(msg.encode('utf-8'), (ip, int(port))) 
s.close()

