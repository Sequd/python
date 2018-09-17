import numpy as np

my_array = np.array([1, 2, 3, 4, 5, 6])
csv_array = np.genfromtxt('data.csv', delimiter=',')  # read array from csv file

print(csv_array)

# adding 3 to each item array
new_my_array = my_array + 3
print(new_my_array)

'''
Select items from 2-D arrays
'''

a = np.array([[32, 15, 6, 9, 14],
              [12, 10, 5, 23, 1],
              [2, 16, 13, 40, 37]])

# a[row,column]
# first index are row value
# second index are column value

# 3 row and 2 column | 16
print(a[2, 1])

# select all value in 1 column | [32 12  2]
print(a[:, 0])

# select all value in 2 row | [12 10  5 23  1]
print(a[1, :])

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

'''
Logical Operations with Arrays
'''

a = np.array([10, 2, 1, 4, 5, 3, 9, 8, 9, 7])
# [10  9  8  9  7]
print(a[a > 5])
# [10  1  9  8  9  7]
print(a[(a > 5) | (a < 2)])
