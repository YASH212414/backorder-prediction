import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from inference import predict  # Assuming you have a function for making predictions

# Title and Header
st.title('Prediction of Backorders in Inventory Management')
st.header('A Random Forest model trained with a balanced subsample class weight')
st.markdown('created by: **Mudimala Yeshwanth Goud**')

# File Upload
st.subheader("Upload a CSV file")
uploaded_file = st.file_uploader("Choose a file...", type=['csv'])

# If file uploaded
if uploaded_file is not None:
    # Read the uploaded file
    dataframe = pd.read_csv(uploaded_file)
    
    # Display first five rows
    st.write("Loading... Displaying first five rows")
    st.dataframe(data=dataframe.head(), width=730, height=200)
    
    # Correlation Matrix
    st.write("Correlation Matrix")
    fig, ax = plt.subplots()
    sns.heatmap(dataframe.corr(), ax=ax)
    plt.title('Correlation Matrix')
    st.pyplot(fig)
    
    # Predictions
    st.write("Predicting...")
    x = dataframe.drop('went_on_backorder', axis=1)  # Assuming 'went_on_backorder' is the target column
    predictions = predict(x)  # Function to make predictions
    st.write(predictions)
    
    st.write('Done')
