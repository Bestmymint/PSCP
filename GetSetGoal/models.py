"""Create Models"""
from flask import Flask, session, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from . import db

class User():
    def __init__(self):
        pass
    
    def start_session(self, user):
        del user['password']
        session['username'] = user['username']
        return redirect(url_for('index'))

    def signup(self, username, password):
        """funtion for signup"""
        
        user = {
            "_id" : uuid.uuid4().hex,
            "username" : username,
            "password" : password
        }
        
        if db.users.find_one({'username' : username}):
            return render_template("signup.html" , err="HaveUser")
        
        user['password'] = generate_password_hash(user['password'])
        
        if db.users.insert_one(user):
            return self.start_session(user)
        return redirect('/user/signup')
    
    def login(self, username, password):
        user = db.users.find_one({'username' : username})
        if user and check_password_hash(user['password'], password):
            return self.start_session(user)
        
        return redirect('login')