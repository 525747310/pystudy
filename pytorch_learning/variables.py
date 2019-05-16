import torch
from torch.autograd import Variable   #使用变量要用这个包


tensor = torch.FloatTensor([[1,2],[3,4]])
variable = Variable(tensor,requires_grad=True)    #requires_grad=True通过variables搭建计算图纸，使节点计算反向传播的梯度

print(variable)

t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable*variable)

print(t_out)
print(v_out)

v_out.backward()   #让v_out反向传播
print(variable.grad)   #看variable的梯度属性
print(variable.data)  #看variable的data属性

print(variable.data.numpy())