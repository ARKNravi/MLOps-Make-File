import shutil
import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import mlflow

def deploy_model():
    # Create deployment directory if it doesn't exist
    os.makedirs('deployment', exist_ok=True)

    # Copy the trained model to the deployment directory
    shutil.copy('models/iris_model.joblib', 'deployment/iris_model.joblib')
    print("Model deployed to deployment/iris_model.joblib")

def test_deployed_model():
    # Load the deployed model
    model = joblib.load('deployment/iris_model.joblib')

    # Load test data
    X_test = pd.read_csv('data/processed/X_test.csv')
    y_test = pd.read_csv('data/processed/y_test.csv').values.ravel()

    # Make predictions
    y_pred = model.predict(X_test)

    # Generate confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # Plot confusion matrix
    plt.figure(figsize=(10,7))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig('deployment/confusion_matrix.png')
    plt.close()

    # Generate and save classification report
    report = classification_report(y_test, y_pred, target_names=['setosa', 'versicolor', 'virginica'])
    with open('deployment/classification_report.txt', 'w') as f:
        f.write(report)

    print("Model performance visualizations saved in deployment folder.")

    # Test the model with a sample input
    sample_input = X_test.iloc[0].values.reshape(1, -1)
    prediction = model.predict(sample_input)
    print(f"Sample prediction: {prediction}")

    # Log artifacts with MLflow
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "sqlite:///mlflow.db"))

    # Use the same experiment name
    experiment_name = "iris_classification"
    experiment = mlflow.get_experiment_by_name(experiment_name)

    # If the experiment doesn't exist, create it
    if experiment is None:
        experiment_id = mlflow.create_experiment(experiment_name)
    else:
        experiment_id = experiment.experiment_id

    with mlflow.start_run(experiment_id=experiment_id):
        mlflow.log_artifact('deployment/confusion_matrix.png', 'confusion_matrix')
        mlflow.log_artifact('deployment/classification_report.txt', 'classification_report')

if __name__ == "__main__":
    deploy_model()
    test_deployed_model()
