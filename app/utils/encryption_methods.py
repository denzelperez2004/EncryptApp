from cryptography.fernet import Fernet
import hashlib
import base64

def generate_key():
    return Fernet.generate_key()

def fernet_encrypt(data, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return encrypted

def fernet_decrypt(encrypted_data, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data).decode()
    return decrypted

def caesar_encrypt(data, shift):
    encrypted = ""
    for char in data:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(data, shift):
    decrypted = ""
    for char in data:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted += char
    return decrypted

def encrypt_data(data, method, key=None):
    if method == "fernet":
        if not key:
            key = generate_key()
        encrypted = fernet_encrypt(data, key)
        return encrypted, key
    elif method == "method1":  # Caesar cipher
        shift = int(key) if key else 3  # Default shift is 3
        encrypted = caesar_encrypt(data, shift)
        return encrypted, str(shift)
    else:
        raise ValueError("Unsupported encryption method")

def decrypt_data(encrypted_data, method, key):
    if method == "fernet":
        decrypted = fernet_decrypt(encrypted_data, key)
        return decrypted
    elif method == "method1":  # Caesar cipher
        shift = int(key)
        decrypted = caesar_decrypt(encrypted_data, shift)
        return decrypted
    else:
        raise ValueError("Unsupported decryption method")