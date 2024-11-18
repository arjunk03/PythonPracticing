import multiprocessing


# Manager  class will enable us to share python data types acrossss processes
# the shaered variables are limited to some types but here we can handle more data types
def get_data(data_list):
    for data in data_list:
        print("name: %s \n Score : %d \n : " % (data[0], data[1]))


def append_data(new_data, data_list):
    data_list.append(new_data)

    print("new data appended")


db = [("arjun", 24), ("Raj", 24), ("Tes", 25)]
new_data = ("Jess", 26)

p1 = multiprocessing.Process(target=append_data, args=(new_data, db))
p2 = multiprocessing.Process(target=get_data, args=(db,))

p1.start()
p1.join()


p2.start()
p2.join()
print("final data :", db)


with multiprocessing.Manager() as manager:
    db = manager.list([("arjun", 24), ("Raj", 24), ("Tes", 25)])
    new_data = ("Jess", 26)

    p1 = multiprocessing.Process(target=append_data, args=(new_data, db))
    p2 = multiprocessing.Process(target=get_data, args=(db,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print("data available to the manager :", db)
