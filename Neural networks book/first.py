import numpy
import matplotlib.pyplot as plt

a = numpy.zeros([3, 2])
print(a)

a[0, 0] = 1
a[1, 0] = 3
a[0, 1] = 6
a[2, 1] = 12

plt.imshow(a, interpolation="nearest")
plt.colorbar()
plt.show()
