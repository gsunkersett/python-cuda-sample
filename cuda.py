import torch
import numpy as np

# This worked on alienware alpha after lot of effort
# Installed Anaconda and then PyTorch 
# https://pytorch.org/get-started/locally/#windows-anaconda
# conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

b = torch.cuda.is_available()

if b:
    print("GPU is available")
    x = torch.rand(50, 30)
    print(x)
else:
    print("GPU is not available")