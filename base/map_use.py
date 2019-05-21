fun = lambda x,y:x+y
a = fun(2,3)
print(a)
map(fun,[1],[2])
b = list(map(fun,[1,3],[2,5]))   #类似zip
print(b)
