def triangle(height, base):
    return 0.5 * height * base


def rectangle(length, breadth):
    return length * breadth


def square(side):
    if side == 3:
        raise ValueError("error")
    return side**2
