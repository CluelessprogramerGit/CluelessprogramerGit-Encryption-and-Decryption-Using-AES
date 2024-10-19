# AES Encryption and Decryption

This project demonstrates how to encrypt and decrypt messages using the AES encryption algorithm in Python. It consists of two scripts: one for encryption and another for decryption.

## Prerequisites

Make sure you have the `pycryptodome` library installed. You can install it using pip:

```bash
pip install pycryptodome
```

## Files
- `encryption_script.py`: Encrypts a plain text message.
- `decryption_script.py`: Decrypts an encrypted message.

## How to Use

### Encryption

1. Run the encryption script:
    ```bash
    python encryption_script.py
    ```

2. Enter the plain text message when prompted.
3. The script will output the encrypted text and save it to `encrypted.txt`. The key is saved to `key.txt`.

### Decryption

1. Run the decryption script:
    ```bash
    python decryption_script.py
    ```

2. The script will read the encrypted text from `encrypted.txt` and the key from `key.txt`.
3. The script will output the decrypted text, which should match the original plain text message.

## Notes
- The encryption key must be 16, 24, or 32 bytes long.
- The encryption uses AES in ECB mode, which is suitable for learning purposes but not recommended for sensitive data in production due to potential security weaknesses.
- Ensure that the `encrypted.txt` and `key.txt` files are kept confidential and are not exposed publicly.

## License
This project is licensed under the MIT License.
