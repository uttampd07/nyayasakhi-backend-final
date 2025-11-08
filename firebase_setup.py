import firebase_admin
from firebase_admin import credentials, firestore
import os, json

if "979070ab24c9f4b7d9785d254359d810d8f11b88" in os.environ:
    # Read key from environment (Render)
    key_dict = json.loads(os.environ["979070ab24c9f4b7d9785d254359d810d8f11b88"])
    cred = credentials.Certificate(key_dict)
else:
    # Local fallback for your PC
    cred = credentials.Certificate("nyayasakhi-key.json")

firebase_admin.initialize_app(cred)
db = firestore.client()
