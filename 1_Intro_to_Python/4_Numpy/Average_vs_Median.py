import numpy as np

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
age = np.round(np.random.normal(28, 5, 5000), 0)

np_baseball = np.column_stack((height, weight, age))
print(np_baseball)

np_height_in = np_baseball[:,0]

print(np.mean(np_height_in))
print(np.median(np_height_in))