# Standard Library Imports
from flask import Flask
from dotenv import dotenv_values
import os

# Import blueprints
from .modules.root.RootController import root_blueprint

# Load environment variables
CONFIG = dotenv_values(os.path.join(os.path.dirname(__file__), '../', '.env'))

# Init App factory
def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(root_blueprint, url_prefix='/')
    
    return app
