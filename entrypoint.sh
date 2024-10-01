#!/bin/bash

# Activate the Conda environment
source activate mlops-makefile

# Run the Makefile
make all

# Start the MLflow server
python mlflow_tracking_server.py