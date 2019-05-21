a = ['yang','can']
print(len(a))
print(a[0])

a.append('song')   #最常用
print(a)

#也可以把元素插入到指定的位置，比如索引号为1的位置：
a.insert(1,'chen')
print(a)

#要删除list的元素，用pop()方法：
a.pop(2)
print(a)

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
a[2] = 'huancg'
print(a)

#a.remove('can')
#print(a)

print(a.index('chen'))   #打印索引
print(a.count('chen'))   #计数

a.sort(reverse=True) #排序
print(a)

mul_a = [[1,2,3],
         [3,4,5],
         [6,7,8]]
print(mul_a[0][1])