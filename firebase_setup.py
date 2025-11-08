import firebase_admin
from firebase_admin import credentials, firestore
import os, json

if "FIREBASE_KEY" in os.environ:
    # Read key from environment (Render)
    key_dict = json.loads(os.environ["FIREBASE_KEY"])
    cred = credentials.Certificate(key_dict)
else:
    # Local fallback for your PC
    cred = credentials.Certificate("nyayasakhi-key.json")

firebase_admin.initialize_app(cred)
db = firestore.client()
