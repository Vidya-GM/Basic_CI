# This is just a simple example to try github actions

def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def multiply(a, b):
    return a*b


def simple_eq(a, b):
    x = add(a, b)
    y = sub(a, b)
    result = x+2*y
    return result


print("Test resloving conflicts on branch, and actions")