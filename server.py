"""A simple chat program based greatly upon susmithHCK's neuron

It doesn't have a lot of functionality, but it will in the future.

This is just the server part of the program, which in this case just recieves and distributes messages.

Example:
  To use this, you simply need to type this into your terminal::
    
    $ python server.py
    
TODO:
  * Add channel functionality
  * Add private message functionality
"""

import socket
import select

  HOST = '127.0.0.1' # IP address of server
  PORT = 8000        # Port for server
  SOCKET_LIST = []   # List of clients
  
def chat_server():
  """Function that includes all of the server functionality
  
  Includes defining the server, handling and distributing the messages
  """
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # The definition of the socket
  server_socket.bind((HOST, PORT))                                  # Binding of the socket to the defined host and port
  # socket.setsockopt()
  server.listen(10)                                                 # Sets how many connections the server can accept
  
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
