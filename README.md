# Flask Guess the Number Game

This repository contains a simple web-based "Guess the Number" game built with Flask. The application is containerized using Docker and includes a CI/CD pipeline for automated builds and deployments.

## 🎯 About The Project

This is a fun, interactive web game where the player tries to guess a randomly generated number between 1 and 100. The application keeps track of the number of guesses and provides feedback to guide the player. The entire front end is rendered from a single HTML template string within the Flask application itself.

The core application logic is in `app.py`. It uses a Flask session to store the game state, such as the secret number and the count of guesses.

## ⚙️ Getting Started

You can run this application locally for development or testing.

### Prerequisites

*   Python 3
*   Docker (optional, for running in a container)

### Running Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/aashishrrjp/flask-app.git
    cd flask-app
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    The required packages are `flask` and `gunicorn`.

3.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will be running at `http://127.0.0.1:5000`.

## 🐳 Docker Support

The application is fully containerized. You can build and run it using Docker.

1.  **Build the Docker image:**
    ```bash
    docker build -t flask-app .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 flask-app
    ```
    The application will be accessible at `http://localhost:5000`.

The `Dockerfile` uses a lightweight Python base image (`python:3.10-slim`), copies the application files, installs dependencies, and uses `gunicorn` to run the web server.

## 🚀 CI/CD Pipeline

This repository includes a GitHub Actions workflow defined in `.github/workflows/docker-build-push.yml` to automate the build and deployment process.

### Workflow Triggers

The workflow is automatically triggered on a `push` to the `main` branch if there are changes in any of the following files:
*   `app.py`
*   `requirements.txt`
*   `Dockerfile`

### Workflow Steps

1.  **Authenticate to Google Cloud:** It authenticates using a service account key stored in GitHub secrets.
2.  **Build and Push Docker Image:** It builds a Docker image, tags it with the Git commit SHA, and pushes it to the Google Artifact Registry.
3.  **Update GitOps Repository:** After a successful push, the workflow checks out a separate GitOps repository (`aashishrrjp/flask-app-deploy`). It then automatically updates the `values-dev.yaml` and `values-prod.yaml` files with the new Docker image tag and pushes the changes, triggering ArgoCD to deploy the new version.

