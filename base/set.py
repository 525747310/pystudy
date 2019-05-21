a = [1,1,2,2,1,4]

print(set(a))
b = set(a)
b.add(5)   #添加元素
b.remove(4)
#b.clear()   #清除
b.discard(6)  #去掉元素
print(b)