from flask import Flask, Blueprint, render_template, session, request, redirect
from .models import User

users = Blueprint('users', __name__)

@users.route('/', methods=['GET'])
def user_index():
    if request.method == "GET":
        return render_template('home.html')

@users.route('/login', methods=['GET', 'POST'])
def login():
    """Path for user Login"""
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        return User().login(username, password)
    
@users.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        return User().signup(username, password)

@users.route('/logout')
def logout():
    session.clear()
    return redirect('/')