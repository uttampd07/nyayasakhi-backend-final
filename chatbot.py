from firebase_setup import db
from sentence_transformers import SentenceTransformer, util
import torch

print("🔹 Initializing Chatbot...")

# Load sentence transformer model (offline-friendly)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Fetch all data from Firestore
def fetch_firestore_data():
    print("📥 Fetching legal data from Firestore...")
    data = []
    collections = ["bare_acts", "court_judgments", "legal_articles", "legal_faqs"]
    for c in collections:
        docs = db.collection(c).stream()
        for doc in docs:
            d = doc.to_dict()
            question = d.get("question", d.get("title", ""))
            answer = d.get("answer", d.get("content", ""))
            data.append({
                "text": f"{question} {answer}",
                "answer": answer or "No answer available."
            })
    print(f"✅ Loaded {len(data)} records from Firestore.")
    return data

# Load Firestore data and encode it
data = fetch_firestore_data()
corpus = [d["text"] for d in data]
corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

def get_answer(query):
    query_emb = model.encode(query, convert_to_tensor=True)
    result = util.semantic_search(query_emb, corpus_embeddings, top_k=1)[0][0]
    best_match = data[result['corpus_id']]
    return best_match["answer"]
