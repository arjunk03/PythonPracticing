class ObjectCounter:
    num_instances = 0

    def __init__(self):
        type(self).num_instances += 1
        print("Number of instances is ", type(self).num_instances)


ObjectCounter()
ObjectCounter()
ObjectCounter()
ObjectCounter()
ObjectCounter()
a = ObjectCounter()
print(a.__dict__)
print(ObjectCounter.__dict__)
