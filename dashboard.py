import streamlit as st
import pandas as pd

# Set page title
st.title('Malaria Cases Dashboard')

# Load data
csv_file_path = 'malaria_cases.csv'
df = pd.read_csv(csv_file_path)

# Display raw data
st.subheader('Raw Data')
st.write(df)

# Aggregate data by state
state_summary = df.groupby('State').agg(
    Total_Users=pd.NamedAgg(column='State', aggfunc='count'),
    Positive_Cases=pd.NamedAgg(column='Malaria_diagnosis', aggfunc=lambda x: (x == 'The person is affected with Malaria 😷').sum()),
    Negative_Cases=pd.NamedAgg(column='Malaria_diagnosis', aggfunc=lambda x: (x == 'The person is not affected with Malaria 😊').sum())
).reset_index()

# Display summary data
st.subheader('State Summary')
st.write(state_summary)

# Visualization (Optional)
st.subheader('Visualization')
st.bar_chart(state_summary.set_index('State'))

# Display the result in a table
st.table(state_summary)
