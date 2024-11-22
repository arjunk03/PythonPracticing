import socket
from PIL import Image


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 4571))
    s.settimeout(5)

    try:
        s.listen(9)

        print("The server is up. Listening for connections....")

        client, address = s.accept()
        print("connection to ", address, " established")
        print("client object: ", client)

        # custom_file = open("server_files/meditations.txt", "rb")
        # custom_data = custom_file.read(40960)
        #
        # while custom_data:
        #     client.send(custom_data)
        #     custom_data = custom_file.read(40960)
        # custom_file.close()

        with open("server_files/dog.jpeg", "rb") as image_file:
            image_batch = image_file.read(40960)

            while image_batch:
                client.send(image_batch)
                image_batch = image_file.read(40960)
                print("one batch sent to file")

        print("Custom file sent duccessfully")

    except socket.timeout:
        print("timeout happened")
