📄 Resume Parser App (LangChain + Gemini)
🚀 Project Overview

This project is a Resume Parser Application that extracts structured information (Name, Email, Skills, Education, Experience, Projects, Certifications, etc.) from resumes in PDF, DOCX, or TXT format.

It uses LangChain with Google Gemini LLM for natural language processing and Streamlit for the user interface.

✨ Features

Upload resumes in PDF, DOCX, or TXT formats

Extracts key fields like:

Name

Email

Phone

LinkedIn

Skills

Education

Experience

Projects

Certifications

Languages

Displays results in a clean JSON format

User-friendly Streamlit UI

🛠️ Tech Stack

Python 3.10+

LangChain

Google Gemini (Generative AI)

Streamlit

dotenv

PyPDFLoader, Docx2txtLoader, TextLoader

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/resume-parser-app.git
cd resume-parser-app


Create & activate a virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux


Install dependencies:

pip install -r requirements.txt


Add your Google API Key to a .env file:

GOOGLE_API_KEY=your_api_key_here

▶️ Usage

Run the Streamlit app:

streamlit run resume_parser_app.py


Then open http://localhost:8501
 in your browser.

📸 Screenshots (Optional)

(Add screenshots of your Streamlit app UI here to impress recruiters!)

Example:


📊 Example Output
{
  "Name": "John Doe",
  "Email": "john.doe@example.com",
  "Phone": "+1-234-567-890",
  "LinkedIn": "https://linkedin.com/in/johndoe",
  "Skills": ["Python", "Machine Learning", "SQL"],
  "Education": ["MCA - XYZ University"],
  "Experience": ["Data Scientist at ABC Corp (2022 - Present)"],
  "Projects": ["Resume Parser App", "Movie Recommendation System"],
  "Certifications": ["Google Data Analytics", "AWS Cloud Practitioner"],
  "Languages": ["English", "Hindi"]
}

💡 Future Improvements

Add support for more resume formats

Improve field extraction accuracy

Export parsed results to CSV / Excel

Integrate with ATS (Applicant Tracking Systems)

🤝 Contributing

Contributions are welcome! Fork the repo and create a PR.

📜 License

This project is licensed under the MIT License.

👉 Pro tip: On GitHub, also add

Project description (at the top of the repo)

Tags like #resume-parser #AI #LangChain #Streamlit

Pinned repo on your GitHub profile
