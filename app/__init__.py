from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config')
    app.config['DEBUG'] = True  # Enable debug mode
    app.secret_key = 'your_secret_key'  # Replace with a secure random key

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app