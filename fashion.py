#Import Needed Libraries
import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

#Loading The Dataset
df = pd.read_csv("Fashion_Retail_Sales.csv")

#Handling Nulls & Missing Values
df = df.dropna(subset=['Purchase Amount (USD)'])

average_rating = df['Review Rating'].mean()
df['Review Rating'] = df['Review Rating'].fillna(average_rating)

# Define the summary function
def summary(df):
    summary_df = pd.DataFrame(df.dtypes, columns=['dtypes'])
    summary_df['missing#'] = df.isna().sum()
    summary_df['missing%'] = (df.isna().sum())/len(df)
    summary_df['unique'] = df.nunique().values
    summary_df['count'] = df.count().values
    return summary_df

# Apply the summary function and style the output
final_summary = summary(df).style.background_gradient(cmap='Blues')


# Create a Styler object to apply formatting
summary_stats = df.describe().transpose()
styled_summary = summary_stats.style.set_properties(**{'text-align': 'center', 'border-color': 'black', 'border-style': 'solid'})
styled_summary = styled_summary.set_table_styles([
    {'selector': 'thead', 'props': [('background-color', '#f2f2f2'), ('border-color', 'black'), ('border-style', 'solid')]},
    {'selector': 'th', 'props': [('border-color', 'black'), ('border-style', 'solid'),
                                  ('background-color', '#8bb8f2'), ('color', '#ffffff')]},
    {'selector': 'td', 'props': [('border-color', 'black'), ('border-style', 'solid'),
                                  ('background-color', '#ffffff'), ('color', '#555555')]}
])



def DatasetStructure(df):
    
    structure_df = pd.DataFrame({'Records': [df.shape[0]], 'Columns': [df.shape[1]]})
    styled_table = structure_df.style.set_table_styles([
        {'selector': 'table', 'props': [('border', '2px solid black')]},
        {'selector': 'th', 'props': [('background-color', 'lightgray')]}
    ])
    
    return styled_table




def app():
    
    #Sidebar
    st.sidebar.header('Data Exploration')
    st.sidebar.write("")
    # Add a sidebar to control the display of different components
    show_sample = st.sidebar.checkbox('Show Data Sample', value=True)
    show_general_info = st.sidebar.checkbox('Show General Information', value=False)
    show_statistical_summary = st.sidebar.checkbox('Show Statistical Summary', value=False)
    show_structure = st.sidebar.checkbox('Show Dataset Structure', value=False)

    # Display the selected components based on the checkbox values
    if show_sample:
        sample_size = st.sidebar.slider('Select sample size', 1, 100, 10)
        st.header("Data Sample")
        st.write(df.sample(sample_size))

    # Display the styled summary based on the checkbox value
    if show_general_info:
        st.header("General Information")
        st.write(final_summary)

    if show_statistical_summary:
        st.header("Statistical Summary")
        st.write(styled_summary)

    # Display the dataset structure based on the checkbox value
    if show_structure:
        st.header("Dataset Structure")
        st.write(DatasetStructure(df))    