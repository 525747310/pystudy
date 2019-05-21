a = [1,2,3]
b = [4,5,6]
print(zip(a,b))
print(list(zip(a,a,b)))
for i,j,k in zip(a,a,b):
    print(i/2,2*j,k)