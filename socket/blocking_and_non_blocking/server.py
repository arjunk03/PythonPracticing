from datetime import date, datetime
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 4571))
    s.listen(5)
    print("The server is up and listening", "\n")

    client, address = s.accept()
    print("Connection to ", address, " established", "\n")
    print("client obj: ", client, "\n")

    start = datetime.now()

    data = client.recv(1024)
    total_recvd_size = len(data)
    print("data :", data)

    i = 1
    while data:
        print(data.decode())

        data = client.recv(1024)

        total_recvd_size += len(data)
        i += 1

    print("all data received in %i batches" % i)
    client.close()

    end = datetime.now()
    print("Duration : ", end - start)

    print("totl size received :", total_recvd_size)
