🚀 GeminiChats – AI Chatbot with Google Gemini API

GeminiChats is a chatbot web application powered by Google Gemini API.
It uses a Flask backend and a clean HTML/JavaScript frontend, with features like multiple chat sessions, chat history, themes, zoom options, and a loading spinner for smooth UX.

✨ Features

✅ Chat with Google Gemini (LLM)

✅ Multiple chat sessions (New chat / Delete chat)

✅ Chat history support

✅ Themes (Default, Dark, Light, Blue)

✅ Zoom in / Zoom out options

✅ Loading spinner for AI responses

✅ Simple, responsive UI


📂 Project Structure
GeminiChats/
│
├── app.py              # Flask backend with Gemini API integration
├── templates/
│   └── index.html      # Frontend (chat UI)
├── static/
│   └── 5353685.png     # Profile image
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation



Installation & Setup
1. Clone the repo
git clone https://github.com/your-username/GeminiChats.git
cd GeminiChats

2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

3. Install dependencies
pip install -r requirements.txt

4. Set up API key

Create a .env file in the project root:

GOOGLE_API_KEY=your_api_key_here

5. Run the Flask app
python app.py

6. Open in browser

Navigate to:

http://127.0.0.1:5000/

🛠️ Tech Stack

Backend: Python, Flask, Google Generative AI SDK

Frontend: HTML, CSS, JavaScript

API: Google Gemini (via AI Studio)

📸 Screenshot

https://github.com/shubhkh/Generative-Ai-Projects/blob/main/Builing%20a%20chatbot%20with%20google%20gemini%20api/Screenshot%202025-10-03%20085505.png

🚧 Future Enhancements

💾 Persistent chat storage (database)

🔊 Voice input/output support

🌐 Deploy on Render / Vercel / Google Cloud

🙌 Author

👤 Shubham Khedekar
💼 Data Scientist | AI/ML Enthusiast
