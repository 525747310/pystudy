import matplotlib.pyplot as plt  #用这个分模块即可
import numpy as np

x = np.linspace(-1,1,50)
y = x**2 + 1
plt.plot(x,y)   #作图
plt.show()   #显示图

