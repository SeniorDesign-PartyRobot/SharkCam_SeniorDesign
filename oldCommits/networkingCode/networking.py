# runs w web application, acts as "client" to pi's "server"

# import modules
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.8.207' # ip address of pi
port = 8080 #make sure this matches the pi, obvs

def establishConnection():
    if s.connect_ex((host,port)) == 0:
        print("Connection successful")
        return True
    else:
        print("unsuccessful connection to ", host)
        return False

def receiveBytes():
    
    try:
        raw = s.recv(1024) # receive bytes
        decoded = raw.decode('utf-8') # decode as string
        print(decoded)
        return True
    except:
        print("unsuccessful reception of bytes")
        return False

def closeAndKill():
    s.close() # close socket when done
    exit() # kill program

#### Making a "main"
def main():
    
    connectionSuccess = 0
    byteSuccess = 0

    while not (connectionSuccess and byteSuccess):
        print("Attempting to connect and receive...")
        connectionSuccess = establishConnection()
        byteSuccess = receiveBytes()
    closeAndKill() # once successful, close and kill

# call main
main()    
    

