import socket
import pickle


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 4571))

    while True:
        msg = s.recv(1024)

        if not msg:
            print("No message: ")
            break
        print(type(msg))
        # print("Message from server : ", msg.decode("utf-8"))
        # print("Type of Message from server : ", type(msg))

        unpickled_data = pickle.loads(msg)
        print("Message from server : ", unpickled_data)
        print("Type of Message from server : ", type(msg))
        print("Type of actual message : ", type(unpickled_data))

        if type(unpickled_data) != dict:
            print(unpickled_data.pid)
            print(unpickled_data.pname)
            print(unpickled_data.pprice)
