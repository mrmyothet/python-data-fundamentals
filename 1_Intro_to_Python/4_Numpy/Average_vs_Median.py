import numpy as np

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
age = np.round(np.random.normal(28, 5, 5000), 0)

np_baseball = np.column_stack((height, weight, age))
print(np_baseball)

np_height_in = np_baseball[:,0]

print(np.mean(np_height_in))
print(np.median(np_height_in))

# Explore the baseball data

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))