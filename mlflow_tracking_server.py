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
    print("Starting MLflow UI. Access it at http://localhost:7000 or http://localhost:7001")

    mlflow_start_time = time.time()
    
    port = 7000
    if subprocess.run(["lsof", "-i", f":{port}"]).returncode == 0:
        print(f"Port {port} is in use. Trying the next port...")
        port = 7001
    
    print(f"Using port {port}")
    subprocess.run(["mlflow", "ui", "--port", str(port), "--host", "0.0.0.0", "--backend-store-uri", mlflow_tracking_uri])

    print(f"MLflow UI started in {time.time() - mlflow_start_time:.2f} seconds.")
    print(f"Total time: {time.time() - start_time:.2f} seconds.")