# Set up the NN
import torch.nn as nn
import torch.nn.functional as F
import torch

class Net(nn.Module):

        def __init__(self):
                super(Net, self).__init__()
                self.fc1 = nn.Linear(1080,540)
                self.fc2 = nn.Linear(540,200)
                self.fc3 = nn.Linear(200,50)
                self.fc4 = nn.Linear(50,8)
                #self.fc4 = nn.Linear(10,6)

        def forward(self, x):
                x = torch.relu(self.fc1(x))
                x = torch.relu(self.fc2(x))
                x = torch.relu(self.fc3(x))
                #x = F.tanh(self.fc3(x))
                #x = torch.exp(self.fc4(x))
                x = torch.exp(self.fc4(x))
                #x = self.fc3(x)
                return x

