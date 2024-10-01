.PHONY: all env data train evaluate deploy clean setup_dirs mlflow_server

# Define the conda environment name
CONDA_ENV := mlops-makefile

# Define the conda activation command for Linux
CONDA_ACTIVATE := conda run -n $(CONDA_ENV)

# Main target that runs everything
all: env setup_dirs data train evaluate deploy

# Check if the Conda environment exists, otherwise create it
env:
	@echo "Checking Conda environment..."
	@conda env list | grep -q "$(CONDA_ENV)" && \
	(echo "Environment already exists") || \
	(echo "Creating Conda environment..." && CONDA_NO_PLUGINS=true conda env create -f environment.yml)

# Ensure necessary directories exist
setup_dirs: env
	@echo "Creating necessary directories..."
	@mkdir -p data/raw data/processed models results deployment scripts mlruns

# Prepare the data
data: setup_dirs
	@echo "Preparing data..."
	$(CONDA_ACTIVATE) python scripts/data_prep.py

# Train the model
train: data
	@echo "Training model..."
	$(CONDA_ACTIVATE) python scripts/train_model.py

# Evaluate the model
evaluate: train
	@echo "Evaluating model..."
	$(CONDA_ACTIVATE) python scripts/evaluate_model.py

# Deploy the model
deploy: evaluate
	@echo "Deploying model..."
	$(CONDA_ACTIVATE) python scripts/deploy_model.py

# Start MLflow tracking server
mlflow_server:
	@echo "Starting MLflow tracking server..."
	$(CONDA_ACTIVATE) python mlflow_tracking_server.py

# Clean up directories and remove the environment
clean:
	@echo "Cleaning up..."
	rm -rf data/processed models results deployment mlruns
	conda env remove -n $(CONDA_ENV)
