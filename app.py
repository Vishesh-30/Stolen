from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_login import LoginManager, login_user, logout_user, login_required, current_user


from application.config import LocalDevelopmentConfig, db
from application.modals import User

app = None
api = None


base_url = 'http://127.0.0.1:5000'
def create_app():
    app = Flask(__name__, template_folder = 'templates', static_folder = 'static')
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    app.app_context().push()
    CORS(app)

    # with app.app_context():
    #     db.create_all()
    #     db.session.commit()

    app.app_context().push()
    return app, api


app, api = create_app()
jwt = JWTManager(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(username):
    user =  User.query.get(username)
    if user:
        return user
    return None




if __name__ == '__main__':
    app.run(debug=True)