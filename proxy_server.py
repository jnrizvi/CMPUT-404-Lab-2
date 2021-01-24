# Needs to be made forking. Check out https://docs.python.org/3.4/library/multiprocessing.html?highlight=process
# Code adapted from TA's echo_server.py

#!/usr/bin/env python3
import socket
import time
import sys

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

#get host information
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

#send data to server
def send_data(serversocket, payload):
    print("Sending payload")    
    try:
        serversocket.sendall(payload.encode())
        # serversocket.sendall(payload)
    except socket.error:
        print ('Send failed')
        sys.exit()
    print("Payload sent successfully from the proxy server")

def main():
    # Recall that this is how a TCP socket is created
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        # I think this is how we instruct the os to reuse the same bind port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        s.bind((HOST, PORT))
        s.listen(2)
        
        # # I'm unable to connect to google for some reason
        # google_ip = get_remote_ip("www.google.com")
        # google_port = 80

        # s.connect((google_ip, google_port))
        # print (f'Proxy server Connected to www.google.com on ip {google_ip}')

        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            # recieve a message from a connected proxy_client
            full_data = conn.recv(BUFFER_SIZE)
            print(full_data)

            # Sends the message received from a connected proxy_client to google
            send_data(s, full_data.decode("utf-8"))
            # s.send(full_data)

            # wait a bit
            time.sleep(0.5)
            # send back to the connected proxy_client
            conn.sendall(full_data)
            conn.close()

if __name__ == "__main__":
    main()

# Send a get request to the proxy server and see if you get the Google homepage back