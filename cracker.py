import hashlib

target_hash = hashlib.md5(b"password123").hexdigest()
print("Target hash: " + target_hash)

wordlist = ["123456", "password", "sunshine",
            "hello", "password123", "qwerty",
            "admin", "letmein"]

print("Cracking...")

for word in wordlist:
    attempt = hashlib.md5(word.encode()).hexdigest()
    if attempt == target_hash:
        print("PASSWORD FOUND: " + word)
        break
    else:
        print("Tried: " + word + " - wrong!")
