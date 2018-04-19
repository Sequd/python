
def test_function():
    """I print 'Hello, world!'"""
    print("Hello, world!")

    maxValue = 250
    startPoint = maxValue / 4
    for i in range(0, maxValue, 1):
        currentPoint = i / 2 + startPoint
        print('{0} = {1}'.format(i, currentPoint))


test_function()