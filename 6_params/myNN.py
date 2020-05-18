# Set up the NN
import torch.nn as nn
import torch.nn.functional as F
import torch

class Net(nn.Module):

        def __init__(self):
                super(Net, self).__init__()
                self.fc1 = nn.Linear(800,40)
                self.fc2 = nn.Linear(40,20)
                self.fc3 = nn.Linear(20,6)
                #self.fc4 = nn.Linear(20,6)
                #self.fc4 = nn.Linear(10,6)

        def forward(self, x):
                x = torch.tanh(self.fc1(x))
                x = torch.tanh(self.fc2(x))
                #x = F.tanh(self.fc3(x))
                #x = torch.exp(self.fc4(x))
                x = self.fc3(x)
                return x

