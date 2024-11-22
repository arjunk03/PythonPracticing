import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    client_name = input("Enter your name:")

    s.connect((socket.gethostname(), 4571))
    s.send(client_name.encode())

    server_name_raw = s.recv(1024)
    server_name = server_name_raw.decode()
    print(f"you have connected to the server {server_name}")

    while True:
        message_recv = s.recv(1024)
        message_recv = message_recv.decode()
        print(server_name, " - ", message_recv)

        send_message = input(client_name + " - ")
        s.send(send_message.encode())

        if send_message.lower() == "bye":
            break
