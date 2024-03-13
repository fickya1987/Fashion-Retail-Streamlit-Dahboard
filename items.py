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

# Convert 'Date Purchase' to datetime
df['Date Purchase'] = pd.to_datetime(df['Date Purchase'])

# Sort the dataframe by date
df.sort_values('Date Purchase', inplace=True)



# Calculate the metrics
# Find the maximum rating item
max_rating = df[df['Review Rating'] == df['Review Rating'].max()]['Item Purchased'].values[0]

# Find the minimum rating item
min_rating = df[df['Review Rating'] == df['Review Rating'].min()]['Item Purchased'].values[0]

# Find the most sold item
most_sold = df['Item Purchased'].value_counts().idxmax()

# Find the least sold item
least_sold = df['Item Purchased'].value_counts().idxmin()


def app():

    # Create 4 columns
    col1, col2, col3, col4 = st.columns(4)

    # Display max rating item
    with col1:
        st.metric(label='Max Rating Item', value=max_rating)

    # Display min rating item
    with col2:
        st.metric(label='Min Rating Item', value=min_rating)

    # Display most sold item
    with col3:
        st.metric(label='Most Sold Item', value=most_sold)

    # Display least sold item
    with col4:
        st.metric(label='Least Sold Item', value=least_sold)

    st.write("")
    st.write("")    
    
    
    #sidebar

    st.sidebar.write("Items")

    # Create sidebar for year and month selection
    year = st.sidebar.selectbox('Select Year', options=[2022, 2023], index=1)
    month = st.sidebar.slider('Select Month', min_value=1, max_value=12, value=1)


    #Filter the data based on the selected year and month
    filtered_data = df[(df['Date Purchase'].dt.year.isin([2022, 2023])) & (df['Date Purchase'].dt.month == month)]
    

    st.write("")

    st.header("2022 Vs 2023 Sales")

    # Generate the plot
    fig, ax = plt.subplots()
    filtered_data.groupby('Item Purchased')['Purchase Amount (USD)'].sum().plot(kind='bar', ax=ax)
    plt.title('Item Purchased Sales for {} {}'.format(month, year))
    plt.xlabel('Item Purchased')
    plt.ylabel('Sales')
    st.pyplot(fig)

    
    # Create multiselect sidebar for item selection
    selected_items = st.sidebar.multiselect('Select Items', ['All'] + list(df['Item Purchased'].unique()), default='All')


    # Filter the data based on the selected items
    if 'All' in selected_items:
        filtered_df = df
    else:
        filtered_df = df[df['Item Purchased'].isin(selected_items)]

    # Create the scatter plot using Plotly Express
    fig = px.scatter(filtered_df, x='Date Purchase', y='Purchase Amount (USD)', color='Item Purchased',
                 title='Items Purchased Sales Popularity', labels={'Purchase Amount (USD)': 'Purchase Amount'})

    # Display the plot using Streamlit
    st.plotly_chart(fig)


    # Create sidebar dropdown for selection
    selection = st.sidebar.selectbox('Select Top Items Based On', ['Review Rating', 'Purchase Amount (USD)'])

    # Determine top 10 items based on selection
    if selection == 'Review Rating':
        top_10 = df.nlargest(10, 'Review Rating')
        title = 'Top 10 Items by Review Rating'
    else:
        top_10 = df.nlargest(10, 'Purchase Amount (USD)')
        title = 'Top 10 Items by Total Purchases'

    st.header('Top 10 Items')

    # Create the bar chart using Plotly Express
    fig = px.bar(top_10, x='Item Purchased', y=selection, title=title, labels={selection: selection})

    # Display the bar chart using Streamlit
    st.plotly_chart(fig)
