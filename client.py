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
    
