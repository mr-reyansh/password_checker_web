import hashlib

def hybrid_crack(target_hash, wordlist_path):
    suffixes = ["123", "!", "2024", "@", "1"]
    with open(wordlist_path, "r") as f:
        base_words = [line.strip() for line in f]

    for word in base_words:
        for suf in suffixes:
            variations = [word + suf, word.capitalize() + suf, word.upper() + suf]
            for guess in variations:
                hashed = hashlib.sha256(guess.encode()).hexdigest()
                if hashed == target_hash:
                    return f"💥 Cracked! Password = {guess}"

    return "❌ Not cracked using hybrid method."
