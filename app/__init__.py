from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite for simplicity
    app.config['UPLOAD_FOLDER'] = 'uploads'  # Define the upload folder
    # Additional configurations for testing
    app.config['TESTING'] = True
    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
