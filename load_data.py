import pandas as pd
from sqlalchemy import create_engine

# Load CSV file
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Buti7755@localhost:5432/churn_project"
)

# Load dataframe into PostgreSQL
df.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully")