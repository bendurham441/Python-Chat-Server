import socket

HOST = '127.0.0.1'
PORT = 8000
SOCKET_LIST = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen
SOCKET_LIST.append(s)

while True:
  msg = input('Enter your message: ')
  
  for socket in SOCKET_LIST:
    new_sock, addr = s.accept()
    SOCKET_LIST.append(new_sock)
    
    if socket == s:
      data = s.recv()
      print(data)
    
    else:
      socket.send(msg)
