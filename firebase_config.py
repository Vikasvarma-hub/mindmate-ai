import firebase_admin
from firebase_admin import credentials, db, auth

import firebase_admin
from firebase_admin import credentials, db
import streamlit as st

def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(dict(st.secrets["firebase"]))
        firebase_admin.initialize_app(
            cred,
            {"databaseURL": st.secrets["firebase_database_url"]}
        )

def get_db_reference(path="/"):
    init_firebase()
    return db.reference(path)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://mentalmadhilo-6900d-default-rtdb.firebaseio.com/"
    })

def get_db_reference(path):
    return db.reference(path)
