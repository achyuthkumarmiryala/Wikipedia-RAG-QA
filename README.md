# 🔍 Wikipedia RAG QA

A lightweight **Retrieval-Augmented Generation (RAG)** system that answers natural-language questions on any Wikipedia topic.  
It combines dense vector retrieval (FAISS + Sentence Transformers) with a Hugging Face question-answering model, wrapped in a friendly Gradio interface.

> **Live demo:** [Try it on Hugging Face Spaces](https://achyuthkumarmiryala-rag-wikipedia-qa.hf.space)

---

## ✨ Features
- **Real-time Wikipedia retrieval** – pulls the latest content directly from Wikipedia’s API.  
- **Semantic search** – encodes text with `all-mpnet-base-v2` and finds the most relevant passages using FAISS.  
- **Accurate answers** – generates concise answers with `deepset/roberta-base-squad2`.  
- **Transparent context** – displays the retrieved passages so users see exactly where the answer came from.  
- **One-file deploy** – run locally or publish to Hugging Face Spaces with the same `app.py`.

---

## 🚀 Quick Start

```bash
# 1️⃣  Clone the repo
git clone https://github.com/achyuthkumarmiryala/Wikipedia-RAG-QA.git
cd Wikipedia-RAG-QA

# 2️⃣  (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3️⃣  Install dependencies
pip install -r requirements.txt

# 4️⃣  Run the app locally
python app.py
```

Then open the local Gradio link in your browser (e.g. `http://127.0.0.1:7860`).

---

## 🗂️ Repository Structure
```
Wikipedia-RAG-QA/
│
├── app.py                       # Gradio app + RAG pipeline
├── RAG_Pipeline_for_LLMs.ipynb  # Annotated notebook explaining each step
├── requirements.txt             # Python dependencies
├── README.md                    # You are here
└── .gitignore                   # Standard Python ignores
```

---

## 🛠️ Tech Stack
| Layer            | Tool / Model                              |
|------------------|-------------------------------------------|
| **UI**           | Gradio                                    |
| **Retriever**    | FAISS (L2 similarity search)              |
| **Embeddings**   | Sentence Transformers `all-mpnet-base-v2` |
| **Generator**    | `deepset/roberta-base-squad2` QA model    |
| **Data Source**  | `wikipedia` Python package                |
| **Hosting**      | Hugging Face Spaces                       |

---

## 📚 How It Works
1. **Fetch Article** – Retrieve full text of the chosen Wikipedia page.  
2. **Chunk & Embed** – Split into 256-token overlapping chunks and embed each with Sentence Transformers.  
3. **Index** – Store embeddings in an in-memory FAISS index.  
4. **Retrieve** – Embed the user’s question and grab the top-k (default = 3) most similar chunks.  
5. **Generate** – Feed those chunks + question to a QA model to produce the final answer.  
6. **Display** – Show the answer *and* the supporting passages for transparency.

---

## 🌱 Environment Variables
| Name            | Purpose                                            |
|-----------------|----------------------------------------------------|
| `HF_TOKEN`      | (*Optional*) Hugging Face access token for models. |

If you deploy on Hugging Face Spaces, add `HF_TOKEN` under **Settings → Secrets** for private models or higher rate limits.

---

## 🖼️ Screenshots
> <sup>Add a screenshot or GIF of the Gradio interface here</sup>

---

## 🔭 Roadmap
- [ ] Add cosine similarity option.  
- [ ] Support multi-page retrieval for broader context.  
- [ ] Streamlit or FastAPI backend edition.  
- [ ] Evaluation script for answer quality (EM / F1).

---

## 🙋‍♂️ Author
**Achyuth Kumar Miryala**  
Master’s in Data Science — University of North Texas  
📍 Denton, TX 📫 [achyuthkumar286@gmail.com](mailto:achyuthkumar286@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/achyuthkumarmiryala/) | [GitHub](https://github.com/achyuthkumarmiryala)

---

## 📄 License
This repository is released for academic & educational use only.  
For commercial or extended usage rights, please contact the author.

> If you find this project useful, ⭐ star the repo and share your feedback!
