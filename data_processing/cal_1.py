import numpy as np

A = np.arange(2,14).reshape((3,4))

print(A)
print(np.argmin(A))
print(np.argmax(A))
print(np.mean(A))
print(A.mean())
print(np.average(A))
print(np.median(A))   #中位数
print(np.cumsum(A))
print(np.diff(A))