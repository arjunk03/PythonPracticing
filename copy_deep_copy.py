import copy

a = 10
b = 10
print(id(a) == id(b))
b = 20
print(a, b)

a = "ttt"
b = "ttt"
print(id(a) == id(b))
b = "t"
print(a, b)


a = [1, 2, 3]
b = [1, 2, 3]
print(id(a) == id(b))
b.append("tt")
print(a, b)


a = [1, 2, 3]
b = a
print(id(a) == id(b))
b.append("tt")
print(a, b)
c = b.copy()
c.append("fffff")
print(a, b, c)


a = {"name": "arjun"}
b = a
print(id(a) == id(b))
b["age"] = 30
print(a, b)
c = b.copy()
c["num"] = 3
print(a, b, c)


a = {"name": [1, 2, 3]}
b = a
print(id(a) == id(b))
b["age"] = 30
print(a, b)
c = b.copy()
c["num"] = 3
c["name"].append("tttttttt")
print(a, b, c)


a = {"name": [1, 2, 3]}
b = a
print(id(a) == id(b))
b["age"] = 30
print(a, b)
c = copy.deepcopy(b)
c["num"] = 3
c["name"].append("tttttttt")
print(a, b, c)
