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
from application.stockInfo import get_stock_info
from app import app, api, db, login_manager



class StockAPI(Resource):

    @marshal_with(stock_info)
    def get(self, ticker):
        stock_info = get_stock_info(ticker)
        return stock_info
    