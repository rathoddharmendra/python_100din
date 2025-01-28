import streamlit as st
import pandas as pd

st.title('Streamlit powered website panel')

# Load data
df = pd.DataFrame({ 
    'name': ['Dee', 'Sheral', 'Alaynna', 'Shana'],
    'score': [23,34,32,53]
    }
)

st.write(df)
st.line_chart(df, x_label='Names', y_label='Score')