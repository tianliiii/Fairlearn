import torch
x = torch.rand(2,3,4)
print(x.permute(1,2,0).shape)
x2 = x.permute(1,2,0)
print(x2.shape)
x = x.flatten()
x2 = x2.flatten()
print(x)
print(x2)