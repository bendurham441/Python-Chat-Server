import socket
import sys
import select

def chat_client():
  if (len(sys.argv) < 5):
    print("Usage: python client.py <hostname> <port> <nick_name>")
    sys.exit()
    
    host = sys.argv[1]
    port = sys.argv[2]
    uname = sys.argv[3]
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    
    try:
      s.connect((host, port))
      
    except:
      print("Not able to connect")
    
    print("Connected to server")
    
    while True:
      socket_list = [sys.stdin, s]
      read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
      for sock in read_sockets:
        if sock == s:
          data = sock.recv(1024)
      
          if not data:
            print("Disconnected from server")
            sys.exit()
          else:
            sys.stdout.write(data)
            sys.stdout.write("[Me :]")
        else:
          msg = sys.stdin.readline()
          msg = '[ ' + uname + ': ]' + msg
          s.send(msg)
          sys.stdout.write('[Me :]')
if __name__ == "__main__":
  sys.exit(chat_client())
