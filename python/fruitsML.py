import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models

device = torch.device('cpu')

transform = transforms.Compose([
    transforms.Resize((100, 100)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

train_data = datasets.ImageFolder(root='Fruits Classification/train', transform=transform)
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)


class FruitClassifier(nn.Module):
    def __init__(self):
        super(FruitClassifier, self).__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding=1),  # input channels (RGB=3), output channels=16
            nn.ReLU(),
            nn.MaxPool2d(2, 2),  # halve the size: 100x100 -> 50x50



            nn.Conv2d(16, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),  # 50x50 -> 25x25



            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),  # 25x25 -> 12x12
        )

        self.fc_layers = nn.Sequential(
            nn.Flatten(),  # flatten the tensor
            nn.Linear(64 * 12 * 12, 128),
            nn.ReLU(),
            nn.Linear(128, 5)  # 5 fruits = 5 output classes
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x


model = FruitClassifier().to(device)

# 4. Loss and Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

epochs = 50
for epoch in range(epochs):
    running_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print(f"Epoch {epoch+1}/{epochs}, Loss: {running_loss/len(train_loader)}")

print("Training complete.")


# ----- Testing
# 1. Load the test data
test_data = datasets.ImageFolder(root='Fruits Classification/test', transform=transform)
test_loader = DataLoader(test_data, batch_size=32, shuffle=False)

# 2. Set model to evaluation mode
model.eval()

# 3. Turn off gradient calculation (saves memory and speed)
correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)  # get the index of the highest score (class prediction)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total
print(f"Test Accuracy: {accuracy:.2f}%")

torch.save(model.state_dict(), 'fruit_classifier.pth')
print("Model saved successfully!")


