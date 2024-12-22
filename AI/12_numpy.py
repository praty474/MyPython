import numpy as np

a = np.array([[1, 2, 3], [3, 4, 5]])
b = np.array([[5, 6], [7, 8], [3, 5]])

c = np.dot(a,b) # this is to multiply matrices

d = np.transpose(a) #transpose

print(c)
print(d)

e = np.sqrt(a) #this is square root

print(e)


num = [4, 5, 6]

mean = np.mean(num) #mean
median = np.median(num)
min = np.min(num)

print(mean)
print(median)
print(min)