# GlimpseGAN

GlimpseGAN: Generating lifelike images using PyTorch-powered Generative Adversarial Networks (GANs)

## Overview

GlimpseGAN is an exciting project that explores the world of Generative Adversarial Networks (GANs) with PyTorch, a powerful deep learning framework. GANs are a class of deep learning models that learn to generate synthetic data, such as lifelike images, by training two competing neural networks: a generator and a discriminator. This project showcases the beauty and potential of AI technology for creative image synthesis.

## Project Structure

The project directory is structured as follows:

- **`generator/`:** Contains the implementation of the generator model, responsible for generating lifelike images.
- **`discriminator/`:** Contains the implementation of the discriminator model, responsible for distinguishing real images from generated ones.
- **`train_gan.py`:** Implements the GAN training loop and model evaluation, including hyperparameter settings and training configurations.

## Installation

To set up and run the GlimpseGAN project locally, follow these steps:

1. **Clone** the GitHub repository:

```bash
git clone https://github.com/your-username/GlimpseGAN.git
cd GlimpseGAN
```

2. **Install** the required Python packages:
```bash
pip install -r requirements.txt
```

3. **Run** the GAN training script:
```bash
python train_gan.py
```

## Usage

Once the GAN model is trained, you can use it to generate lifelike images. GlimpseGAN has been Dockerized for easy deployment and reproducibility. Additionally, you can deploy the Docker image on a Kubernetes cluster for scalable image generation.

## Dockerized Usage

To generate images using the Dockerized GlimpseGAN, follow these steps:

1. Ensure you have Docker installed on your local machine. You can install it from here: [Docker Install](https://www.docker.com/products/docker-desktop/)

2. Pull the pre-built Docker image from Docker Hub:
```bash
docker pull sabdulmajid/glimpse-gan:latest
```

3. Run the Docker container and mount the output directory for generated images:
```bash
docker run --rm -v $(pwd)/generated_images:/app/generated_images sabdulmajid/glimpse-gan:latest python generate_images.py --num_images 10 --output_dir /app/generated_images/
```
This command generates 10 lifelike images and saves them in the `generated_images/` directory within your current working directory.

## Kubernetes Deployment

To deploy GlimpseGAN on a Kubernetes cluster, you need to have a working Kubernetes environment set up, including ```kubectl``` configured to connect to your cluster.

1. Ensure your Docker image is available on a container registry accessible to your Kubernetes cluster. You can push your locally built Docker image to a container registry or use a public registry like Docker Hub.

2. Create a Kubernetes deployment YAML file, let's call it `glimpse-gan-deployment.yaml` and define the deployment configuration:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: glimpse-gan-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: glimpse-gan
  template:
    metadata:
      labels:
        app: glimpse-gan
    spec:
      containers:
      - name: glimpse-gan-container
        image: your-username/glimpse-gan:latest
        ports:
        - containerPort: 80

```