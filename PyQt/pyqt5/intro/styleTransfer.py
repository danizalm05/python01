
import torch
# pip3 install torch
# #pip3 show torch
#pip -V
#pip 22.2.2 from C:\Users\rockman\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
from torchvision import transforms , models
#pip3 install torchvision
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

device = ("cuda" if torch.cuda.is_available() else "cpu")

model = models.vgg19(pretrained=True).features
for p in model.parameters():
    p.requires_grad = False
model.to(device)
'''
Downloading:   https://download.pytorch.org/models/vgg19-dcbb9e9d.pth 
to C:/Users/rockman/.cache/torch/hub\checkpoints/vgg19-dcbb9e9d.pth


'''


def model_activations(input, model):
    layers = {
        '0': 'conv1_1',
        '5': 'conv2_1',
        '10': 'conv3_1',
        '19': 'conv4_1',
        '21': 'conv4_2',
        '28': 'conv5_1'
    }
    features = {}
    x = input
    x = x.unsqueeze(0)
    for name, layer in model._modules.items():
        x = layer(x)
        if name in layers:
            features[layers[name]] = x

    return features


transform = transforms.Compose([transforms.Resize(300),
                                transforms.ToTensor(),
                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])


content = Image.open("content.jpg").convert("RGB")
content = transform(content).to(device)