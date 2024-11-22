import socket
from PIL import Image


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 4571))

    serevr_name = input("Enter the server name: ")
    s.listen(9)

    print(f"The serevr: {
        serevr_name} is up. Listening for connections....")

    client, address = s.accept()
    print("connection to ", address, " established", "\n")
    print("The clint object :", client, "\n")

    client_name_raw = client.recv(1024)
    client_name = client_name_raw.decode()
    print(f"client : {client_name} has initiated a connection")

    client.send(serevr_name.encode())

    while True:
        send_message = input(serevr_name + " - ")
        client.send(send_message.encode())

        if send_message.lower() == "bye":
            break

        message_recv = client.recv(1024)
        message_recv = message_recv.decode()
        print("\t", client_name, " - ", message_recv)
