import socket 

port = input("Port: ")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try: 
  s.bind(("", int(port))) 
  while True: 
    data, addr = s.recvfrom(1024) 
    print("[%s] %s" % (addr[0], data))
finally: 
  s.close()
