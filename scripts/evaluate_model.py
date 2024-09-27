import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import json
import mlflow
import os

# Use SQLite as the backend tracking URI (ensure the correct path to 'mlflow.db')
mlflow.set_tracking_uri("sqlite:///C:/Recovery/Project/MLOpsSemester5/MLOps-Make-File/mlflow.db")

# Load the model and test data
model = joblib.load('models/iris_model.joblib')
X_test = pd.read_csv('data/processed/X_test.csv')
y_test = pd.read_csv('data/processed/y_test.csv').values.ravel()

# Make predictions
y_pred = model.predict(X_test)

# Calculate metrics
metrics = {
    'accuracy': accuracy_score(y_test, y_pred),
    'precision': precision_score(y_test, y_pred, average='weighted'),
    'recall': recall_score(y_test, y_pred, average='weighted'),
    'f1_score': f1_score(y_test, y_pred, average='weighted')
}

# Save metrics locally
with open('results/model_metrics.json', 'w') as f:
    json.dump(metrics, f)

# Start an MLflow run using SQLite for experiment tracking
with mlflow.start_run():
    for metric_name, metric_value in metrics.items():
        mlflow.log_metric(metric_name, metric_value)

print("Model evaluation completed. Metrics saved to results/model_metrics.json and logged with MLflow.")
