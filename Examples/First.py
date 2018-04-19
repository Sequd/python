from math import factorial


def test_function():
    """I print 'Hello, world!'"""
    print("Hello, world!")

    maxValue = 250
    startPoint = maxValue / 4
    for i in range(0, maxValue, 1):
        currentPoint = i / 2 + startPoint
        print('{0} = {1}'.format(i, currentPoint))


t = 'Hello, world!'
print(t)
print(100. / 12)
print(round(100. / 12, 3))

print(factorial(3))

u = u"abs"  # unicode
l = [1, 2, 3]  # list
e = dict()
e['abc'] = 3.5

if True:
    print("OK")
else:
    print("NOT OK")

# range возвращает список
# xrange возвращает итератор
for i in range(2,5):
    print(i)

w = [x ** 2 for x in range(1,11) if x % 2 == 0]
print(w)


x = 0
while x < 10:
    print(x)
    x += 1