from flask_restful import fields


user = {
    "user_id": fields.Integer,
    "username": fields.String,
    "password": fields.String,
    "email": fields.String,
    "StolenCoins": fields.Integer,
    "error": fields.String
}

stock = {
    "id": fields.Integer,
    "ticker": fields.String,
    "name": fields.String
}

watchlist = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "stock_id": fields.Integer,
    "stock_name": fields.String,
    "current_price": fields.String,
    "stock": fields.Nested(stock),
    "error": fields.String,
}

