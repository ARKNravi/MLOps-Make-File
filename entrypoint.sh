#!/bin/bash

# Activate the Conda environment
source activate mlops-makefile

# Run the Makefile
make all

# Start the MLflow server and make it accessible on localhost:8080
mlflow ui --backend-store-uri sqlite:///mlflow.db --host 0.0.0.0 --port 8080
