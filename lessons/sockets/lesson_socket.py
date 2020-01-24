import socket

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the port
server_address = ("localhost", 10000)
print("Starting up on {} port {}".format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    print("\nWaiting for a new connection...")
    connection, client_address = sock.accept()
    try:
        print("connection from", client_address)

        # receive data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print("received {!r}".format(data))
            if data:
                print("Sending data back to the client...")
                connection.sendall(data)
            else:
                print("Did not receive any data from", client_address)
                break
    finally:
        print("Closing current connection")
        connection.close()
