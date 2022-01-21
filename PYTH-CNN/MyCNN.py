from torch import nn
import torch.nn.functional as F

class MyNet(nn.Module):
    def __init__(self): #istanciramo objekt MyNet clase
        super().__init__()

        self.conv1 = nn.Conv2d(1, 10, kernel_size=(5,5), padding=2)
        self.pool = nn.MaxPool2d(kernel_size=(2,2)) #kernel size moze biti i samo jedan broj
        self.conv2 = nn.Conv2d(10, 20, kernel_size=(5,5), padding=2)
        self.fc1 = nn.Linear(in_features=(20*7*7), out_features=50) #in features je broj 980
        self.fc2 = nn.Linear(in_features=50, out_features=10)

    def forward(self, x):   # x je batch slika
        x = self.conv1(x)
        x = F.relu(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = self.pool(x)
        x = x.view(-1, 980) # -1 znaci da ce si sam batch prilagoditi broj slika
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)

        return x


