# CI Pipeline Diagram

```mermaid
flowchart TD
    A[Push to main or tag] --> B[Checkout code]
    B --> C[Set up Python]
    C --> D[Install dependencies]
    D --> E[Run Tests]
    E --> F[Log in to Docker Hub]
    F --> G[Build Docker Image]
    G --> H[Push Image to Docker Hub]
