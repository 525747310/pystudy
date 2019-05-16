import torch
import numpy as np

np_data = np.arange(6).reshape((2,3))
torch_data = torch.from_numpy(np_data)   #从numpy数据变为torch数据

print(np_data)
print(torch_data)

tensor2array = torch_data.numpy()   #torch数据变为numpy数据
print(tensor2array)

data = [-1, -2, 1, 2]
torch_data = torch.FloatTensor(data)
print(torch.mean(torch_data))

data = [[-1, -2], [1, 2]]
torch_data = torch.FloatTensor(data)
print(torch.mm(torch_data,torch_data))

