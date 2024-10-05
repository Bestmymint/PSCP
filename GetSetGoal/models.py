"""Create Models"""
from flask import Flask, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from . import db

class User():
    def __init__(self):
        pass
    
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['username'] = user['username']
        return redirect(url_for('index'))

    def signup(self, username, password):
        """funtion for signup"""
        
        user = {
            "_id" : uuid.uuid4().hex,
            "username" : username,
            "password" : password
        }
        
        if db.user.find_one({'username' : username}):
            return "Name already in use"
        
        user['password'] = generate_password_hash(user['password'])
        
        if db.users.insert_one(user):
            return self.start_session(user)
        return redirect('/user/signup')
    
    def login(self, username, password):
        user = db.users.find_one({'username' : username})
        if user and check_password_hash(user['password'], password):
            return self.start_session(user)
        
        return redirect('login')