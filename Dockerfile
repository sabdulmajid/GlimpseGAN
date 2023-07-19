# Dockerfile

FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime

WORKDIR /app

COPY generator generator
COPY discriminator discriminator
COPY train_gan.py .
