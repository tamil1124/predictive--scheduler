import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("data.csv")

# Encode categorical columns
machine_encoder = LabelEncoder()
priority_encoder = LabelEncoder()
status_encoder = LabelEncoder()

df["Machine_ID"] = machine_encoder.fit_transform(df["Machine_ID"])
df["Priority"] = priority_encoder.fit_transform(df["Priority"])
df["Status"] = status_encoder.fit_transform(df["Status"])

# Features and Target
X = df[["Machine_ID", "Processing_Time", "Priority"]]
y = df["Status"]

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Prediction Function
def predict_status(machine_id, processing_time, priority):

    machine = machine_encoder.transform([machine_id])[0]
    priority = priority_encoder.transform([priority])[0]

    prediction = model.predict([[machine, processing_time, priority]])

    return status_encoder.inverse_transform(prediction)[0]