import torch
from torchvision.datasets import MNIST
from torchvision import transforms
from torchvision.transforms import ToTensor, Resize
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
from MyCNN import MyNet
from torch import nn

Learning_Rate = 0.001
batch_size = 32
device = "cuda" if torch.cuda.is_available() else "cpu"
num_epochs = 20

transform = transforms.Compose([Resize((28,28)), ToTensor()]) #augumentacija

mnist_dataset_train = MNIST(root="data", train=True, transform=transform, download=True)

mnist_dataset_val = MNIST(root="data", train=False, transform=transform, download=True)


sample = mnist_dataset_train[0]

# fig, axes = plt.subplots(3)
# for i in range(3):
#     image, label = mnist_dataset_train[i]
#     image = image.squeeze()
#     axes[i].imshow(image, cmap = "gray")
#     axes[i].set_title(str(label))
#
# plt.show()


mnist_dataloader_train = DataLoader(mnist_dataset_train, batch_size=batch_size, shuffle=True)
mnist_dataloader_val = DataLoader(mnist_dataset_val, batch_size=batch_size, shuffle=True)

model = MyNet().to(device)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), Learning_Rate)


def train(train_dataloader, model, loss_fn, optimizer, current_epoch):
    dataset_size = len(train_dataloader.dataset)
    running_loss = 0
    for batch_iter, (images, labels) in enumerate(train_dataloader):
        images, labels = images.to(device), labels.to(device)

        predictions = model(images)
        loss = loss_fn(predictions, labels)

        optimizer.zero_grad() #stavljmo gradijente(promjene) na 0 inace bi se zbrajali
        loss.backward()  #izracunava gradijente
        optimizer.step()

        running_loss += loss.item()

        if batch_iter % 100 == 0:
            average_loss = running_loss / 100
            current_itteration = batch_iter * len(labels)
            print("[%d] [%d / %d] Loss: %.3f" %(current_epoch, current_itteration, dataset_size, average_loss))
            running_loss = 0

for epochs in range(num_epochs):
    train(mnist_dataloader_train, model, loss_fn, optimizer, epochs)    #mi definirano funkcije train i validate
    #validate()