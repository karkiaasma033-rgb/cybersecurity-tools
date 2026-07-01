from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'MySecretKey12345'
cipher = AES.new(key, AES.MODE_CBC)

message = b"Hello Aashma! This is encrypted!"
encrypted = cipher.encrypt(pad(message, 16))

print("Original: " + message.decode())
print("Encrypted: " + encrypted.hex())

cipher2 = AES.new(key, AES.MODE_CBC, cipher.iv)
decrypted = unpad(cipher2.decrypt(encrypted), 16)
print("Decrypted: " + decrypted.decode())

