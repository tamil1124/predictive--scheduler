import streamlit as st
import pandas as pd
from model import predict_status

st.set_page_config(
    page_title="Predictive Scheduling for Production Plants",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Predictive Scheduling for Production Plants")
st.write("### Machine Learning Based Scheduling System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Dataset", "Prediction", "About"]
)

if menu == "Home":
    st.header("Welcome")
    st.write("""
This project predicts production scheduling status using
Machine Learning.
""")

elif menu == "Dataset":
    st.header("Production Dataset")
    df = pd.read_csv("data.csv")
    st.dataframe(df)

elif menu == "Prediction":
    st.header("Predict Production Status")

    machine = st.selectbox("Machine ID", ["M1", "M2", "M3"])

    processing_time = st.number_input(
        "Processing Time",
        min_value=1,
        max_value=24,
        value=3
    )

    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"]
    )

    if st.button("Predict"):

        result = predict_status(
            machine,
            processing_time,
            priority
        )

        st.success("Prediction Completed")

        st.table(pd.DataFrame({
            "Machine": [machine],
            "Processing Time": [processing_time],
            "Priority": [priority],
            "Predicted Status": [result]
        }))

elif menu == "About":
    st.header("About")
    st.write("""
Project Name:
Predictive Scheduling for Production Plants

Developed using:
- Python
- Streamlit
""")
