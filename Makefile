.PHONY: all data train evaluate deploy clean

# Use PowerShell as the shell
SHELL := powershell.exe
.SHELLFLAGS := -NoProfile -Command

all: data train evaluate deploy

data:
	@echo "Preparing data..."
	python scripts/data_prep.py

train: data
	@echo "Training model..."
	python scripts/train_model.py

evaluate: train
	@echo "Evaluating model..."
	python scripts/evaluate_model.py

deploy: evaluate
	@echo "Deploying model..."
	python scripts/deploy_model.py

clean:
	@echo "Cleaning up..."
	if (Test-Path data/processed) { Remove-Item -Recurse -Force data/processed/* }
	if (Test-Path models) { Remove-Item -Recurse -Force models/* }
	if (Test-Path results) { Remove-Item -Recurse -Force results/* }
	if (Test-Path deployment) { Remove-Item -Recurse -Force deployment/* }