class Config:
    SECRET_KEY = 'your_secret_key_here'
    DEBUG = True
    TESTING = False
    ENCRYPTION_METHODS = ['AES', 'DES', 'RSA']  # List of available encryption methods
    # Add any other configuration settings as needed