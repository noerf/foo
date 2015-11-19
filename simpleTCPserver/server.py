import socket

port = input("Port: ")  
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((socket.gethostname(), int(port)))
s.bind(("", int(port)))

while 1:
  s.listen(1)

  conn, addr = s.accept()
  print("connected to:", addr)
  
  while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("[%s] %s" % (addr[0], data))
  conn.close()
  print("connection closed")

conn.close()

