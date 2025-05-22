import pandas as pd
import psycopg2
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "postgres")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

df = pd.read_sql("SELECT * FROM machine_data", conn)

# Update with actual feature columns and target
X = df[["temperature", "pressure"]]
y = (df["status"] == "failed").astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as model.pkl")
