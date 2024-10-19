from Crypto.Cipher import AES
import base64


def unpad(text):
    padding = ord(text[-1])
    return text[:-padding]


def decrypt(encrypted_text, key):
    encrypted_text = base64.b64decode(encrypted_text)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(encrypted_text).decode('utf-8')
    return unpad(decrypted_text)


# Read the encrypted text and key from files
with open('encrypted.txt', 'r') as file:
    encrypted_text = file.read()

with open('key.txt', 'r') as file:
    key = file.read()

# Decrypt the message
decrypted_text = decrypt(encrypted_text, key)

print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")
