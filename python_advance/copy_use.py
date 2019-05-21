import copy

a= [1,2,3]
b = a
print(id(a))
print(id(b))
c = copy.copy(a)
print(id(c))