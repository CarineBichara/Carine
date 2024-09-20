import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Full path to the Excel file
file_path = r'C:\Users\User\Downloads\data.xlsx'

# Check if the file exists
if os.path.exists(file_path):
    try:
        # Load the Excel file
        data = pd.read_excel(file_path)

        # Display the first few rows of the data
        st.write("Data Preview:")
        st.write(data.head())

        # Verify column names
        st.write("Column Names:")
        st.write(data.columns)

        # Town selection
        if 'Town' in data.columns:
            town = st.selectbox("Select Town", data['Town'].unique())
            filtered_data = data[data['Town'] == town]
        else:
            st.error("Column 'Town' not found in data.")
            filtered_data = data  # Fallback to show all data if 'Town' is missing

        # Scatter Plot
        if 'Potable water source - artesian well' in data.columns and 'State of the water network - good' in data.columns:
            scatter_fig = px.scatter(
                data,
                x='Potable water source - artesian well',
                y='State of the water network - good',
                color='Town',
                title='Scatter Plot Example'
            )
            scatter_fig.update_layout(
                xaxis_title='Potable Water Source - Artesian Well',
                yaxis_title='State of the Water Network - Good'
            )
            st.subheader('Scatter Plot')
            st.plotly_chart(scatter_fig)
        else:
            st.write("Scatter Plot: Required columns not found in data.")

        # Pie Chart
        if 'Town' in data.columns and 'Potable water source - artesian well' in data.columns:
            pie_fig = px.pie(
                data,
                names='Town',
                values='Potable water source - artesian well',
                title='Pie Chart Example'
            )
            pie_fig.update_layout(
                margin=dict(l=50, r=50, t=50, b=50)
            )
            st.subheader('Pie Chart')
            st.plotly_chart(pie_fig)
        else:
            st.write("Pie Chart: Required columns not found in data.")

        # Line Chart
        if 'Town' in data.columns and 'State of the water network - good' in data.columns:
            line_fig = px.line(
                data,
                x='Town',
                y='State of the water network - good',
                title='Line Chart: State of Water Network by Town'
            )
            line_fig.update_layout(
                xaxis_title='Town',
                yaxis_title='State of the Water Network - Good'
            )
            st.subheader('Line Chart')
            st.plotly_chart(line_fig)
        else:
            st.write("Line Chart: Required columns not found in data.")

        # 3D Scatter Plot
        if {'Potable water source - artesian well', 'State of the water network - good', 'Total number of seasonal water springs'}.issubset(data.columns):
            fig_3d = px.scatter_3d(
                data,
                x='Potable water source - artesian well',
                y='State of the water network - good',
                z='Total number of seasonal water springs',
                color='Town',
                title='3D Scatter Plot Example'
            )
            fig_3d.update_layout(
                scene=dict(
                    xaxis_title='Potable Water Source - Artesian Well',
                    yaxis_title='State of the Water Network - Good',
                    zaxis_title='Total Number of Seasonal Water Springs'
                )
            )
            st.subheader('3D Scatter Plot')
            st.plotly_chart(fig_3d)
        else:
            st.write("3D Scatter Plot: Required columns not found in data.")

        # Bar Chart
        if 'Town' in data.columns and 'Potable water source - artesian well' in data.columns:
            bar_fig = px.bar(
                data,
                x='Town',
                y='Potable water source - artesian well',
                title='Bar Chart Example'
            )
            bar_fig.update_layout(
                xaxis_title='Town',
                yaxis_title='Potable Water Source - Artesian Well'
            )
            st.subheader('Bar Chart')
            st.plotly_chart(bar_fig)
        else:
            st.write("Bar Chart: Required columns not found in data.")

    except ValueError as e:
        st.error(f"ValueError: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.error(f"File not found: {file_path}")
