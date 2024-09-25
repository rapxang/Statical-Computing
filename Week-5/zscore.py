import numpy as np

data=np.array([2, 2, 2, 3, 1, 1, 9,8, 2, 2, 2, 3, 1, 1, 2])
mean=np.mean(data)
std=np.std(data)
threshold=3
outlier = []

print("mean of the dataset = ",mean)
print("Standard Deviation of the dataset = ",std)
for i in data:
    z=(i-mean)/std
    if z>threshold:
        outlier.append(i)
        print("outlier datats are = ",outlier)
