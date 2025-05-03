from flask import Blueprint, render_template, request, jsonify, session
from app.utils.encryption_methods import encrypt_data, decrypt_data

# Define el Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('base.html')

@main.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'GET':
        # Renderiza el formulario de cifrado
        return render_template('encrypt.html')

    # Maneja la solicitud POST para cifrar datos
    data = request.form.get('data')
    method = request.form.get('method')
    key = request.form.get('key', None)
    try:
        encrypted, key = encrypt_data(data, method, key)
        session['last_key'] = key  # Save the key in the session
        return render_template('encrypt.html', encrypted_data=encrypted, key=key)
    except ValueError as e:
        return render_template('encrypt.html', error=str(e))

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