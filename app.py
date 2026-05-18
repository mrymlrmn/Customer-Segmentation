import streamlit as st
from main import run

st.title("Customer Segmentation App")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    with st.spinner("Processing..."):
        df = run(uploaded_file)
    
    st.subheader("Customer Segments")
    st.dataframe(df[['Cluster', 'Segment', 'Total_Spent', 'Frequency', 'Recency']])
    
    st.subheader("Segment Summary")
    st.dataframe(df.groupby('Segment')[['Total_Spent', 'Frequency', 'Recency']].mean().round(2))