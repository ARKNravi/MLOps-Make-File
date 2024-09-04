import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load processed data
X_train = pd.read_csv('data/processed/X_train.csv')
y_train = pd.read_csv('data/processed/y_train.csv').values.ravel()

# Train the model
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'models/iris_model.joblib')

print("Model training completed.")