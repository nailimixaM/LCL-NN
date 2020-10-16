# Set up the NN
import torch.nn as nn
import torch.nn.functional as F
import torch

class Net(nn.Module):

        def __init__(self):
                super(Net, self).__init__()
                self.fc1 = nn.Linear(900,700)
                self.fc2 = nn.Linear(700,500)
                self.fc3 = nn.Linear(500,300)
                self.fc4 = nn.Linear(300,100)
                self.fc5 = nn.Linear(100,6)

        def forward(self, x):
                x = F.relu(self.fc1(x))
                x = F.relu(self.fc2(x))
                x = F.relu(self.fc3(x))
                x = F.relu(self.fc4(x))
                x = torch.sigmoid(self.fc5(x))
                return x

