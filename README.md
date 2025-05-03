# Flask Encrypter-Decrypter

This project is a web application built using Flask that provides encryption and decryption functionalities. Users can input data to be encrypted or decrypted using various encryption methods.

## Features

- User-friendly interface for encryption and decryption.
- Supports multiple encryption algorithms.
- Input validation for secure data handling.

## Project Structure

```
flask-encrypter-decrypter
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
│   ├── templates
│   │   ├── base.html
│   │   ├── encrypt.html
│   │   └── decrypt.html
│   └── utils
│       └── encryption_methods.py
├── tests
│   ├── __init__.py
│   └── test_app.py
├── requirements.txt
├── config.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-encrypter-decrypter
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   flask run
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Use the navigation to access the encryption and decryption pages.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.