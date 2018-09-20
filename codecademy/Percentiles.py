import numpy as np

patrons = np.array([2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])

thirtieth_percentile = np.percentile(patrons, 25)
seventieth_percentile = np.percentile(patrons, 75)
print(thirtieth_percentile)
print(seventieth_percentile)

mid = seventieth_percentile - thirtieth_percentile
print(mid)
