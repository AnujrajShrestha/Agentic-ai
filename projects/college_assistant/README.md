# 🎓 AI College Assistant

An intelligent **College Assistant** built using **LangGraph**, **LangChain**, **Mistral AI**, **FAISS**, and **Streamlit**. The assistant answers students' questions by retrieving information from official college documents such as the **Academic Handbook** and **Fee Structure**, while also handling general queries through an LLM.

---

## ✨ Features

* 📘 Academic Handbook Question Answering
* 💰 Fee Structure Question Answering
* 🤖 General College Assistant
* 🔀 Intelligent Query Routing using LangGraph
* 📄 Retrieval-Augmented Generation (RAG)
* ⚡ FAISS Vector Database
* 🎓 Personalized Responses based on Student Programme
* 💬 Chat Interface with Streamlit
* 🧠 Mistral AI Embeddings & LLM

---

## 🛠️ Tech Stack

| Technology                     | Purpose               |
| ------------------------------ | --------------------- |
| Python                         | Programming Language  |
| LangChain                      | LLM Framework         |
| LangGraph                      | Agent Workflow        |
| Mistral AI                     | LLM & Embeddings      |
| FAISS                          | Vector Database       |
| Streamlit                      | Web Interface         |
| PyPDFLoader                    | PDF Loading           |
| RecursiveCharacterTextSplitter | Document Chunking     |
| dotenv                         | Environment Variables |

---

## 📂 Project Structure

```text
college-assistant/
│
├── agentic.py                 # LangGraph workflow
├── db.py                      # PDF loading & FAISS retrievers
├── app.py                     # Streamlit UI
├── pipeline.py                # CLI version
│
├── academics_handbook.pdf
├── fee_structure.pdf
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Workflow

```text
                User Question
                      │
                      ▼
              LangGraph Classifier
                      │
      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼
 Academic RAG      Fee RAG        General LLM
      │               │               │
      └───────────────┼───────────────┘
                      ▼
              Response Generator
                      │
                      ▼
                 Final Answer
```

---

## 🧠 How It Works

### 1. Query Classification

The assistant first classifies the student's question into one of three categories:

* Academic
* Fee
* General

---

### 2. Retrieval

Depending on the classification:

* Academic questions search the **Academic Handbook**
* Fee-related questions search the **Fee Structure**
* General questions are answered directly by the LLM

---

### 3. Response Generation

The retrieved context and the student's programme (BCA, BBA, or B.Com (H)) are provided to the language model to generate an accurate, personalized response.

---

## 🚀 Installation

### Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file.

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run the Streamlit Application

```bash
streamlit run app.py
```

---

## ▶️ Run the CLI Version

```bash
python pipeline.py
```

---

## 💬 Example Questions

### Academic

* What is the minimum attendance requirement?
* How many credits are required to graduate?
* What are the examination rules?
* What is the grading system?

### Fee

* What is the tuition fee for BCA?
* Is there any late payment penalty?
* What is the refund policy?
* When should fees be paid?

### General

* Hello
* Who are you?
* What can you help me with?
* Thank you

---

## 📸 Screenshots

Add screenshots here after running the application.

```
screenshots/
├── home.png
├── chat.png
└── sidebar.png
```

---

## 📌 Future Improvements

* Conversation Memory
* Persistent FAISS Index
* Multiple College Policies
* Hostel Handbook Support
* Scholarship Information
* Library Rules
* Faculty Directory
* Source Citation with Page Numbers
* Voice Input
* Chat Export (PDF/Markdown)
* Authentication System
* Admin Dashboard

---

## 🎯 Learning Highlights

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* LangGraph Conditional Workflows
* State Management
* Prompt Engineering
* Document Retrieval
* FAISS Vector Search
* Mistral AI Integration
* Streamlit Deployment
* Modular Project Architecture

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Anuj Shrestha**

* GitHub: https://github.com/AnujrajShrestha
* Location: Butwal, Nepal

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
