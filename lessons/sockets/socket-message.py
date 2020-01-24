import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the port where the server is listening
server_address = ("localhost", 10000)
print("connecting to {} port {}".format(*server_address))
sock.connect(server_address)

try:
    # send data
    message = b"this is our message. it is very long but will only be transmitted in chunks of 16 at a time"
    sock.send(message)
except:
    print("Some error occurred")
