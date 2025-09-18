# Imports
import os
import json
import re
from dotenv import load_dotenv
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Initialize LLM (Gemini)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2  # lower temperature for structured output
)

# Prompt template
PROMPT_TEMPLATE = """
You are an expert resume parser. Given the resume text, extract the following fields
and return a single valid JSON object:

{{
    "Name": "...",
    "Email": "...",
    "Phone": "...",
    "LinkedIn": "...",
    "Skills": [...],
    "Education": [...],
    "Experience": [...],
    "Projects": [...],
    "Certifications": [...],
    "Languages": [...]
}}

Rules:
- If a field cannot be found, set its value to "No idea".
- Return ONLY valid JSON (no markdown, no commentary).
- Keep lists as arrays, and keep Experience/Projects as arrays of short strings.

Resume text:
{text}
"""
prompt = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["text"])


# Resume loader function
def load_resume_docs(uploaded_file):
    temp_path = f"temp_{uploaded_file.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if uploaded_file.name.endswith(".pdf"):
        loader = PyPDFLoader(temp_path)
    elif uploaded_file.name.endswith(".docx"):
        loader = Docx2txtLoader(temp_path)
    elif uploaded_file.name.endswith(".txt"):
        loader = TextLoader(temp_path)
    else:
        return None
    return loader.load()


# JSON safe parser
def safe_json_parse(response_content: str):
    """Extract and parse JSON from model response safely."""
    raw = response_content.strip()

    # Extract only the JSON block if extra text is added
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if match:
        raw = match.group(0)

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


# Streamlit app
def main():
    st.set_page_config(page_title="Resume Parser", page_icon="📄", layout="centered")

    st.title("📄 Resume Parser - LangChain + Gemini")

    uploaded_file = st.file_uploader("Upload resume", type=["pdf", "docx", "txt"])

    if uploaded_file:
        with st.spinner("📂 Loading resume..."):
            docs = load_resume_docs(uploaded_file)
            if not docs:
                st.error("Unsupported file type.")
                return

        if st.button("🔍 Parse Resume with LLM"):
            with st.spinner("🤖 Extracting details..."):
                full_text = "\n\n".join([d.page_content for d in docs])
                formatted_prompt = prompt.format(text=full_text)

                response = llm.invoke(formatted_prompt)
                parsed_json = safe_json_parse(response.content)

                if parsed_json:
                    st.subheader("✅ Parsed Resume Data")
                    st.json(parsed_json)
                else:
                    st.error("⚠️ LLM did not return valid JSON.")
                    st.write(response.content)


if __name__ == "__main__":
    main()
