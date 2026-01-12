import streamlit as st

st.title("Basic Streamlit Elements")

slider_value = st.slider("Select a Value", 0 , 100, 50)
st.write(f"Slider value: {slider_value}")

if st.button("Click Me"):
    st.write("Button clicked!")

options = st.multiselect("Choose multiple", ["Option 1", "Option 2", "Option 3"])
st.write(f"Selected options: {options}")

uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    st.write(f"Uploaded file: {uploaded_file.name}")

radio_choice = st.radio("Pick one", ["Choice A", "Choice B", "Choice C"])
st.write(f"Radio choice : {radio_choice}")

checkbox = st.checkbox("Check me!")
if checkbox:
    st.write("Checkbox is checked!")

