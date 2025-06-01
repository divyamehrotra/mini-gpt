# GPT model 

import torch.nn as nn

class SimpleGPT(nn.Module):
    def __init__(self, config):
        super().__init__()
        print("Model initialized with config:", config.__dict__)

    def forward(self, x):
        return x
