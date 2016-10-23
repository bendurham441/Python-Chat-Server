import socket
import sys
import select

  HOST = '127.0.0.1'
  PORT = 8000
  SOCKET_LIST = []
  
def chat_server():
  
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind((HOST, PORT))
  # socket.setsockopt()
  server.listen(10)
  
  SOCKET_LIST.append(server_socket)
  
  while True:
    
    ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [], [], 0)
    
    for sock in ready_to_read:
      
      if sock == server_socket:
        
        sockfd, addr = server_socket.accept()
        SOCKET_LIST.append(sockfd)
        print("Client (%s, %s) has connected")
        broadcast(server_socket, sockfd, "[ %s:%s ] has joined\n" % addr)
        
      else:
        try:
          data = sock.recv(1024)
          
          if data:
            
            broadcast(server_socket, sock, "\r" + data)
          
          else:
            
            if sock in SOCKET_LIST:
              SOCKET_LIST.remove(sock)
              
            broadcast(server_socket, sock, "( %s, %s ) is offline\n" % addr)
        
        except:
          broadcast(server_socket, sock, "( %s, %s ) is offline\n" % addr)
          continue
          
    server_socket.close()
          
def broadcast(server_socket, sock, message):
  
  for socket in SOCKET_LIST:
    
    if socket != server_socket and socket != sock:
      
      try:
      
        socket.send(message)
      
      except:
        
        socket.close()
        
        if socket in SOCKET_LIST:
          SOCKET_LIST.remove(socket)
        
if __name__ == "__main__":
  
  chat_server()
