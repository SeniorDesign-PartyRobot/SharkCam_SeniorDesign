# runs w web application, acts as "client" to pi's "server"

# import modules
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.8.207' # ip address of pi
port = 8080 #make sure this matches the pi, obvs

print(host)
s.connect((host, port))
raw = s.recv(1024) # receive bytes
decoded = raw.decode('utf-8') # decode as string
print(decoded) 
s.close() # close socket when done
exit() # kill program

