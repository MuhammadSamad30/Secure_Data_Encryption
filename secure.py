import streamlit as st
import hashlib
import base64
from cryptography.fernet import Fernet, InvalidToken


def get_key(passkey: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(passkey.encode()).digest())


def encrypt(text: str, passkey: str) -> str:
    return Fernet(get_key(passkey)).encrypt(text.encode()).decode()


def decrypt(cipher: str, passkey: str) -> str:
    return Fernet(get_key(passkey)).decrypt(cipher.encode()).decode()


def hash_key(passkey: str) -> str:
    return hashlib.sha256(passkey.encode()).hexdigest()


for k, v in {'data': {}, 'attempts': 0, 'logged_in': False}.items():
    if k not in st.session_state:
        st.session_state[k] = v


def reset_attempts():
    st.session_state.attempts = 0


def home():
    st.title("🔐 Secure Storage App")
    st.markdown("""
    - 💾 Store secret data securely.
    - 🔍 Retrieve using passkey.
    - 🔐 Login after 3 failed attempts.
    """)
    st.info(f"❗ Failed Attempts: {st.session_state.attempts}")
    st.success(
        f"📁 Keys: {list(st.session_state.data.keys()) or 'No data yet'}")


def insert():
    st.title("📥 Store Data")
    key = st.text_input("Key (unique):")
    text = st.text_area("Data:")
    passkey = st.text_input("Passkey:", type="password")

    if st.button("Save"):
        if not key or not text or not passkey:
            st.warning("⚠️ All fields required.")
        elif key in st.session_state.data:
            st.error("⚠️ Key already exists.")
        else:
            try:
                enc = encrypt(text, passkey)
                st.session_state.data[key] = {
                    'enc': enc, 'hash': hash_key(passkey)}
                st.success(f"✅ Saved under key: {key}")
            except Exception as e:
                st.error(f"Error: {e}")


def retrieve():
    st.title("📤 Retrieve Data")

    if st.session_state.attempts >= 3 and not st.session_state.logged_in:
        st.error("⛔ Too many attempts. Login required.")
        return

    key = st.text_input("Key:")
    passkey = st.text_input("Passkey:", type="password")

    if st.button("Get"):
        if not key or not passkey:
            st.warning("⚠️ Provide key and passkey.")
        elif key not in st.session_state.data:
            st.error("❌ Key not found.")
        else:
            entry = st.session_state.data[key]
            if hash_key(passkey) == entry['hash']:
                try:
                    dec = decrypt(entry['enc'], passkey)
                    st.success("✅ Decrypted:")
                    st.code(dec)
                    reset_attempts()
                except InvalidToken:
                    st.error("❌ Invalid passkey.")
                    st.session_state.attempts += 1
            else:
                st.error("❌ Incorrect passkey.")
                st.session_state.attempts += 1

            if st.session_state.attempts >= 3:
                st.warning("⚠️ 3 failed attempts. Please login.")


def login():
    st.title("🔐 Login")
    user = st.text_input("Username:")
    pwd = st.text_input("Password:", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "admin":
            st.session_state.logged_in = True
            reset_attempts()
            st.success("✅ Logged in!")
        else:
            st.error("❌ Wrong credentials.")


st.sidebar.title("📂 Menu")
page = st.sidebar.radio("", ["Home", "Insert", "Retrieve", "Login"])

if page == "Home":
    home()
elif page == "Insert":
    insert()
elif page == "Retrieve":
    retrieve()
elif page == "Login":
    login()

st.markdown("Made with ❤️ by [Muhammad Samad]")
