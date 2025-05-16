from flask import Flask, render_template, request
from utils.hybrid import hybrid_crack
from utils.rainbow import rainbow_crack
from utils.bcrypt_utils import hash_bcrypt
from utils.strength_check import check_strength

import hashlib
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/attack", methods=["GET", "POST"])
def attack():
    result = None

    if request.method == "POST":
        target_hash = request.form["target_hash"]
        method = request.form["method"]
        max_length = request.form.get("max_length")  # For brute

        # Only load wordlist file if not using brute
        wordlist_file = request.files.get("wordlist")

        filepath = None
        if wordlist_file and method != "brute":
            filepath = os.path.join("uploads", wordlist_file.filename)
            os.makedirs("uploads", exist_ok=True)
            wordlist_file.save(filepath)

        try:
            if method == "hybrid" and filepath:
                result = hybrid_crack(target_hash, filepath)
            elif method == "rainbow" and filepath:
                result = rainbow_crack(target_hash, filepath)
            elif method == "brute":
                result = brute_force_crack(target_hash, max_length=int(max_length or 4))
            else:
                result = "❌ Invalid method or missing wordlist"
        except Exception as e:
            result = f"Error during attack: {str(e)}"
        finally:
            if filepath and os.path.exists(filepath):
                os.remove(filepath)

    return render_template("attack.html", result=result)

@app.route("/defense", methods=["GET", "POST"])
def defense():
    strength = hashed = None

    if request.method == "POST":
        password = request.form["password"]
        method = request.form["method"]
        strength = check_strength(password)

        if method == "sha256":
            hashed = hashlib.sha256(password.encode()).hexdigest()
        elif method == "bcrypt":
            hashed = hash_bcrypt(password)

    return render_template("defense.html", strength=strength, hashed=hashed)

if __name__ == "__main__":
    app.run(debug=True)
