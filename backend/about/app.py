import json
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from static import ResponseSuccess, ResponseFailure
from about.about import AboutDB

load_dotenv()
app = Flask(__name__)
login_manager = LoginManager()
app.secret_key = os.getenv('FLASK_SECRET_KEY')
login_manager.init_app(app)
CORS(app)


@login_manager.user_loader
def load_user(user_id):
    return UserDB().find_user_by_id(int(user_id))


@app.route("/register", methods=["POST"])
@cross_origin()
def register():
    try:
        if current_user.is_authenticated:
            response = ResponseSuccess.response_already_logged_in
            return jsonify(response), 400
        else:
            password = json.loads(request.data)['password']
            email = json.loads(request.data)['email']
            password_hash = generate_password_hash(password, 10).decode('utf8')
            user = UserDB().add_user(email, password_hash)
            if user:
                response = ResponseSuccess.response_registered
                return jsonify(response), 201
            else:
                response = ResponseFailure.response_not_registered
                return jsonify(response), 400
    except Exception:
        response = {"message": "Try to use another email or password"}
        return jsonify(response), 400


@app.route('/login', methods=['POST'])
def login():
    try:
        if current_user.is_authenticated:
            response = ResponseSuccess.response_already_logged_in
            return jsonify(response), 200
        else:
            password = json.loads(request.data)['password']
            email = json.loads(request.data)['email']
            user = UserDB().find_user(email)
            if user and check_password_hash(user.password_hash, password):
                if login_user(user):
                    response = ResponseSuccess.response_logged_in
                    return jsonify(response), 200
                else:
                    response = ResponseFailure.response_not_logged_in
                    return jsonify(response), 400
            else:
                response = ResponseFailure.response_incorrect_data
                return jsonify(response), 400

    except Exception as e:
        response = {"message": e.args}
        return jsonify(response), 400


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    try:
        if current_user.is_authenticated:
            logout_user()
            return {}, 204
    except Exception as e:
        response = {"message": e.args}
        return jsonify(response), 400


@app.route('/', methods=['GET'])
def index():
    response = {"message": True}
    return jsonify(response), 200
