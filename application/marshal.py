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
    "stock_ticker": fields.String,
    "current_price": fields.String,
    "stock": fields.Nested(stock),
    "error": fields.String,
}

stock_info = {
    'ticker': fields.String,
    'name': fields.String,
    'current_price': fields.Float,
    'sector': fields.String,
    'industry': fields.String,
    'market_cap': fields.String,
    'previous_close': fields.Float,
    'open': fields.Float,
    'volume': fields.Integer,
    'average_volume': fields.Integer,
    'pe_ratio': fields.Float,
    'dividend_yield': fields.Float,
    'error': fields.String
}

stock_price = {
    'datetime': fields.String,
    'price': fields.Float
}

stock_history = {
    'ticker': fields.String,
    'period': fields.String,
    'prices': fields.List(fields.Nested(stock_price)),
    'error': fields.String
}