import pandas as pd
import joblib
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Database connection
engine = create_engine(
    "postgresql+psycopg2://postgres@localhost:5432/churn_project"
)

# Load data
df = pd.read_sql("SELECT * FROM customers;", engine)

# Preprocessing
df["totalcharges"] = pd.to_numeric(
    df["totalcharges"],
    errors="coerce"
)

df = df.dropna()

df["churn"] = df["churn"].map({
    "Yes": 1,
    "No": 0
})

df = df.drop("customerid", axis=1)

df_encoded = pd.get_dummies(
    df,
    drop_first=True
)

# Features and target
X = df_encoded.drop("churn", axis=1)
y = df_encoded["churn"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "churn_model.pkl")

# Save column names
joblib.dump(X.columns.tolist(), "model_columns.pkl")

print("Model saved successfully")