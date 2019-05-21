X = 100   #全局变量



def fun():
    global b    #定义全局变量
    b = 10
    a = 10
    print(a)
    return a + 100

print(fun())
print(b)