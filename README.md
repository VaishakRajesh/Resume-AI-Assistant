# 🤖 Resume AI Assistant

Resume AI Assistant is an AI-powered web application built with **Gradio**, **LlamaIndex**, and **OpenAI** that allows users to upload a resume (PDF) and ask natural language questions about its content.

The application extracts text from the uploaded resume, creates a vector index using LlamaIndex, and answers user queries using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 Upload Resume in PDF format
- 🤖 AI-powered Question Answering
- 📋 Resume Summary
- 💻 Extract Technical Skills
- 📂 List Projects
- 🎓 Show Education Details
- ⭐ Display Certifications
- 📝 Resume Improvement Suggestions
- 🎨 Modern Gradio Interface with Custom CSS

---

## 🛠 Technologies Used

- Python
- Gradio
- LlamaIndex
- OpenAI GPT
- LangChain
- PDFReader

---

## 📂 Project Structure

```
Resume-AI-Assistant/
│
├── app.py                 # Main application
├── requirements.txt       # Required packages
├── README.md              # Project documentation
└── sample_resume.pdf      # (Optional) Sample resume
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/resume-ai-assistant.git

cd resume-ai-assistant
```

### 2. Create Virtual Environment (Recommended)

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install gradio llama-index langchain-openai pypdf
```

---

## 🔑 Configure OpenAI API Key

Replace

```python
os.environ['OPENAI_API_KEY'] = "YOUR_OPENAI_API_KEY"
```

with your own API key.

Alternatively, set it as an environment variable:

Windows

```bash
set OPENAI_API_KEY=your_api_key
```

Linux / macOS

```bash
export OPENAI_API_KEY=your_api_key
```

---

## ▶️ Run the Application

```bash
python app.py
```

The application will launch locally and display a URL similar to:

```
http://127.0.0.1:7860
```

Open it in your browser.

---

## 🧠 How It Works

1. User uploads a PDF resume.
2. The PDF is read using **PDFReader**.
3. LlamaIndex converts the document into embeddings.
4. A Vector Store Index is created.
5. User asks a question.
6. The query engine retrieves relevant information.
7. OpenAI generates an accurate response based on the resume.

---

## 💬 Example Questions

- Summarize my resume.
- What are my technical skills?
- List all my projects.
- Describe my education.
- What certifications are mentioned?
- Suggest improvements for my resume.
- What programming languages do I know?
- What is my work experience?
- Which technologies have I used?

---

## 🎨 User Interface

The interface includes:

- Resume Upload Section
- Processing Status
- Question Input Box
- AI Response Panel
- Suggested Question Buttons
- Responsive Layout
- Custom Styling with CSS

---

## 📸 Screenshot

Add a screenshot of your application here.

```
images/screenshot.png
```

---

## 📋 Requirements

- Python 3.10+
- Gradio
- LlamaIndex
- LangChain OpenAI
- OpenAI API Key

---

## 🔒 Limitations

- Supports only PDF resumes.
- Requires an active internet connection for OpenAI API.
- API usage may incur costs depending on your OpenAI plan.

---

## 🚀 Future Improvements

- Support DOCX resumes
- Chat history
- Resume comparison
- Download AI responses
- Multiple resume uploads
- Dark mode
- Voice-based questions
- ATS score analysis
- Cover letter generation

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed using:

- Python
- Gradio
- LlamaIndex
- OpenAI
- LangChain

---

## ⭐ If You Like This Project

If you found this project useful, consider giving it a ⭐ on GitHub.
