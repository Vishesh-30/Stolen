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



class WatchListAPI(Resource):



    @marshal_with(watchlist)
    def get(self, username):
        # Find the user by username
        user = User.query.filter_by(username=username).first()
        if user is not None:
            # Query the watchlist for the user
            watchlist_entries = Watchlist.query.filter_by(user_id=user.user_id).all()
            result = []

            # Iterate over each entry in the watchlist
            for entry in watchlist_entries:
                stock_entry = Stock.query.get(entry.stock_id)
                if stock_entry:
                    # Fetch the current price of the stock
                    try:
                        stock_info = get_stock_info(stock_entry.ticker)
                        # print(stock_info)

                        current_price = round(stock_info.get("current_price", 0), 2)
                        error_message = None
                    except Exception as e:
                        current_price = "N/A"
                        error_message = str(e)

                    # Add the entry to the result list
                    result.append({
                        "id": entry.id,
                        "user_id": entry.user_id,
                        "stock_id": entry.stock_id,
                        "stock_name": stock_entry.name,
                        "current_price": current_price,
                        "stock": {
                            "id": stock_entry.id,
                            "ticker": stock_entry.ticker,
                            "name": stock_entry.name
                        },
                        "error": error_message
                    })
                else:
                    result.append({
                        "id": entry.id,
                        "user_id": entry.user_id,
                        "stock_id": entry.stock_id,
                        "stock_name": "Unknown",
                        "current_price": "N/A",
                        "stock": None,
                        "error": "Stock not found"
                    })
            if len(result) > 0:
                return result, 200
            else:
                return {"error": "Watchlist is empty"}, 404
        return {"error": "User not found"}, 404
            
        
    



    def post(self,username, ticker):
        user = User.query.filter_by(username=username).first()
        if user is not None:
            stock = Stock.query.filter_by(ticker=ticker).first()
            if stock is not None:
                watchlist = Watchlist.query.filter_by(user_id=user.user_id, stock_id=stock.id).first()
                if watchlist is None:
                    watchlist = Watchlist(user_id=user.user_id, stock_id=stock.id, stock_name=stock.ticker)
                    db.session.add(watchlist)
                    db.session.commit()
                    return {"message": "Stock added to watchlist"}, 201
                else:
                    return {"error": "Stock already in watchlist"}, 400
            else:
                return {"error": "Stock not found"}, 400
        else:
            return {"error": "User not found"}, 400
        
        






api.add_resource(WatchListAPI, '/api/watchlist/<string:username>', '/api/watchlist/<string:username>/<string:ticker>')

