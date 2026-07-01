import gradio as gr

# =====================================================
# Imports for LlamaIndex and LangChain
# =====================================================
from llama_index.readers.file import PDFReader
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from langchain_openai import ChatOpenAI
import os

# Ensure OPENAI_API_KEY is set (from previous cells)
os.environ['OPENAI_API_KEY'] = " "

# Global variable to store the LlamaIndex
resume_index = None

# =====================================================
# Function to upload and process PDF
# =====================================================
def upload_pdf(file_obj):
    global resume_index
    if file_obj is None:
        return "Error: Please upload a PDF file."

    try:
        # Gradio File component provides a NamedTemporaryFile, so get its name
        filepath = file_obj.name
        reader = PDFReader()
        documents = reader.load_data(file=filepath)

        # Build index
        resume_index = VectorStoreIndex.from_documents(documents)
        return "Resume processed successfully! You can now ask questions."
    except Exception as e:
        return f"Error processing resume: {e}"

# =====================================================
# Function to chat with the PDF content
# =====================================================
def chat_with_pdf(question):
    global resume_index
    if resume_index is None:
        return "Please upload and process your resume first."

    try:
        query_engine = resume_index.as_query_engine()
        response = query_engine.query(question)
        return response.response
    except Exception as e:
        return f"Error querying resume: {e}"

# =====================================================
# Custom CSS
# =====================================================

css = """
.gradio-container{
    max-width:1200px !important;
    margin:auto;
    padding:10px !important;
}

footer{
    display:none !important;
}

h1,h2,h3{
    text-align:center;
    margin:4px 0px !important;
}

button{
    border-radius:10px !important;
    height:42px !important;
}

.gr-textbox textarea{
    border-radius:10px !important;
}

.gr-file{
    border-radius:10px !important;
}

#answer textarea{
    min-height:320px !important;
    max-height:320px !important;
    font-size:15px !important;
}
"""

# =====================================================
# UI
# =====================================================

with gr.Blocks(css=css, title="Resume AI Assistant") as demo:

    gr.Markdown(
        """
        # 🤖 Resume AI Assistant
        Upload your resume and ask anything about it.
        """
    )

    # =================================================
    # Upload Row
    # =================================================

    with gr.Row():

        pdf = gr.File(
            label="📄 Upload Resume",
            file_types=[".pdf"],
            scale=4
        )

        upload_btn = gr.Button(
            "🚀 Process Resume",
            variant="primary",
            scale=2
        )

        status = gr.Textbox(
            label="Status",
            interactive=False,
            scale=3
        )

    # =================================================
    # Question
    # =================================================

    question = gr.Textbox(
        label="💬 Ask a Question",
        placeholder="Ask anything about your resume...",
        lines=2
    )

    with gr.Row():

        ask_btn = gr.Button(
            "📤 Submit",
            variant="primary"
        )

        clear_btn = gr.Button(
            "🗑 Clear"
        )

    # =================================================
    # Bottom Section
    # =================================================

    with gr.Row():

        # ------------------------
        # Suggested Questions
        # ------------------------

        with gr.Column(scale=1):

            gr.Markdown("### 💡 Suggested Questions")

            q1 = gr.Button("📄 Summarize")
            q2 = gr.Button("💻 Skills")
            q3 = gr.Button("📂 Projects")
            q4 = gr.Button("🎓 Education")
            q5 = gr.Button("⭐ Certifications")
            q6 = gr.Button("📝 Improve Resume")

        # ------------------------
        # AI Answer
        # ------------------------

        with gr.Column(scale=2):

            answer = gr.Textbox(
                label="🤖 AI Answer",
                value="Your AI answer will appear here...",
                interactive=False,
                lines=15,
                elem_id="answer"
            )

    # =================================================
    # Events
    # =================================================

    upload_btn.click(
        fn=upload_pdf,
        inputs=pdf,
        outputs=status
    )

    ask_btn.click(
        fn=chat_with_pdf,
        inputs=question,
        outputs=answer
    )

    question.submit(
        fn=chat_with_pdf,
        inputs=question,
        outputs=answer
    )

    clear_btn.click(
        lambda: ("", "Your AI answer will appear here..."),
        outputs=[question, answer]
    )

    # Suggested Questions

    q1.click(
        lambda: "Summarize my resume",
        outputs=question
    )

    q2.click(
        lambda: "What are my technical skills?",
        outputs=question
    )

    q3.click(
        lambda: "List all my projects",
        outputs=question
    )

    q4.click(
        lambda: "Describe my education",
        outputs=question
    )

    q5.click(
        lambda: "What certifications are mentioned in my resume?",
        outputs=question
    )

    q6.click(
        lambda: "Suggest improvements for my resume",
        outputs=question
    )

demo.launch()
