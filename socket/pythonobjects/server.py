import socket
import pickle
from product import Product


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 4571))
    s.settimeout(5)

    python_dict = {"a": 1, "b": 2}
    pickled_dict = pickle.dumps(python_dict)
    custom_object = Product("P024", "Torch", 13)
    pickled_obj = pickle.dumps(custom_object)

    try:
        s.listen(9)

        print("The server is up. Listening for connections....")

        client, address = s.accept()
        print("connection to ", address, " established")
        print("client object: ", client)

        # client.send(bytes(str(python_dict), "utf-8"))
        # client.send(bytes(str(custom_object), "utf-8"))

        client.send(pickled_dict)
        import time

        time.sleep(1)

        client.send(pickled_obj)
    except socket.timeout:
        print("timeout happened")
