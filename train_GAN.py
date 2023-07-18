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
        
        optimizer_G.zero_grad()
        
        z = torch.randn(batch_size, latent_dim)
        
        generated_images = generator(z)
        
        g_loss = adversarial_loss(discriminator(generated_images), valid)
        
        g_loss.backward()
        optimizer_G.step()
        
        optimizer_D.zero_grad()
        
        real_loss = adversarial_loss(discriminator(real_images.view(-1, img_shape)), valid)
        
        fake_loss = adversarial_loss(discriminator(generated_images.detach()), fake)
        
        d_loss = (real_loss + fake_loss) / 2
        
        d_loss.backward()
        optimizer_D.step()

        if (i+1) % 200 == 0:
            print(f"Epoch [{epoch+1}/{epochs}], Batch [{i+1}/{len(dataloader)}], Generator Loss: {g_loss.item():.4f}, Discriminator Loss: {d_loss.item():.4f}")

torch.save(generator.state_dict(), 'generator.pth')
torch.save(discriminator.state_dict(), 'discriminator.pth')