import re


def test_function():
    """I print 'Hello, world!'"""
    print("Hello, world!")

    maxValue = 250
    startPoint = maxValue / 4
    for i in range(0, maxValue, 1):
        currentPoint = i / 2 + startPoint
        print('{0} = {1}'.format(i, currentPoint))


test_function()


def t1(data: str) -> bool:
    if len(data) < 10:
        return False

    digital = 0
    upper = 0
    lower = 0

    for c in data:
        if str.isdigit(c):
            digital += 1;
        if str.isupper(c):
            upper += 1;
        if str.islower(c):
            lower += 1;

    if digital > 0 and upper > 0 and lower > 0:
        return True
    return False
