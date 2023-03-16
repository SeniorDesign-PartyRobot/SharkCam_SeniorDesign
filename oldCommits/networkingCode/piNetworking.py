# Pi acts as "server," device accessing application acts as "client"

# import modules
import socket

# init and bind socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.8.207'
port = 8080 # arbitrary
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # close port after program closes
s.bind((host, port))

#listen for client connection
print(host)
try:
    s.listen(1) #only allows one connection at a time
except:
    print("not listening")
finally:
    print("listening")

while True:
    c, addr = s.accept() #establish connection
    print('connection from ',c, ' at ', addr)
    c.send(str.encode('connected'))
    c.close() # close connection
    exit() # kill program

