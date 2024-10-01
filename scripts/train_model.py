import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import mlflow
import mlflow.sklearn
import os

# Set SQLite-based tracking URI for both tracking and model registry
mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "sqlite:///mlflow.db"))

# Load processed data
X_train = pd.read_csv('data/processed/X_train.csv')
y_train = pd.read_csv('data/processed/y_train.csv').values.ravel()

# Create or get the experiment
experiment_name = "iris_classification"
try:
    experiment_id = mlflow.create_experiment(experiment_name)
except mlflow.exceptions.MlflowException:
    experiment_id = mlflow.get_experiment_by_name(experiment_name).experiment_id

# Start MLflow run
with mlflow.start_run(experiment_id=experiment_id):
    # Train the model
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)

    # Log model parameters
    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_param("random_state", 42)

    # Save the model
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/iris_model.joblib')
    
    # Log the model to registry
    mlflow.sklearn.log_model(model, "iris_model")

    print("Model training completed and logged with MLflow.")
