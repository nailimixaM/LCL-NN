# Set up the NN
import torch.nn as nn
import torch.nn.functional as F
import torch

class Net(nn.Module):

        def __init__(self):
                super(Net, self).__init__()
                self.fc1 = nn.Linear(800,600)
                self.fc2 = nn.Linear(600,400)
                self.fc3 = nn.Linear(400,100)
                self.fc4 = nn.Linear(100,6)
                #self.fc4 = nn.Linear(10,6)

        def forward(self, x):
                x = torch.relu(self.fc1(x))
                x = torch.relu(self.fc2(x))
                x = torch.relu(self.fc3(x))
                #x = F.tanh(self.fc3(x))
                x = torch.exp(self.fc4(x))
                #x = self.fc4(x)
                return x

