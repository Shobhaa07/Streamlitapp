# Imports necessary libraries 
import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(
    page_title="Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)
# Custom CSS to style the dashboard
st.markdown(
    """
    <style>
        /* Center align the main header and subheader */
        .center {
            text-align: center;
        }
        
        /* Add padding to the bordered container */
        .bordered {
            border: 2px solid #ddd;  /* Add a light gray border */
            border-radius: 10px;  /* Add border radius for rounded corners */
            padding: 20px;
            margin-bottom: 20px;  /* Add some space between elements */
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Add a shadow effect */
            background-color: #f9f9f9; /* Light gray background color */
        }
      
    </style>
    """,
    unsafe_allow_html=True
)

# Bordered container for the entire dashboard
st.markdown('<div class="bordered">', unsafe_allow_html=True)

# Main header and subheader
st.markdown('<div class="center header"><h1>Global Superstore Dashboard<h1></div>', unsafe_allow_html=True)
st.markdown('<div class="center subheader"><h3>An Analysis of Sales Data<h3></div>', unsafe_allow_html=True)

# Read the dataset
df = pd.read_excel("cleaned_dataset.xlsx", engine='openpyxl')

# Creating three-column layout
col1, col2, col3 = st.columns(3)

# Box Plot
with col1:
        fig_box = px.box(df, x='Sub-Category', y='Quantity', title='Box Plot')
        fig_box.update_traces(marker=dict(color='green'))
        st.plotly_chart(fig_box, use_container_width=True)

# Bar Chart
with col2:
        fig_bar = px.bar(df, x='Ship Mode', y='Shipping Cost', title='Bar Chart')
        fig_bar.update_traces(marker=dict(color='#eba434')) 
        st.plotly_chart(fig_bar, use_container_width=True)
