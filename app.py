from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configure Streamlit page
st.set_page_config(page_title="Search GPT", page_icon="🔍")

# UI for the app
st.title("Search GPT 🔍")
st.write(
    "Chat GPT with real-time internet search capabilities. "
)

# Add spacing with st.write() OR with custom HTML & CSS using st.markdown()
# st.write("")  # Empty string for line space/gap
st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)

prompt = "Please answer this question in detail: "

# Get user input
prompt += st.text_input("Ask your question here...")
button = st.button("Search")

# Initialize LLM
llm = OpenAI(temperature=0.7, openai_api_key=os.getenv('OPENAI_API_KEY'))

# Load tools
tool_names = ['serpapi']
tools = load_tools(tool_names)

# Initialize agent
agent = initialize_agent(tools, llm, agent='zero-shot-react-description', verbose=True)

# Process user input
if button:
    with st.spinner("Searching..."):
        try:
            response = agent.run(prompt)
            st.write(response)
        except Exception as e:
            st.write("An error occured")
