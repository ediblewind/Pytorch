import torch
import torchvision
import numpy
x = torch.rand(5,3)
print(x)
y = torch.rand(5,3)
print(y)
print(x+y)
result = torch.zeros(5,3)
torch.add(x,y,out = result)
print(result)
y = y.add_(x)
print(y)