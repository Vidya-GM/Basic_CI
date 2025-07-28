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


def divide(num1, num2):
    if num2 == 0:
        raise ValueError
    return num1/num2


print("Test resloving conflicts on branch, and actions")