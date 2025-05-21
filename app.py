import wikipedia
import gradio as gr
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import os

token = os.getenv("HF_TOKEN")  # fetch token from Hugging Face Secrets

# Load models
embedding_model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2", token=token)
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", tokenizer="deepset/roberta-base-squad2", token=token)

# Helper to chunk large text
def chunk_text(text, max_length=256, overlap=20):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + max_length, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += max_length - overlap
    return chunks

# Main function for RAG
def rag_pipeline(topic, question):
    try:
        doc = wikipedia.page(topic).content
    except:
        return "❌ Could not retrieve Wikipedia content.", ""

    chunks = chunk_text(doc)
    embeddings = embedding_model.encode(chunks, convert_to_numpy=True)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    query_embedding = embedding_model.encode([question])
    distances, indices = index.search(np.array(query_embedding), k=3)

    retrieved_chunks = [chunks[i] for i in indices[0]]
    context = " ".join(retrieved_chunks)

    answer = qa_pipeline(question=question, context=context)["answer"]
    return answer, "\n\n---\n\n".join(retrieved_chunks)

# Gradio UI
iface = gr.Interface(
    fn=rag_pipeline,
    inputs=[
        gr.Textbox(label="📘 Wikipedia Topic", placeholder="e.g. Artificial Intelligence"),
        gr.Textbox(label="❓ Your Question", placeholder="e.g. What is AI used for?")
    ],
    outputs=[
        gr.Textbox(label="🧠 Answer"),
        gr.Textbox(label="📚 Retrieved Context")
    ],
    title="🔍 Wikipedia RAG QA",
    description="Ask any question on a Wikipedia topic using a Retrieval-Augmented Generation (RAG) pipeline"
)

iface.launch()
