from flask import request, session, redirect, url_for, render_template, flash, jsonify
from flask_restful import Resource, Api, reqparse
from flask_restful import marshal_with
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import hashlib
import yfinance as yf
import pandas as pd
import json



from application.models import *
from application.marshal import *
from application.controllers.validate import *
from application.stockInfo import *
from app import app, api, db, login_manager



class ProfileAPI(Resource):
    @marshal_with(user)
    def get(self):
        try:
            user = User.query.filter_by(id=session.get('user_id')).first()
            return user
        except Exception as e:
            return {'error': str(e)}, 400

    def post(self):
        try:
            user = User.query.filter_by(id=session.get('user_id')).first()
            data = request.get_json()
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            user.phone = data.get('phone', user.phone)
            user.address = data.get('address', user.address)
            user.city = data.get('city', user.city)
            user.state = data.get('state', user.state)
            user.zipcode = data.get('zipcode', user.zipcode)
            db.session.commit()
            return {'message': 'Profile updated successfully'}
        except Exception as e:
            return {'error': str(e)}, 400
        
    def put(self):
        try:
            user = User.query.filter_by(id=session.get('user_id')).first()
            data = request.get_json()
            if not check_password_hash(user.password, data.get('old_password')):
                return {'error': 'Incorrect old password'}, 400
            
            user.password = generate_password_hash(data.get('password'))
            db.session.commit()
            return {'message': 'Password updated successfully'}
        except Exception as e:
            return {'error': str(e)}, 400
        
        
        


# Add resources to the API
api.add_resource(ProfileAPI, '/api/profile')
