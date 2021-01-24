#!/usr/bin/env python3
import socket
import time

# Needs to be made forking. Check out https://docs.python.org/3.4/library/multiprocessing.html?highlight=process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    # Recall that this is how a TCP socket is created
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        # I think this is how we instruct the os to reuse the same bind port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # bind the TCP socket to its local address, so that clients can use the address in
        # order to connect to it as a remote server.
        s.bind((HOST, PORT))
        # set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            #recieve data
            full_data = conn.recv(BUFFER_SIZE)
            print(full_data)
            # wait a bit
            time.sleep(0.5)
            # send it back
            conn.sendall(full_data)
            # closes after receiving and sending back one byte
            conn.close()

if __name__ == "__main__":
    main()
