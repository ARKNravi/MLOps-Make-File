.PHONY: all env data train evaluate deploy clean

# Define the conda environment name
CONDA_ENV := mlops-makefile

# Define the conda activation command for Windows
CONDA_ACTIVATE := call activate $(CONDA_ENV)

all: env data train evaluate deploy

env:
	@echo "Checking Conda environment..."
	@conda info --envs | findstr /i "$(CONDA_ENV)" > nul && \
	(echo Environment already exists) || \
	(echo Creating Conda environment... && conda env create -f environment.yml)

data: env
	@echo "Preparing data..."
	$(CONDA_ACTIVATE) && python scripts/data_prep.py

train: data
	@echo "Training model..."
	$(CONDA_ACTIVATE) && python scripts/train_model.py

evaluate: train
	@echo "Evaluating model..."
	$(CONDA_ACTIVATE) && python scripts/evaluate_model.py

deploy: evaluate
	@echo "Deploying model..."
	$(CONDA_ACTIVATE) && python scripts/deploy_model.py

clean:
	@echo "Cleaning up..."
	if exist data\processed rmdir /s /q data\processed
	if exist models rmdir /s /q models
	if exist results rmdir /s /q results
	if exist deployment rmdir /s /q deployment
	conda env remove -n $(CONDA_ENV)