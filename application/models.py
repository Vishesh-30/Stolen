from application.config import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    zipcode = db.Column(db.String(10), nullable=True)
    StolenCoins = db.Column(db.Integer, nullable=False)

    def __init__(self, username, email, password, StolenCoins):
        self.username = username
        self.email = email
        self.password = password
        self.StolenCoins = StolenCoins

    def __repr__(self):
        return f'User {self.username}'


class Stock(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticker = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)



class Watchlist(db.Model):
    __tablename__ = 'watchlists'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stocks.id'), nullable=False)
    stock_name = db.Column(db.String(255), nullable=False)
    stock = db.relationship('Stock', backref=db.backref('watchlists', lazy=True))