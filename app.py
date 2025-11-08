from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_answer
from firebase_setup import db

app = Flask(__name__)
CORS(app)  # enable frontend-backend communication

@app.route('/')
def home():
    return "⚖️ NyayaSakhi Flask Backend is Running Successfully!"

# ---------- CHATBOT API ----------
@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_query = request.json.get("query", "")
        if not user_query:
            return jsonify({"error": "Query is missing"}), 400
        answer = get_answer(user_query)
        return jsonify({"response": answer})
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500


# ---------- DOCUMENT GENERATOR API ----------
@app.route('/generate_document', methods=['POST'])
def generate_document():
    try:
        data = request.get_json()
        doc_type = data.get("type", "FIR").upper()
        name = data.get("name", "User")
        
        if doc_type == "FIR":
            document = f"FIR Report\nComplainant: {name}\nDetails: ... (fill your details here)"
        elif doc_type == "RTI":
            document = f"RTI Application\nApplicant: {name}\nSubject: Request for Information..."
        elif doc_type == "COMPLAINT":
            document = f"Formal Complaint by {name}\nDetails of Incident: ..."
        else:
            document = f"{doc_type} Document generated for {name}"

        return jsonify({"document": document})
    except Exception as e:
        print("Error generating document:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
