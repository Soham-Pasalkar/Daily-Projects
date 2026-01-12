import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

st.title("Machine Learning with Iris Dataset")

# Load Iris Dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
st.write("Iris Dataset")
st.dataframe(df.head())

# Train Model
model = RandomForestClassifier()
model.fit(iris.data , iris.target)
st.write("Model trained on Iris dataset.")

# User Input for Prediction
st.header("Make a Prediction")
sepal_length = st.slider("Sepal Length", 4.0,8.0,5.0)
sepal_width = st.slider("Sepal Width", 2.0,4.5,3.0)
petal_length = st.slider("Petal Length", 1.0,7.0,1.5)
petal_width = st.slider("Petal Width", 0.1,2.5,0.2)
user_input = np.array([[sepal_length, sepal_width, petal_length, petal_width]])


prediction = model.predict(user_input)
predicted_species = iris.target_names[prediction][0]
st.write(f"Predicted Species: {predicted_species}")