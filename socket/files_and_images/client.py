import socket
import pickle


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 4571))

    # custom_file = open("client_files/received_file.txt", "wb")
    with open("client_files/received_image.jpeg", "wb") as custom_file:
        while True:
            msg = s.recv(40960)

            if not msg:
                print("No message: closing the connection")
                break
            print(type(msg))
            # print("Message from server : ", msg.decode("utf-8"))
            # print("Type of Message from server : ", type(msg))

            custom_file.write(msg)
