#!/bin/bash

# Activate the Conda environment
source activate mlops-makefile

# Run the Makefile
make all

# Start the MLflow server and make it accessible from outside the container
mlflow ui --backend-store-uri sqlite:///mlflow.db --host 0.0.0.0 --port 5000
