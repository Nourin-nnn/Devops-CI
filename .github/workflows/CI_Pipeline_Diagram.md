# CI Pipeline for Docker App

This project implements a Continuous Integration (CI) pipeline for a Docker application using GitHub Actions.

## CI Pipeline Diagram

```mermaid
flowchart TD
    A[Push to main or tag] --> B[Checkout code]
    B --> C[Set up Python]
    C --> D[Install dependencies]
    D --> E[Build Docker Image]
    E --> F[Log in to Docker Hub]
    F --> G[Push Image to Docker Hub]
    G --> H[Checkout code from Devops-CD]
    H --> I[Modify image tag in deployment file]
    I --> J[Push changes to Devops-CD]
