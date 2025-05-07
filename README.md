
# 🔐 Secure Data Storage & Retrieval App

A lightweight and secure web app built with **Streamlit** that allows users to store and retrieve encrypted data using a passkey. Ideal for small-scale secret storage, password reminders, or confidential notes.

## 🚀 Features

- 💾 **Store Data Securely** – Text is encrypted using Fernet symmetric encryption.
- 🔓 **Retrieve Data with Passkey** – Only correct passkey can decrypt stored information.
- ❌ **Brute-force Prevention** – Three failed attempts block retrieval.
- 🔐 **Admin Login** – Regain access after failed attempts (default credentials).
- 🧠 **Session-Based** – All data is tracked using Streamlit’s session state.


---

## 🛠️ How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/secure-storage-app.git
   cd secure-storage-app

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

---

## 🔑 Default Admin Login

* **Username:** `admin`
* **Password:** `admin`

You can change these in the `login()` function in the code.

---

## 📂 Project Structure

```
secure-storage-app/
│
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📦 Requirements

* streamlit
* cryptography

You can install them with:

```bash
pip install streamlit cryptography
```

---

## 🙌 Author

**Muhammad Samad**
[Portfolio](https://portfolio-tailwind-css-by-samad.vercel.app/) •

