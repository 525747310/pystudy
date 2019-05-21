import numpy as np
'''a = np.array([10,20,30,40])
b = np.arange(4)

c = a - b
print(c)
d = a + b
print(d)

print(c**2)


print(np.sin(d))

print(a==10)'''

a = np.array([[1,1],
              [0,1]])
b = np.arange(4).reshape(2,2)

print(a)
print(b)

print(a*b)   #对应位置相乘
print(np.dot(a,b))   #矩阵乘法


d = np.random.random((2,3))
print(d)

print(np.sum(d,axis=0))
print(np.min(d,axis=1))   #1对行进行操作
print(np.max(d))