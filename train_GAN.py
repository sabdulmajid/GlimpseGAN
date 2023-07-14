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
