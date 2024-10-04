import sys
import mlflow
import os
import subprocess
import time

if __name__ == "__main__":
    start_time = time.time()
    print(f"Python executable: {sys.executable}")
    print(f"MLflow version: {mlflow.__version__}")

    mlflow_tracking_uri = os.getenv("MLFLOW_TRACKING_URI", f"sqlite:///{os.path.abspath('mlflow.db')}")
    mlflow.set_tracking_uri(mlflow_tracking_uri)

    print(f"MLflow Tracking URI: {mlflow_tracking_uri}")
    print("Starting MLflow UI. Access it at http://0.0.0.0:5000")  # Change to port 5000 or 8080

    mlflow_start_time = time.time()
    subprocess.run(["mlflow", "ui", "--host", "0.0.0.0", "--port", "5000", "--backend-store-uri", mlflow_tracking_uri])

    print(f"MLflow UI started in {time.time() - mlflow_start_time:.2f} seconds.")
    print(f"Total time: {time.time() - start_time:.2f} seconds.")
