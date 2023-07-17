# The script simulates a streaming socket data source.  It accepts the host and port number of 
# the connection.  It also accepts number of lines to stream per second as well as the name
# of the text to use to simulate the streaming data
#
# Parameters:
#     host: the host name or IP to bind to (e.g. localhost)
#     port: the port to listen on (e.g. 1234)
#
# Note: script makes no attempt to recover from a broken connection; restart the script.

import sys
import time
import socket

if __name__ == "__main__":
  
  # The host to connect to
  host = sys.argv[1]
  
  # The port to send
  port = int(sys.argv[2])
  
  # Time between sending
  sleeptime = 2 
  
  # 
  n = 4
  
  # Create socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host,port))
  
  # Loop to send tweets
  while(1):
    s.send(str(n)+"\n")
    time.sleep(sleeptime)
    n += 1
