import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

engine = create_engine(
    "postgresql+psycopg2://postgres@localhost:5432/churn_project"
)

df = pd.read_sql("SELECT * FROM customers;", engine)

df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")
df = df.dropna()

df["churn"] = df["churn"].map({"Yes": 1, "No": 0})
df = df.drop("customerid", axis=1)

# Plot 1
sns.countplot(x="churn", data=df)
plt.title("Customer Churn Distribution")
plt.savefig("churn_distribution.png")
plt.close()

# Plot 2
sns.boxplot(x="churn", y="tenure", data=df)
plt.title("Tenure vs Churn")
plt.savefig("tenure_vs_churn.png")
plt.close()

# Plot 3
sns.boxplot(x="churn", y="monthlycharges", data=df)
plt.title("Monthly Charges vs Churn")
plt.savefig("monthly_charges_vs_churn.png")
plt.close()

# ML model again for confusion matrix
df_encoded = pd.get_dummies(df, drop_first=True)

X = df_encoded.drop("churn", axis=1)
y = df_encoded["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.savefig("confusion_matrix.png")
plt.close()