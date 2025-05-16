# 🔐 Password Security Toolkit

A full-stack educational cybersecurity project built with Flask that simulates real-world password **attacks** and **defenses**.

## 🧠 About

This web app demonstrates how common password security techniques can be implemented, attacked, and defended against using:

- Hybrid Dictionary Attacks  
- Rainbow Table Lookups  
- Password Hashing using SHA-256 and bcrypt  
- Password Strength Analysis

All functionality is handled via a simple and clean interface for educational and demonstration purposes.

---

## 🚀 Features

### 🛡️ Defense Mode
- 🔒 **Hashing** with SHA-256 or bcrypt
- 📊 **Strength checking** of entered passwords
- 📘 Clean interface with glowing cyber-themed design

### 💣 Attack Mode
- 🧠 **Hybrid Attack**: Combines wordlist with common suffixes (e.g. `123`, `!`, `2024`)
- 🌈 **Rainbow Table**: Matches precomputed hash-password pairs from a text file

---

## 📁 Project Structure

```
project/
│
├── app.py                    # Flask main app
├── utils/
│   ├── hybrid.py             # Hybrid attack logic
│   ├── rainbow.py            # Rainbow table logic
│   ├── bcrypt_utils.py       # Bcrypt hashing
│   └── strength_check.py     # Password strength checker
│
├── templates/
│   ├── index.html            # Home page
│   ├── defense.html          # Defense mode UI
│   └── attack.html           # Attack mode UI
│
├── static/
│   └── style.css             # Glowing hacker-style UI
│
└── uploads/                  # (Auto-created) Wordlist temp storage
```

---

## 🧪 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/password-security-toolkit.git
   cd password-security-toolkit
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install flask bcrypt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Open your browser and go to**
   ```
   http://localhost:5000
   ```

---

## 📸 Screenshots

> _You can add screenshots here for the UI. Eg:_
- Defense page showing hashed password & strength
- Attack page with cracking results

---

## 📂 Sample Files

To test rainbow or hybrid attacks:
- Use your own wordlists or
- Create a rainbow table in the format:
  ```
  hash:plaintext
  ```

Example:
```txt
5e884898da28047151d0e56f8dc6292773603d0d6aabbdd3fbb58b6a:password
```

---

## ⚠️ Disclaimer

This tool is created **for educational purposes only**. Do **not** use this for unauthorized cracking or unethical purposes. Always follow legal and ethical cybersecurity practices.

---

## 📌 Future Improvements (Optional Ideas)

- Add SHA-1 / MD5 support  
- Brute-force with multi-threading (if re-added)  
- User authentication system  
- Upload result reports

---

## 📃 License

MIT License
