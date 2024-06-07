from flask import request, session, redirect, url_for, render_template, flash, jsonify
from flask_restful import Resource, Api, reqparse
from flask_restful import marshal_with
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import hashlib
import yfinance as yf
import pandas as pd

from application.models import *
from application.marshal import *
from application.controllers.validate import *
from app import app, api, db, login_manager




class TopStocksAPI(Resource):
    def get(self):
        tickers = yf.Tickers('RELIANCE.NS TCS.NS HDFCBANK.NS BHARTIARTL.NS')
        data = tickers.history(period='1d')
        
        # Transform the data to a more readable structure
        transformed_data = {}
        for index, row in data.iterrows():
            date = index.strftime('%Y-%m-%d')
            transformed_data[date] = {}
            for (item, ticker), value in row.items():
                if ticker not in transformed_data[date]:
                    transformed_data[date][ticker] = {}
                transformed_data[date][ticker][item] = value
        
        return jsonify(transformed_data)

api.add_resource(TopStocksAPI, '/api/top-stocks')