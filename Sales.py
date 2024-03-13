#Import Needed Libraries
import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.dates as mdates


# Set the deprecation option to False to ignore the warning
st.set_option('deprecation.showPyplotGlobalUse', False)

#Loading The Dataset
df = pd.read_csv("Fashion_Retail_Sales.csv")

#Handling Nulls & Missing Values
df = df.dropna(subset=['Purchase Amount (USD)'])

# Convert 'Date Purchase' to datetime
df['Date Purchase'] = pd.to_datetime(df['Date Purchase'])

# Sort the dataframe by date
df.sort_values('Date Purchase', inplace=True)


# Set the plot background to dark black
plt.style.use('dark_background')

# Function to create line chart
def create_line_chart(df, year):
    plt.figure(figsize=(10, 6))
    filtered_df = df[df['Date Purchase'].dt.year == year]
    sns.lineplot(data=filtered_df, x='Date Purchase', y='Purchase Amount (USD)', color='yellow', linestyle='--')

    plt.title('Purchase Amount Over Time')
    plt.xlabel('Date')
    plt.ylabel('Purchase Amount (USD)')

    # Rotate x-axis tick labels by 45 degrees
    plt.xticks(rotation=45)

    # Format x-axis dates as 'YYYY-MM-DD'
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    st.pyplot()


# Calculate the metrics
maximum_purchase = df['Purchase Amount (USD)'].max()
average_purchase = df['Purchase Amount (USD)'].mean()
minimum_purchase = df['Purchase Amount (USD)'].min()



def app():

    col1, col2, col3 = st.columns(3)

    # Display the metrics in the Streamlit app
    with col1:
        st.metric(label="Maximum purchase", value=f"{int(maximum_purchase)} USD", delta=None)
        st.markdown(f"<style>.container{{text-align:center !important;}}</style>", unsafe_allow_html=True)

    with col2:
        st.metric(label="Average purchase", value=f"{int(average_purchase)} USD", delta=None)
        st.markdown(f"<style>.container{{text-align:center !important;}}</style>", unsafe_allow_html=True)

    with col3:
        st.metric(label="Minimum purchase", value=f"{int(minimum_purchase)} USD", delta=None)
        st.markdown(f"<style>.container{{text-align:center !important;}}</style>", unsafe_allow_html=True)


    st.write("")
    st.write("")     

    st.write("Purchase Amount Over Time")
    st.write("")
    
    # Sidebar
    st.sidebar.header("Sales Overview")
    st.sidebar.write("")

    # Sidebar year selection
    year = st.sidebar.selectbox("Select Year", options=df['Date Purchase'].dt.year.unique())

    # Sidebar filter for Purchase Amount
    purchase_amount_filter = st.sidebar.slider('Select Purchase Amount Range', min_value=0, max_value=500, value=(0, 500))


    # Apply filter to dataframe
    filtered_df = df[(df['Purchase Amount (USD)'] >= purchase_amount_filter[0]) & (df['Purchase Amount (USD)'] <= purchase_amount_filter[1])]



    # Call the function with selected year
    create_line_chart(df, year)


    st.write("")
    st.write( "Purchase Amount (USD) vs Review Rating")
    st.write("")

    # Create scatter plot with two different colors
    fig, ax = plt.subplots()
    ax.scatter(filtered_df.loc[filtered_df['Review Rating'] < 4, 'Purchase Amount (USD)'], filtered_df.loc[filtered_df['Review Rating'] < 4, 'Review Rating'], color='lightblue', label='Low Rating')
    ax.scatter(filtered_df.loc[filtered_df['Review Rating'] >= 4, 'Purchase Amount (USD)'], filtered_df.loc[filtered_df['Review Rating'] >= 4, 'Review Rating'], color='lightgreen', label='High Rating')
    ax.set_xlabel('Purchase Amount (USD)')
    ax.set_ylabel('Review Rating')
    ax.legend()
    st.pyplot(fig)
    
