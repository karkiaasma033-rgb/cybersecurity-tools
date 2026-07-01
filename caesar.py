def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            else:
                if shifted > ord('z'):
                   shifted -= 26
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

message = "Hello Aashma"
shift = 3

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("Original: " + message)
print("Encrypted: " + encrypted)
print("Decrypted: " + decrypted)


