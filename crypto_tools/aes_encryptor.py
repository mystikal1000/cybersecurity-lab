---

## 🔒 `crypto_tools/aes_encryptor.py`
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt_file(filename, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(filename, 'rb') as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)
    with open(filename + ".enc", 'wb') as f:
        for x in (cipher.nonce, tag, ciphertext):
            f.write(x)

def decrypt_file(enc_filename, key):
    with open(enc_filename, 'rb') as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    with open(enc_filename.replace('.enc', '.dec'), 'wb') as f:
        f.write(data)

# Example usage
# key = get_random_bytes(16)
# encrypt_file('secret.txt', key)
# decrypt_file('secret.txt.enc', key)
