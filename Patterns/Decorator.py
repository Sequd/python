def m1():
    print("Main method 'm1'")


def decorator_method(m):
    def inner():
        print("begin decorator")
        if m is not None:
            m()
        print("end decorator")

    return inner


print("without decoration")
m1()
print("decoration")
m1 = decorator_method(m1)
m1()
