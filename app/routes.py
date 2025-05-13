from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, flash
from app.utils.encryption_methods import rsa_encrypt, rsa_decrypt, generate_rsa_keys, encrypt_data, decrypt_data

# Define el Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('base.html')

@main.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        data = request.form.get('data')
        method = request.form.get('method')

        if method == "rsa":
            public_key = request.form.get('public_key')
            private_key = request.form.get('private_key')
            key = (public_key, private_key)  # Combina las llaves en una tupla
        else:
            key = request.form.get('key')

        try:
            # Llama a la función de cifrado
            encrypted_data, encryption_key = encrypt_data(data, method, key)

            return render_template(
                'encrypt.html',
                encrypted_data=encrypted_data,
                key=encryption_key
            )
        except ValueError as e:
            return render_template('encrypt.html', error=str(e))
    return render_template('encrypt.html')

@main.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'GET':
        # Renderiza el formulario de descifrado con la clave por defecto
        default_key = session.get('last_key', '')  # Retrieve the key from the session
        return render_template('decrypt.html', default_key=default_key)

    # Maneja la solicitud POST para descifrar datos
    encrypted_data = request.form.get('encrypted_data')
    method = request.form.get('decryption_method')
    key = request.form.get('key')
    try:
        if method == "method1":  # Caesar Cipher
            decrypted = decrypt_data(encrypted_data, method, key)
        else:
            decrypted = decrypt_data(encrypted_data.encode(), method, key.encode())
        return render_template('decrypt.html', decrypted_data=decrypted)
    except ValueError as e:
        return render_template('decrypt.html', error=str(e))

@main.route('/generate_keys', methods=['POST'])
def generate_keys():
    public_key, private_key = generate_rsa_keys()
    # Guarda las claves en la sesión
    session['public_key'] = public_key
    session['private_key'] = private_key
    rsa_keys = {
        'public_key': public_key,
        'private_key': private_key
    }
    return render_template('base.html', rsa_keys=rsa_keys)

@main.route('/generate_rsa_keys', methods=['POST'])
def generate_rsa_keys_route():
    from app.utils.encryption_methods import generate_rsa_keys
    n, e, d = generate_rsa_keys()
    return render_template('rsa.html', n=n, e=e, d=d)

@main.route('/caesar', methods=['GET', 'POST'])
def caesar():
    encrypted_data = None
    decrypted_data = None

    if request.method == 'POST':
        data = request.form.get('data')
        method = request.form.get('method')
        key = request.form.get('key')

        if method == "method1":
            if 'encrypt' in request.form:
                encrypted_data, _ = encrypt_data(data, method, key)
            elif 'decrypt' in request.form:
                decrypted_data = decrypt_data(data, method, key)

    return render_template('caesar.html', encrypted_data=encrypted_data, decrypted_data=decrypted_data)


@main.route('/rsa', methods=['GET', 'POST'])
def rsa():
    encrypted_data = None
    decrypted_data = None
    n = None
    e = None
    d = None

    if request.method == 'POST':
        data = request.form.get('data')
        method = request.form.get('method')
        n = request.form.get('n')
        e = request.form.get('e')
        d = request.form.get('d')

        try:
            # Convertir las llaves a enteros si están presentes
            if n and e and d:
                n = int(n)
                e = int(e)
                d = int(d)

                if 'encrypt' in request.form:
                    public_key = (e, n)
                    encrypted_data = rsa_encrypt(data, public_key)
                elif 'decrypt' in request.form:
                    private_key = (d, n)
                    encrypted_data = eval(data)  # Convertir la cadena a lista de enteros
                    decrypted_data = rsa_decrypt(encrypted_data, private_key)
        except ValueError:
            return render_template('rsa.html', error="Invalid key format. Please enter valid integers.")

    return render_template(
        'rsa.html',
        n=n,
        e=e,
        d=d,
        encrypted_data=encrypted_data,
        decrypted_data=decrypted_data
    )

@main.route('/show_code', methods=['GET'])
def show_code():
    try:
        # Ruta del archivo encryption_methods.py
        file_path = 'app/utils/encryption_methods.py'
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()
    except FileNotFoundError:
        code = "El archivo encryption_methods.py no se encontró."
    return render_template('show_code.html', code=code)