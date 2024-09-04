import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import json

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

# Save metrics
with open('results/model_metrics.json', 'w') as f:
    json.dump(metrics, f)

print("Model evaluation completed. Metrics saved to results/model_metrics.json")