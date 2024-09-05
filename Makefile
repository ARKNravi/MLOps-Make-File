.PHONY: all env data train evaluate deploy clean setup_dirs

# Define the conda environment name
CONDA_ENV := mlops-makefile

# Define the conda activation command for Windows
CONDA_ACTIVATE := call activate $(CONDA_ENV)

# Main target that runs everything
all: env setup_dirs data train evaluate deploy

# Check if the Conda environment exists, otherwise create it
env:
	@echo "Checking Conda environment..."
	@conda info --envs | findstr /i "$(CONDA_ENV)" > nul && \
	(echo Environment already exists) || \
	(echo Creating Conda environment... && conda env create -f environment.yml)

# Ensure necessary directories exist
setup_dirs:
	@echo "Creating necessary directories..."
	@if not exist data\raw mkdir data\raw
	@if not exist data\processed mkdir data\processed
	@if not exist models mkdir models
	@if not exist results mkdir results
	@if not exist deployment mkdir deployment
	@if not exist scripts mkdir scripts

# Prepare the data
data: env
	@echo "Preparing data..."
	$(CONDA_ACTIVATE) && python scripts/data_prep.py

# Train the model
train: data
	@echo "Training model..."
	$(CONDA_ACTIVATE) && python scripts/train_model.py

# Evaluate the model
evaluate: train
	@echo "Evaluating model..."
	$(CONDA_ACTIVATE) && python scripts/evaluate_model.py

# Deploy the model
deploy: evaluate
	@echo "Deploying model..."
	$(CONDA_ACTIVATE) && python scripts/deploy_model.py

# Clean up directories and remove the environment
clean:
	@echo "Cleaning up..."
	if exist data\processed rmdir /s /q data\processed
	if exist models rmdir /s /q models
	if exist results rmdir /s /q results
	if exist deployment rmdir /s /q deployment
	conda env remove -n $(CONDA_ENV)
