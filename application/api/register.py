from flask import request, session, redirect, url_for, render_template, flash, jsonify
from flask_restful import Resource, Api, reqparse
from flask_restful import marshal_with
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import hashlib

from application.models import *
from application.marshal import *
from application.controllers.validate import *
from app import app, api, db, login_manager



class RegisterApI (Resource):
    # def get(self):
    #     return {'message': 'User created successfully'}
    
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        StolenCoins = 100000
        pass_hash = hashlib.sha256(password.encode()).hexdigest()

        if not username:
            raise MissingParameterError(400, "User name is required")
        if not password:
            raise MissingParameterError(400, "User password is required")
        if not email:
            raise MissingParameterError(400, "User email is required")
        else:
            user = User.query.filter_by(username=username, password=pass_hash).first()
            if user is None:
                user = User(username=username, email=email, password=pass_hash, StolenCoins=StolenCoins)
                db.session.add(user)
                db.session.commit()
                token = create_access_token(identity=user.username)
                return {'access_token': token}, 201
            else:
                return {'message': 'User already exists'}, 400
            

api.add_resource(RegisterApI, '/api/register')
