import streamlit  as st
import pandas as pd

dataset = pd.read_csv("HOSTEL ATTENDENCE.csv")

st.dataframe(dataset)