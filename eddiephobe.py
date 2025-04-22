import torch

def prod():
    x = torch.rand(1, 5)
    y = 10 * torch.rand((5, 12))
    return torch.matmul(x, y)

print(prod())