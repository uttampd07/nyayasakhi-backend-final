import firebase_admin
from firebase_admin import credentials, firestore

# Load the key file (make sure filename matches the one you downloaded)
cred = credentials.Certificate("nyayasakhi-key.json")

# Initialize the Firebase app
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()
