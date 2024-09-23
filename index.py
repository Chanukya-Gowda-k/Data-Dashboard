import streamlit as st
import pandas as pd
import plotly.express as px

# Set page layout to wide mode and configure the page title
st.set_page_config(page_title="Data Dashboard", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .dashboard-title {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        padding-top: 20px;
        padding-bottom: 10px;
    }
    .description {
        text-align: center;
        font-size: 18px;
        color: #6c757d;
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 28px;
        font-weight: bold;
        color: #007BFF;
        margin-top: 40px;
        margin-bottom: 10px;
    }
    .limitations, .footer {
        text-align: center;
        font-size: 16px;
        color: #6c757d;
        margin-top: 20px;
    }
    .footer {
        margin-bottom: 20px;
    }
    .card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Dashboard Title and Description
st.markdown('<div class="dashboard-title">Data Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Easily upload your data and visualize it with interactive plots!</div>', unsafe_allow_html=True)

# File uploader in the main page (not the sidebar)
uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file is not None:
    # Read CSV file
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())  # Display first few rows of the uploaded data

    # Create three columns for X and Y axis selection, and plot type selection
    col1, col2, col3 = st.columns(3)

    with col1:
        x_column = st.selectbox('Choose X-axis column', df.columns)

    with col2:
        y_column = st.selectbox('Choose Y-axis column', df.columns)

    with col3:
        plot_type = st.selectbox('Select plot type', [
            'Line Chart', 'Bar Chart', 'Scatter Plot', 
            'Area Chart', 'Histogram', 'Box Plot', 
            'Violin Plot', 'Pie Chart'
        ])

    # Plot based on user input
    st.write("<div class='section-title'>Plot based on the data</div>", unsafe_allow_html=True)
    
    if plot_type == 'Line Chart':
        fig = px.line(df, x=x_column, y=y_column, title=f'{plot_type} of {x_column} vs {y_column}')
        st.plotly_chart(fig)

    elif plot_type == 'Bar Chart':
        fig = px.bar(df, x=x_column, y=y_column, title=f'{plot_type} of {x_column} vs {y_column}')
        st.plotly_chart(fig)

    elif plot_type == 'Scatter Plot':
        fig = px.scatter(df, x=x_column, y=y_column, title=f'{plot_type} of {x_column} vs {y_column}', hover_data={x_column: True, y_column: True})
        st.plotly_chart(fig)

    elif plot_type == 'Area Chart':
        fig = px.area(df, x=x_column, y=y_column, title=f'{plot_type} of {x_column} vs {y_column}')
        st.plotly_chart(fig)

    elif plot_type == 'Histogram':
        fig = px.histogram(df, x=x_column, title=f'Histogram of {x_column}')
        st.plotly_chart(fig)

    elif plot_type == 'Box Plot':
        fig = px.box(df, x=x_column, y=y_column, title=f'Box Plot of {y_column} by {x_column}')
        st.plotly_chart(fig)

    elif plot_type == 'Violin Plot':
        fig = px.violin(df, x=x_column, y=y_column, title=f'Violin Plot of {y_column} by {x_column}')
        st.plotly_chart(fig)

    elif plot_type == 'Pie Chart':
        fig = px.pie(df, names=x_column, values=y_column, title=f'Pie Chart of {y_column} by {x_column}')
        st.plotly_chart(fig)

else:
    st.write("### Please upload a CSV file to get started!")

# Limitations Section
st.markdown("---")
st.markdown('<div class="section-title">Limitations</div>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
- Data Types: The app currently assumes that the selected columns are numeric for plotting. Non-numeric data types may cause errors.<br>
- File Size: Large CSV files may lead to performance issues or crashes during data processing.<br>
- Customization: Limited options for customizing plot appearance and styles.<br>
- Error Handling: Minimal error handling for invalid inputs or unsupported data formats.<br>
- Chart Options: While there are several chart types available, more advanced visualizations are not included.
</div>
""", unsafe_allow_html=True)

# Future Improvements
st.markdown('<div class="section-title">Future Improvements</div>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
We plan to address these limitations by:<br>
- Adding support for different data types and better error handling.<br>
- Optimizing the app to handle larger datasets.<br>
- Expanding the customization options for charts.<br>
- Incorporating more advanced visualizations and interactivity.
</div>
""", unsafe_allow_html=True)

