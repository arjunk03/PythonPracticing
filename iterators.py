def get_list_of_num(n):
    for val in range(1, n):
        yield val


t = get_list_of_num(10)

for val in t:
    print(val)

# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
