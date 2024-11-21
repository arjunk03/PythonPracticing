import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 4571))
    s.settimeout(5)

    try:
        s.listen(9)

        print("The server is up. Listening for connections....")

        client, address = s.accept()
        print("connection to ", address, " established")
        print("client object: ", client)

        client.send(bytes("Hello, welcome", "utf-8"))
    except socket.timeout:
        print("timeout happened")
