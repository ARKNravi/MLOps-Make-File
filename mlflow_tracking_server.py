import sys
import mlflow
import os
import subprocess

if __name__ == "__main__":
    print(f"Python executable: {sys.executable}")
    print(f"MLflow version: {mlflow.__version__}")
    
    # Define SQLite URI for model registry and experiment tracking
    mlflow_tracking_uri = os.getenv("MLFLOW_TRACKING_URI", f"sqlite:///{os.path.abspath('mlflow.db')}")
    mlflow.set_tracking_uri(mlflow_tracking_uri)
    
    print(f"MLflow Tracking URI: {mlflow_tracking_uri}")
    print("Starting MLflow UI. Access it at http://localhost:5000")
    
    subprocess.run(["mlflow", "ui", "--port", "5000", "--backend-store-uri", mlflow_tracking_uri])
