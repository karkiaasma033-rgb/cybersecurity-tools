def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.isupper():
                if shifted < ord('A'):
                   shifted += 26
            else:
                if shifted < ord('a'):
                   shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

# Encrypted message to crack
encrypted = "Khoor Ddvkpd"

print("Trying all 25 possible shifts:")
print("-" * 40)

for shift in range(1, 26):
    attempt = decrypt(encrypted, shift)
    print("Shift " + str(shift) + ":" + attempt)
