from Crypto.Cipher import AES
import base64


def pad(text):
    block_size = 16
    padding = block_size - len(text) % block_size
    return text + padding * chr(padding)


def encrypt(plain_text, key):
    plain_text = pad(plain_text)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    encrypted_text = cipher.encrypt(plain_text.encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')


# Example usage:
key = 'This is a key123'  # Key must be 16, 24, or 32 bytes long
plain_text = input("Enter the plain text: ")
encrypted_text = encrypt(plain_text, key)

print(f"Plain text: {plain_text}")
print(f"Encrypted text: {encrypted_text}")

# Save the encrypted text and key to a file for later use
with open('encrypted.txt', 'w') as file:
    file.write(encrypted_text)
with open('key.txt', 'w') as file:
    file.write(key)
