import torch
import torch.nn as nn
import torch.optim as optim
from torchvision.datasets import MNIST
from torchvision import transforms
from torch.utils.data import DataLoader


torch.manual_seed(42)

latent_dim = 100
img_shape = 28 * 28
epochs = 100
batch_size = 128

generator = Generator(latent_dim, img_shape)
discriminator = Discriminator(img_shape)

adversarial_loss = nn.BCELoss()

optimizer_G = optim.Adam(generator.parameters(), lr=0.0002, betas=(0.5, 0.999))
optimizer_D = optim.Adam(discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))

dataset = MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

for epoch in range(epochs):
    for i, (real_images, _) in enumerate(dataloader):
        batch_size = real_images.size(0)

        valid = torch.ones(batch_size, 1)
        fake = torch.zeros(batch_size, 1)
        