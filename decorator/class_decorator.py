# import functools
#
#
# class Counter:
#     def __init__(self, start=0):
#         functools.update_wrapper(self, func)
#         self.count = start
#
#     def __call__(self):
#         self.count += 1
#         print(f" Current count is {self.count}")
#
#
# counter = Counter()
# counter()


import functools


class CountCalls:
    def __init__(self, func, nn=""):
        functools.update_wrapper(self, func)
        print("init , ", func, nn)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(args, kwargs)
        print(f"the number of calls for {
              self.func.__name__} is {self.num_calls}")
        return self.func(*args, **kwargs)


@CountCalls
def test(name):
    print(" name is ", name)


test("arjun")
