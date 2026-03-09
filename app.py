import streamlit as st
from google.genai import Client
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# API Setup
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key missing! Check .env file")
    st.stop()

client = Client(api_key=api_key)

# Page Config
st.set_page_config(page_title="Take Off AI", layout="centered", page_icon="🚀")
st.title("🚀 SignsVerse: Take Off Team Portal")

# Expert Instructions
instruction = """You are the 'Take Off' project expert analyst for SignsVerse.
Extract specific data from uploaded files.
- Mention page numbers
- If missing, say 'Not available'
- Be precise with measurements"""

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = None

# File Upload
uploaded_file = st.file_uploader("Upload PDF/TXT", type=["pdf", "txt"])

if uploaded_file:
    
    # Extract text once
    if st.session_state.extracted_text is None:
        with st.spinner("Processing..."):
            text = ""
            if uploaded_file.type == "application/pdf":
                reader = PdfReader(uploaded_file)
                for i, page in enumerate(reader.pages, 1):
                    page_text = page.extract_text()
                    if page_text:
                        text += f"\n--- Page {i} ---\n{page_text}"
            else:
                text = uploaded_file.read().decode("utf-8")
            
            st.session_state.extracted_text = text[:15000]
            st.success("Document loaded!")

    # Show chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if user_query := st.chat_input("Ask about the document..."):
        
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        with st.chat_message("assistant"):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",  # ✅ Correct Remeber This
                    contents=f"{instruction}\n\nContext: {st.session_state.extracted_text}\n\nQuestion: {user_query}"
                )
                
                ai_response = response.text
                st.markdown(ai_response)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                
            except Exception as e:
                error = str(e)
                if "429" in error:
                    st.error("⏳ Quota exceeded! Wait 1 minute.")   
                elif "404" in error:
                    st.error("❌ Model not found")
                else:
                    st.error(f"Error: {error}")