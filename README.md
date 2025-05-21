# 📊 LLM-Powered Data Visualization App

This Streamlit app lets you upload a CSV or Excel file and ask natural language questions about your data. It uses OpenAI's GPT-4 model (via LangChain) to generate Python code to analyze and visualize your dataset dynamically.

---

## Features

- Upload CSV or Excel files for data exploration  
- Natural language questions about your data  
- Generates and executes Python visualization code  
- Displays results and the generated code  
- Secure API key input via sidebar  

---

## Requirements

- Python 3.8+  
- [Streamlit](https://streamlit.io/)  
- pandas  
- openai  
- langchain-core  
- langchain-openai  
- python-dotenv  

---

## Installation

1. Clone the repo:

bash
git clone https://github.com/yourusername/dataviz-ai.git
cd dataviz-ai

2. Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt

3. Create a .env file or enter your OpenAI API key in the app sidebar.

4. Usage
Run the app with:

bash
Copy
Edit
streamlit run app.py
Upload your dataset (CSV or Excel)

Enter your OpenAI API key in the sidebar

Ask questions like: "Plot sales trend over time"

View the generated answer and Python code

5. Notes
Make sure your OpenAI API key has access to GPT-4.

Execution of generated code is done dynamically and may raise errors depending on the output.



# Do's and Don'ts

## Do's
✅ Use well-structured CSV or Excel files for best results.

✅ Keep your OpenAI API key secure and do not share it publicly.

✅ Ask clear and specific questions about your data for accurate responses.

✅ Review generated Python code before executing, especially if modifying it.

✅ Test the app with smaller datasets first to ensure smooth performance.

## Don'ts
❌ Don’t upload sensitive or confidential data without proper authorization.

❌ Don’t share your OpenAI API key or commit it to public repos.

❌ Don’t expect 100% error-free code generation — AI-generated code may require manual adjustment.

❌ Don’t run the app without an active internet connection (required for OpenAI API).

❌ Don’t input ambiguous or vague questions — it reduces answer quality.

