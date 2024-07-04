import json
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request, flash
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import LoginManager, current_user, login_user, login_required, logout_user

from user import UserDB

load_dotenv()
app = Flask(__name__)
login_manager = LoginManager()
app.secret_key = os.getenv('FLASK_SECRET_KEY')
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return UserDB().find_user_by_id(int(user_id))


@app.route("/register", methods=["POST"])
def register():
    try:
        if current_user.is_authenticated:
            flash("You are already registered")
        else:
            password = json.loads(request.data)['password']
            email = json.loads(request.data)['email']
            password_hash = generate_password_hash(password, 10).decode('utf8')
            user = UserDB().add_user(email, password_hash)
            if user:
                response = {"message": "You have successfully registered"}
                return jsonify(response), 200
            else:
                response = {"message": "You are not registered. Please try again later"}
                return jsonify(response), 400
    except Exception as e:
        return e.args


@app.route('/login', methods=['POST'])
def login():
    try:
        if current_user.is_authenticated:
            response = {"message": current_user.email}
            return jsonify(response), 200
        else:
            if request.method == 'POST':
                email = request.form['email']
                password = request.form['password']
                user = UserDB().find_user(email)
                if user and check_password_hash(user.password_hash, password):
                    if login_user(user):
                        response = {"message": "You are successfully logged in"}
                        return jsonify(response), 200
                    else:
                        response = {"message": "Try again later"}
                        return jsonify(response), 400
                else:
                    response = {"message": "Either your email or your password are incorrect. Please try again"}
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
            response = {"message": "You are logged out"}
            return jsonify(response), 200
    except Exception as e:
        response = {"message": e.args}
        return jsonify(response), 400


@app.route('/', methods=['GET'])
def index():
    response = {"message": True}
    return jsonify(response), 200
