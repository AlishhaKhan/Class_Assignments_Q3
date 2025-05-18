# app.py
import streamlit as st
import hashlib
import json
from cryptography.fernet import Fernet
import os

# -------------------- SETUP --------------------
DATA_FILE = "data.json"
MASTER_PASSWORD = "admin123"  # Change this in real-world use

# Generate or load encryption key
if not os.path.exists("secret.key"):
    with open("secret.key", "wb") as f:
        f.write(Fernet.generate_key())

with open("secret.key", "rb") as f:
    KEY = f.read()

cipher = Fernet(KEY)
stored_data = {}
failed_attempts = 0

# Load saved data from file
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        stored_data = json.load(file)

# -------------------- FUNCTIONS --------------------
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text, passkey):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    global failed_attempts
    hashed = hash_passkey(passkey)

    entry = stored_data.get(encrypted_text)
    if entry and entry["passkey"] == hashed:
        failed_attempts = 0
        return cipher.decrypt(encrypted_text.encode()).decode()
    
    failed_attempts += 1
    return None

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(stored_data, file)

# -------------------- UI --------------------
st.title("🔐 Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome")
    st.write("Encrypt and decrypt sensitive data securely with a passkey.")

elif choice == "Store Data":
    st.subheader("📁 Store New Data")
    data = st.text_area("Enter data to encrypt")
    passkey = st.text_input("Enter passkey", type="password")

    if st.button("Encrypt & Store"):
        if data and passkey:
            hashed = hash_passkey(passkey)
            encrypted = encrypt_data(data, passkey)
            stored_data[encrypted] = {"encrypted_text": encrypted, "passkey": hashed}
            save_data()
            st.success("✅ Data encrypted and saved.")
            st.text(f"Encrypted Text (Save this): {encrypted}")
        else:
            st.error("⚠️ Both fields are required.")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Data")
    encrypted_input = st.text_area("Enter encrypted text")
    passkey = st.text_input("Enter passkey", type="password")

    if st.button("Decrypt"):
        if encrypted_input and passkey:
            result = decrypt_data(encrypted_input, passkey)
            if result:
                st.success(f"✅ Decrypted Data: {result}")
            else:
                attempts_left = 3 - failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts left: {attempts_left}")
                if failed_attempts >= 3:
                    st.warning("🔒 Too many attempts! Go to Login.")
                    st.experimental_rerun()
        else:
            st.error("⚠️ Fill both fields.")

elif choice == "Login":
    st.subheader("🔐 Reauthorization")
    login = st.text_input("Enter Master Password", type="password")
    if st.button("Login"):
        if login == MASTER_PASSWORD:
            failed_attempts = 0
            st.success("✅ Reauthorized! Try retrieving again.")
            st.experimental_rerun()
        else:
            st.error("❌ Wrong password.")
