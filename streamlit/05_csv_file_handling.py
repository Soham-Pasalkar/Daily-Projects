import streamlit as st
import pandas as pd

st.title("CSV File Handling")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data")
    st.dataframe(df)

#Basic Transformations

    if st.button("Show Summary Statistics"):
        st.write("Summary Statistics:")
        st.write(df.describe())

    if st.button("Filter by Column"):
        column = st.selectbox("Select Column to Filter", df.columns)
        value = st.text_input(f"Enter value to filter {column} by")
        if value:
            filtered_df = df[df[column].astype(str).str.contains(value,case=False)]
            st.dataframe(filtered_df)

else:
    st.write("Please enter a csv file.")

