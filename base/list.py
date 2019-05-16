a = ['杨宇雪','黄灿']
print(len(a))
print(a[0])

a.append('宋喜荣')
print(a)

#也可以把元素插入到指定的位置，比如索引号为1的位置：
a.insert(1,'陈瑞')
print(a)

#要删除list的元素，用pop()方法：
a.pop(2)
print(a)

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
a[2] = '黄灿'
print(a)