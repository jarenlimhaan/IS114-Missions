# Standard Library Imports
from flask import Flask

# Import blueprints
from .modules.root.RootController import root_blueprint

# Init App factory
def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(root_blueprint, url_prefix='/')
    
    return app
