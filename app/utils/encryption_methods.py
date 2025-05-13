import random

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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    # Calcula el inverso modular de e mod phi
    d = 0
    x1, x2, x3 = 1, 0, phi
    y1, y2, y3 = 0, 1, e
    while y3 != 0:
        q = x3 // y3
        t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    if x3 != 1:
        raise Exception("No existe inverso modular")
    return x2 % phi

def generate_rsa_keys():
    import random
    # Generar dos números primos
    p = random.choice([61, 53, 47, 43, 41])
    q = random.choice([59, 67, 71, 73, 79])
    n = p * q
    phi = (p - 1) * (q - 1)

    # Elegir un número e tal que 1 < e < phi y gcd(e, phi) = 1
    e = random.choice([3, 5, 17, 257, 65537])
    while gcd(e, phi) != 1:
        e = random.choice([3, 5, 17, 257, 65537])

    # Calcular d, el inverso modular de e mod phi
    d = mod_inverse(e, phi)

    return n, e, d

def rsa_encrypt(data, public_key):
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in data]
    return encrypted

def rsa_decrypt(encrypted_data, private_key):
    d, n = private_key
    decrypted = ''.join([chr(pow(char, d, n)) for char in encrypted_data])
    return decrypted

def encrypt_data(data, method, key=None):
    if method == "method1": 
        shift = int(key) if key else 3  
        encrypted = caesar_encrypt(data, shift)
        return encrypted, str(shift)
    elif method == "rsa":  # RSA encryption
        if not key or not isinstance(key, tuple) or len(key) != 2:
            raise ValueError("Se requieren dos claves: (n, e) para encriptar")
        public_key = key  # Solo usamos la clave pública para encriptar
        encrypted = rsa_encrypt(data, public_key)
        return encrypted, None
    else:
        raise ValueError("No se puede encriptar con el método especificado")

def decrypt_data(encrypted_data, method, key):
    if method == "method1":  # Caesar cipher
        shift = int(key)
        decrypted = caesar_decrypt(encrypted_data, shift)
        return decrypted
    elif method == "rsa":  # RSA decryption
        if not key:
            raise ValueError("Ingresa una clave privada")
        decrypted = rsa_decrypt(encrypted_data, key)
        return decrypted
    else:
        raise ValueError("No se puede desencriptar con el método especificado")