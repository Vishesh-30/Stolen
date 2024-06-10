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


class StockInfoAPI(Resource):
    @marshal_with(stock_info)
    def get(self, ticker):
        try:
            stock_info_data = get_stock_info(ticker)
            return stock_info_data
        except Exception as e:
            return {'error': str(e)}, 400

class StockHistoryAPI(Resource):
    @marshal_with(stock_history)
    def get(self, ticker, period):
        try:
            stock_history_data = get_stock_history(ticker, period)
            # print(stock_history_data)
            return stock_history_data
        except Exception as e:
            return {'error': str(e)}, 400

# Add resources to the API
api.add_resource(StockInfoAPI, '/api/stockinfo/<string:ticker>')
api.add_resource(StockHistoryAPI, '/api/stockhistory/<string:ticker>/<string:period>')


