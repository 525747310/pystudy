class Calculator:
    name = 'yiy'
    price = 18
    def __init__(self,name,price,height,weigth):
        self.name = name
        self.add(1,2)


    def add(self,x,y):   #self实例属性
        result = x+y
        print(result)




cal = Calculator('caso',17,10,5)
print(cal.name)
cal.add(1,2)
print(Calculator.name)