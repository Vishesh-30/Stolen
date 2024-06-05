from application.config import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    StolenCoins = db.Column(db.Integer, nullable=False)

    def __init__(self, username, email, password, StolenCoins):
        self.username = username
        self.email = email
        self.password = password
        self.StolenCoins = StolenCoins

    def __repr__(self):
        return f'User {self.username}'
