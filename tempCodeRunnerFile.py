import streamlit as st
import pandas as pd

st.set_page_config(page_title="LLM Data Visualizer", layout="wide")
st.title("📊 LLM-Powered Data Visualizer")

# Upload CSV or Excel file
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

# Display the file
if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())

from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent

if uploaded_file:
    st.subheader("Ask questions about your data")
    question = st.text_input("Enter your question:")

    if question:
        # Create LangChain OpenAI LLM instance
        llm = OpenAI(temperature=0, openai_api_key=None)  # We'll use env variable

        # Create Pandas dataframe agent
        agent = create_pandas_dataframe_agent(llm, df, verbose=True)

        # Run the question through the agent
        response = agent.run(question)
        
        st.markdown("### Answer:")
        st.write(response)
