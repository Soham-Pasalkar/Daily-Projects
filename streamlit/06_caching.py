import streamlit as st

st.title("Caching")

n = st.slider("Select a number", 1, 1000000, 1000)

@st.cache_data #decortator to cache the function output
def sum_numbers(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

st.write(f"Sum of numbers from 0 to {n} is:", sum_numbers(n))
              