#pip3 install numpy
#pip3 uninstall numpy
#pip3 install numpy-1.9.2
#pip3 install -U numpy #升级
import time as t
from time import time,localtime    #只调用这两个功能
#from time import *
print(localtime())
print(time())

import function_def
function_def.sale_car(1,2)