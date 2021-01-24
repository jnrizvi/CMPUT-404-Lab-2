# f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'

# Proxy acts as a middleman between client and server

# Client should connect, send something to the server, the server sends the same thing back. 
# That's the "echo" part. Once it finishes recieving it back, it should close.

# from multiprocess import Process

# allow for multiple processes with a Process daemon