import numpy as np
list_a = [[1,2,3],
          [4,5,6]]

array_a = np.array(list_a)   #处理为numpy数组

print(array_a)

print('number of dim:',array_a.ndim)  #维度
print('shape:',array_a.shape)   #形状
print('size:',array_a.size)   #大小

a = np.array([[2,23,4],
              [2,3,4]],dtype=np.int64)   #直接用列表创建array
print(a.dtype)
print(a)

b = np.zeros((3,4))
print(b)

c = np.ones((2,3),dtype=np.int16)
print(c.dtype)
print(c)

d = np.empty((2,3))   #生成一个十分接近与0的矩阵
print(d)

e = np.arange(10,20,2)   #类似python的range
print(e)

f = np.arange(12).reshape((3,4))  #从0到11
print(f)

g = np.linspace(1,10,5).reshape((1,5))   #生成5段
print(g)




