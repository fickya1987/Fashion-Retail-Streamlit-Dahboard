#Import Needed Libraries
import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.dates as mdates

#Loading The Dataset
df = pd.read_csv("Fashion_Retail_Sales.csv")

# Convert 'Date Purchase' to datetime
df['Date Purchase'] = pd.to_datetime(df['Date Purchase'])

# Sort the dataframe by date
df.sort_values('Date Purchase', inplace=True)


# Calculate the metrics
# Calculate the top purchasing customer
top_purchasing_customer = df.loc[df['Purchase Amount (USD)'].idxmax(), 'Customer Reference ID']

# Calculate the min purchasing customer
min_purchasing_customer = df.loc[df['Purchase Amount (USD)'].idxmin(), 'Customer Reference ID']

# Calculate the top rating customer
top_rating_customer = df.loc[df['Review Rating'].idxmax(), 'Customer Reference ID']

# Calculate the least rating customer
least_rating_customer = df.loc[df['Review Rating'].idxmin(), 'Customer Reference ID']


def app():


    # Display metrics in two columns using streamlit
    col1, col2, col3, col4 = st.columns(4)


    # Metric 1: Top Purchasing Customer
    with col1:
        st.metric("Top Purchasing Customer", top_purchasing_customer)

    # Metric 2: Min Purchasing Customer
    with col2:
        st.metric("Min Purchasing Customer", min_purchasing_customer)

    # Metric 3: Top Rating Customer
    with col3:
        st.metric("Top Rating Customer", top_rating_customer)

    # Metric 4: Least Rating Customer
    with col4:
        st.metric("Least Rating Customer", least_rating_customer)


    st.header('Top 10 Customers')

    #sidebar

    # Create sidebar dropdown for selection
    selection_customers = st.sidebar.selectbox('Select Top Customers Based On', ['Review Rating', 'Purchase Amount (USD)'])

    # Determine top 10 customers based on selection
    if selection_customers == 'Review Rating':
        top_10_customers = df.nlargest(10, 'Review Rating', keep='first')
        title_customers = 'Top 10 Customers by Review Rating'
    else:
        top_10_customers = df.nlargest(10, 'Purchase Amount (USD)')
        title_customers = 'Top 10 Customers by Total Purchases'

    # Create the bar chart using Plotly Express for top customers
    fig_customers = px.bar(top_10_customers, x='Customer Reference ID', y=selection_customers, title=title_customers, labels={selection_customers: selection_customers})

    # Display the bar chart for top customers using Streamlit
    st.plotly_chart(fig_customers)


    
    st.header("Payment Method: Cash Vs Credit Card")


    # Create sidebar dropdown for payment method selection
    payment_method = st.sidebar.selectbox('Select Payment Method', ['Cash', 'Credit Card'])

    # Filter data based on payment method selection
    filtered_data = df[df['Payment Method'] == payment_method]

    
    # Set the size of the plot
    plt.figure(figsize=(10, 6))

    # Create the line chart using seaborn
    line_chart = sns.lineplot(data=filtered_data, x='Date Purchase', y='Purchase Amount (USD)')
    plt.title(f'Total Purchases Over Time ({payment_method})')
    plt.xlabel('Date')
    plt.ylabel('Total Purchases')

    # Set x-axis to display only months
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))


    # Display the line chart using Streamlit
    st.pyplot()
    
    
    
    # Create the line chart using Plotly Express
    #line_chart = px.line(filtered_data, x='Date Purchase', y='Purchase Amount (USD)', title=f'Total {payment_method} Purchases Over Time')

    # Set x-axis to display only months
    #line_chart.update_xaxes(dtick='M1', tickformat='%b\n%Y')

    # Display the line chart using Streamlit
    #st.plotly_chart(line_chart)





    