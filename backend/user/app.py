import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_login import LoginManager

from user import UserDB

load_dotenv()
app = Flask(__name__)
login_manager = LoginManager()
app.secret_key = os.getenv('FLASK_SECRET_KEY')
login_manager.init_app(app)


@app.route('/')
def index():
    data = UserDB().user_loader("1")
    response = {
        "message": f"User {data}",

    }
    return jsonify(response), 200
