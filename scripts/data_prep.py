import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

# Ensure output directory exists
os.makedirs('data/processed', exist_ok=True)

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Create a DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save processed data
pd.DataFrame(X_train_scaled).to_csv('data/processed/X_train.csv', index=False)
pd.DataFrame(X_test_scaled).to_csv('data/processed/X_test.csv', index=False)
pd.DataFrame(y_train).to_csv('data/processed/y_train.csv', index=False)
pd.DataFrame(y_test).to_csv('data/processed/y_test.csv', index=False)

print("Data preparation completed.")
