'''Flask Initialization'''
from flask import Flask, render_template, blueprints, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

client = pymongo.MongoClient(os.getenv("HOST"), int(os.getenv("PORT")))
db = client.mydb
users = db.users

def create_app():
    """Create an instance of Flask app"""
    app = Flask(__name__)
    app.secret_key = os.getenv("MY_SECRET_KEY")

    from .users import users
    app.register_blueprint(users , url_prefix='/user')
    from .models import User

    @app.route('/')
    def index():
        if 'username' in session:
            return render_template('index.html', username = session['username'])
        return redirect('user')

    return app