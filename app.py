import streamlit as st
import pandas as pd
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Streamlit app setup
st.set_page_config(page_title="DataViz AI", layout="wide")
st.title("📊 LLM-Powered Data Visualization App")

# Upload CSV or Excel
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx", "xls"])
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")
        st.write("📄 Preview of your data:")
        st.dataframe(df)

        # OpenAI API Key input
        st.sidebar.title("🔐 API Settings")
        api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
        if not api_key:
            st.warning("⚠️ Please enter your OpenAI API Key.")
            st.stop()
        os.environ["OPENAI_API_KEY"] = api_key

        # Initialize LLM agent
        llm = ChatOpenAI(temperature=0, model="gpt-4")
        agent = create_pandas_dataframe_agent(llm, df, verbose=True)

        # Ask questions
        st.subheader("💬 Ask a question about your data")
        user_query = st.text_input("E.g., Plot sales trend over time")

        if user_query:
            with st.spinner("🔍 Generating response..."):
                try:
                    code_output = agent.run(user_query)
                    st.subheader("✅ Answer / Output:")
                    st.write(code_output)

                    st.subheader("📜 Generated Python Code:")
                    with st.expander("Click to view code"):
                        st.code(code_output, language="python")

                    # Attempt to execute code if it's a code string
                    try:
                        exec(code_output)
                    except Exception as e:
                        st.error(f"⚠️ Error while executing generated code:\n{e}")

                except Exception as e:
                    st.error(f"⚠️ Error while generating response:\n{e}")

    except Exception as e:
        st.error(f"⚠️ Error loading file:\n{e}")