import json
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_mail import Mail, Message

from about.about import AboutDB
from join.join import JoinDB
from join.static import Letters
from user.static import ResponseSuccess, ResponseFailure
from user.user import UserDB, UserInfoDB

load_dotenv()
app = Flask(__name__)
login_manager = LoginManager()
app.secret_key = os.getenv('FLASK_SECRET_KEY')
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
login_manager.init_app(app)
CORS(app)
mail = Mail(app)


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
                info = UserInfoDB().add_user_info(user_id=user.id, orders=[], favorites=[], reads=[])
                if info:
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


@app.route('/about/create', methods=['POST'])
@cross_origin()
def create_about():
    name = json.loads(request.data)['name']
    social_1 = json.loads(request.data)['social_1']
    social_2 = json.loads(request.data)['social_2']
    social_3 = json.loads(request.data)['social_3']
    photo_link = json.loads(request.data)['photo_link']

    about = AboutDB().add_about_user(name, social_1, social_2, social_3, photo_link)
    if about:
        response = {"message": "successfully created",
                    "data": {"user_name": about.name, "social_1": about.social_1, "social_2": about.social_2,
                             "social_3": about.social_3, "photo": about.photo_link}}
        return jsonify(response), 201
    else:
        response = ResponseFailure.info_not_created
        return jsonify(response), 400


@app.route('/join', methods=['POST'])
@cross_origin()
def join_request():
    name = json.loads(request.data)['name']
    email = json.loads(request.data)['email']
    link = json.loads(request.data)['link']

    join = JoinDB().add_join_request(name, email, link)
    if join:
        response = {"message": "We have received your data. You will receive a letter from our team",
                    "data": {"name": join.name, "email": join.email, "photo": join.link}}
        send_mail(Letters.subject_join, "zine.maat@gmail.com", [join.email], Letters.message_body_join)
        return jsonify(response), 201
    else:
        response = ResponseFailure.info_not_created
        return jsonify(response), 400


@app.route('/about', methods=['GET'])
def about_page():
    items = []
    data = AboutDB().select_all_abouts()
    for el in data:
        item = {"id": el.id, "name": el.name, "photo_link": el.photo_link, "socials": []}
        for i in [el.social_1, el.social_2, el.social_3]:
            if i != "":
                item["socials"].append(i)
        items.append(item)

    response = {"message": items}
    return jsonify(response), 200


@app.route("/mail")
def send_mail(subject, sender, recipients, message):
    msg = Message(subject=subject, sender=sender, recipients=recipients)
    msg.body = message
    mail.send(msg)
    return 'Sent'
