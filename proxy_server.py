# Needs to be made forking. Check out https://docs.python.org/3.4/library/multiprocessing.html?highlight=process

#!/usr/bin/env python3
import socket
import time

# Needs to be made forking. Check out https://docs.python.org/3.4/library/multiprocessing.html?highlight=process

#define address & buffer size

# Should this host be google?
HOST = "www.google.com"
PORT = 8001
BUFFER_SIZE = 1024

def main():
    # Recall that this is how a TCP socket is created
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        # I think this is how we instruct the os to reuse the same bind port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # This time, bind the TCP socket to Google. Clients can connect to this proxy server
        # and GET from Google without having to connect directly to Google! 
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            #recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            print(full_data)
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

if __name__ == "__main__":
    main()

# Send a get request to the proxy server and see if you get the Google homepage back