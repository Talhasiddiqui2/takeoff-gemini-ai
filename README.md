# takeoff-gemini-ai
AI-powered document analysis system built using Google Gemini 2.5 Flash and RAG (Retrieval-Augmented Generation) to extract precise measurements and data from project files.

# 🚀 SignsVerse: Take Off Team Portal

An advanced AI-powered document intelligence tool designed for the **SignsVerse** team. This application automates the "Take Off" process by analyzing technical documents, blueprints, and project files to extract specific measurements, costs, and dates instantly.

## 🛠️ How It's Built (Technical Stack)
This project is a custom implementation of **RAG (Retrieval-Augmented Generation)**, which ensures the AI stays "grounded" in your data without hallucinations.

* **Model:** `Google Gemini 2.5 Flash` (via Google GenAI SDK)
* **Frontend:** `Streamlit` (Web Interface)
* **Processing:** `PyMuPDF (fitz)` for high-speed PDF text extraction.
* **Environment:** Python 3.13 Virtual Environment.
* **Security:** `python-dotenv` for secure API key management.

## ✨ Key Features
- **Zero-Manual Search:** Extracts specific technical data points so the team doesn't have to scroll through 100+ pages.
- **Smart Grounding:** The AI is strictly instructed to only answer based on the uploaded file.
- **Fast Processing:** Optimized for large files (up to 25MB) using efficient memory handling.
- **Team Collaboration:** Centralized portal that requires no individual API keys or complex setups for team members.

## 🚀 Getting Started
1. Clone this repository.
2. Add your `GEMINI_API_KEY` to the `.env` file.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the app: `streamlit run app.py`.

---
**Developed by Muhammad Talha Siddiqui **
