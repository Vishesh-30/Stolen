from flask_restful import fields


user = {
    "user_id": fields.Integer,
    "username": fields.String,
    "password": fields.String,
    "email": fields.String,
    "StolenCoins": fields.Integer
}