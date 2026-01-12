import streamlit as st
import pandas as pd
import numpy as np
import time 

st.title("Real-time Data Visualization")

#Progress Bar
progress_bar = st.progress(0)
status_text = st.empty()

for i in range(100):
    progress_bar.progress(i + 1)
    status_text.text(f"Iteration {i + 1}/100")
    time.sleep(0.1)

status_text.text("Process completed!")

#Real-Time Chart
chart_placeholder = st.empty()
data = pd.DataFrame(np.random.randn(100, 3), columns=['A','B','C'])
print(data)

for i in range(10):
    new_data = pd.DataFrame(np.random.randn(10, 3), columns=['A','B','C'])
    chart_placeholder.line_chart(new_data)
    chart_placeholder.line_chart(new_data)

st.write("Real-time data visualization complete!")