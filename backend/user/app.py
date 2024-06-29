import json
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request, flash
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from user import UserDB
from flask_bcrypt import check_password_hash, generate_password_hash


load_dotenv()
app = Flask(__name__)
login_manager = LoginManager()
app.secret_key = os.getenv('FLASK_SECRET_KEY')
login_manager.init_app(app)


@app.route("/register", methods=["POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already registered")
    else:
        try:
            password = json.loads(request.data)['password']
            email = json.loads(request.data)['email']
            password_hash = generate_password_hash(password, 10)
            user = UserDB().add_user(email, password_hash)
            if user:
                login_user(user)
                flash("You registered and are now logged in. Welcome!", "success")
            response = {"message": True}
            return jsonify(response), 200
        except Exception as e:
            return e.args


@app.route('/login', methods=['POST'])
def login():
    error = None
    if current_user.is_authenticated:
        flash("You are already logged in.")
    else:
        try:
            if request.method == 'POST':
                email = request.form['email']
                password = request.form['password']
                user = UserDB().find_user(email)
                if user and check_password_hash(user[3], password):
                    login_user(user)
                    if login_user(user):
                        response = {"message": user.email}
        except Exception as e:
            return e.args
        return jsonify(response), 200


@login_manager.user_loader
def load_user(user_id):
    return UserDB.find_user_by_id(int(user_id))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    response = {"message": True}
    return jsonify(response), 200


@app.route('/', methods=['GET'])
def index():
    response = {"message": True}
    return jsonify(response), 200
