# Hybrid Cloud Auto Scaling ML System

## Architecture

```mermaid
flowchart LR

A[Locust Load Generator] --> B[Gateway Server Node.js]

B --> C[ML Server Python]

C --> D[MobileNet Model Inference]

C --> E[CPU Monitor monitor.py]

E --> F[Google Cloud VM Auto Scaling]

F --> G[Additional ML Compute Node]



## Components

### Gateway Server
- Node.js server
- Receives client image uploads
- Forwards images to ML server

### ML Server
- Python inference server
- Uses MobileNet deep learning model
- Performs image classification

### CPU Monitor
- Continuously monitors CPU usage
- Triggers scaling when CPU usage exceeds 75%

### Cloud Scaling
- Uses gcloud CLI to start cloud resources
- Automatically launches a VM on Google Cloud when load increases

### Load Testing
- Locust is used to simulate multiple users uploading images
- Helps demonstrate system auto-scaling under high load
