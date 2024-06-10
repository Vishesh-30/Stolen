from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from application.config import LocalDevelopmentConfig, db
from application.models import User


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object(LocalDevelopmentConfig)
db.init_app(app)
api = Api(app)
CORS(app)

jwt = JWTManager(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Uncomment this if you want to create tables at startup
# with app.app_context():
#     db.create_all()


from application.api.register import *
from application.api.topStocks import *
from application.api.stock import *
from application.api.watchlist import *



if __name__ == '__main__':
    app.run(debug=True)
