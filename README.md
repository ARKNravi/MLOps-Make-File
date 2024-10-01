

# MLOps Project with Docker and MLflow

This project is set up to demonstrate an MLOps workflow using Docker and MLflow. The project uses a `Dockerfile` to set up the environment and a `docker-compose.yml` file to run the main application and MLflow server.

## Project Overview

This project contains:
1. **mlops-app**: The main application that handles the machine learning workflow.
2. **MLflow**: A tool to manage the lifecycle of machine learning models, including experiment tracking and model deployment.

## Requirements

Before running the project, ensure you have:
- **Docker** installed on your system.
- **Docker Compose** installed.

## How to Run the Project

To build and run the project with MLflow locally, follow these steps:

### 1. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/ARKNravi/MLOps-Make-File.git
cd MLOps-Make-File
```

### 2. Build and Run with Docker Compose

Run the following command to build the Docker images and start the services:

```bash
docker-compose up --build
```

This will:
- Build the Docker image for the main application (`mlops-app`).
- Pull the necessary image for MLflow.
- Start both the main application and MLflow UI.

### 3. Access MLflow UI

Once everything is up and running, you can access the MLflow UI by navigating to:

```
http://localhost:5000
```

### 4. Stopping the Services

To stop the services, press `CTRL + C` in the terminal where Docker Compose is running. You can also stop the services with:

```bash
docker-compose down
```

## Dockerfile Overview

The `Dockerfile` sets up the environment using Miniconda, installs necessary dependencies, and clones the repository. Here's an outline of what each section does:

- **FROM continuumio/miniconda3**: Uses Miniconda as the base image for managing Python environments.
- **WORKDIR /app**: Sets `/app` as the working directory.
- **RUN apt-get update && apt-get install -y git make**: Installs Git and Make tools.
- **RUN git clone ... || git pull**: Clones or updates the project repository.
- **RUN conda env create/update**: Sets up the Conda environment specified in `environment.yml`.
- **COPY entrypoint.sh**: Copies the entrypoint script into the container.
- **ENTRYPOINT**: Sets the entrypoint script as the container’s startup command.

## `docker-compose.yml` Overview

The `docker-compose.yml` file defines the services to be run:

- **mlops-app**: The main application.
  - **build**: Builds the Docker image from the local `Dockerfile`.
  - **ports**: Exposes the app on port `8080`.
  - **volumes**: Mounts the current directory into the container.
  - **environment**: Specifies the MLflow tracking URI for SQLite.
  
- **mlflow**: MLflow service for experiment tracking.
  - **image**: Uses Miniconda to install MLflow.
  - **ports**: Exposes MLflow on port `5000`.
  - **volumes**: Mounts the current directory for the database and artifacts.
  - **working_dir**: Sets the working directory to `/app`.
  - **command**: Starts MLflow, ensures the SQLite database is upgraded, and serves the MLflow UI.

## Environment Configuration

The project environment is defined in `environment.yml`, which includes all necessary dependencies such as:

- **Python 3.8**
- **Pandas**
- **Scikit-learn**
- **MLflow**
- **Joblib**
- **Matplotlib**
- **Seaborn**

You can modify this file to add or update dependencies as needed.

## Troubleshooting

- **MLflow Database Error**: If you encounter an error related to the database migration (`Can't locate revision identified by '4465047574b1'`), delete the `mlflow.db` file and restart the services to reset the database.
  
```bash
rm mlflow.db
docker-compose up --build
```

- **Orphaned Containers**: If Docker shows a warning about orphaned containers, use the `--remove-orphans` flag to clean them up:

```bash
docker-compose up --build --remove-orphans
```

---
