# foo = 1
#
#
# def func():
#     foo = 2
#
#     # creates a new variable foo in local scope, global foo is not affected
#     print(foo)
#     # prints 2
#     # global variable foo still exists, unchanged:
#     print(globals()["foo"])  # prints 1
#     print(locals()["foo"])  # prints 2
#
#
# func()

foo = 1


def func():
    # In this function, foo is a global variable from the beginning
    foo = 7
    # global foo is modified
    print(foo)  # 7
    print(globals()["foo"])
    global foo
    print(foo)


# 7
# this could be anywhere within the function
# 7
func()
