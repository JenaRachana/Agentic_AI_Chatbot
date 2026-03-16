#step-1 :Setup UI with streamlit (model provider, model, system prompt, query)
import streamlit as st

st.set_page_config(page_title="LanGgraph Agent UI",layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with AI Agents")

system_prompt = st.text_area("Define you AI Agent:", height =70, placeholder="Type your sytem prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile","mistral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider",("Groq","OpenAI"))

if provider == "Groq":
    select_model = st.selectbox("Select Groq Model:",MODEL_NAMES_GROQ)
if provider == "OpenAI":
    select_model = st.selectbox("Select OpenAI Model:",MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow web Search")

user_query = st.text_area("Enter you query:",height = 150,placeholder="Ask Anything!")



API_URL =  "http://127.0.0.1:8000/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        #step-2 :Connect with backend via URL
        import requests

        payload = {
            "model_name": select_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])

            st.subheader("Agent Response")
            st.markdown(f"**Final Response :**{response_data}")
