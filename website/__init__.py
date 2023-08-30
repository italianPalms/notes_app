"""
This module contains a flask application for a simple web service
"""

from flask import Flask

def create_app():
    """
    Create and configure the Flask app.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wkslhjykksks'
    return app 