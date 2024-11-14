import json
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt

from backend.about.about import AboutDB
from backend.issue.issue import IssueDB
from backend.join.join import JoinDB
from backend.join.static import Letters
from backend.texts.texts import TextDB
from backend.user.static import ResponseSuccess, ResponseFailure
from backend.user.user import UserDB, UserInfoDB
from backend.photos.photo import PhotoDB

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
bcrypt = Bcrypt(app)
CORS(app)
mail = Mail(app)


@login_manager.user_loader
def load_user(user_id: int):
    return UserDB().find_user_by_id(int(user_id))


@app.route("/register", methods=["POST"])
@cross_origin()
def register():
    try:
        password = json.loads(request.data)['password']
        email = json.loads(request.data)['email']
        hashed = bcrypt.generate_password_hash(password).decode('utf8')
        user = UserDB().add_user(email, hashed)
        if user:
            info = UserInfoDB().add_user_info(user_id=user.id, orders=[], favorites=[], reads=[])
            if info:
                response = ResponseSuccess.response_registered
                return jsonify(response), 201
        else:
            response = ResponseFailure.response_not_registered
            return jsonify(response), 400
    except Exception as e:
        response = {"message": e.args}
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
            if user and bcrypt.check_password_hash(user.password_hash, password):
                login_user(user, remember=True)
                response = {"user": "Successfully logged"}
                return jsonify(response), 200
            else:
                response = ResponseFailure.response_not_logged_in
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
    try:
        name = json.loads(request.data)['name']
        social = json.loads(request.data)['social']
        photo_link = json.loads(request.data)['photo_link']

        about = AboutDB().add_about_user(name, social, photo_link)
        if about:
            response = {"message": "successfully created",
                        "data": {"user_name": about.name, "social": about.social, "photo": about.photo_link}}
            return jsonify(response), 201
        else:
            response = ResponseFailure.info_not_created
            return jsonify(response), 400
    except Exception as e:
        response = {"message": e.args}
        return jsonify(response), 400


@app.route('/join', methods=['POST'])
@cross_origin()
def join_request():
    try:
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
    except Exception as e:
        response = {"message": e.args}
        return jsonify(response), 400


@app.route('/about', methods=['GET'])
@cross_origin()
def about_page():
    try:
        items = []
        data = AboutDB().select_all_abouts()
        for el in data:
            item = {"id": el.id, "name": el.name, "photo_link": el.photo_link, "social": el.social}
            items.append(item)

        response = {"message": items}
        return jsonify(response), 200
    except Exception as e:
        response = {"message": e.args}
        return jsonify(response), 400


@app.route('/user/<user_id>', methods=['GET'])
@login_required
def user_info(user_id: int):
    try:
        user = UserInfoDB().user_info(user_id=user_id)
        if user:
            response = {"message": "User found", "user_info": {
                "user_id": user.user_id,
                "user_reads": user.reads,
                "user_orders": user.orders,
                "user_favorites": user.favorites
            }}
            return jsonify(response), 200
        else:
            response = {"message": f"User with id {user_id} not found"}
            return jsonify(response), 400
    except Exception as e:
            response = {"message": e.args}
            return jsonify(response), 400


@app.route("/mail")
def send_mail(subject, sender, recipients, message):
    try:
        msg = Message(subject=subject, sender=sender, recipients=recipients)
        msg.body = message
        mail.send(msg)
        return 'Sent'
    except Exception as e:
        response = {"message": e.args}
        return jsonify(response), 400


@app.route('/photo/create', methods=['POST'])
@cross_origin()
def create_photo():
    try:
        link = json.loads(request.data)['link']
        photo = PhotoDB().add_new_photo(link)
        if photo:
            response = {"message": "Photo successfully added"}
            return jsonify(response), 201
    except KeyError as err:
        response = {"message": f"Photo not added, {err.args[0]} is missing"}
        return jsonify(response), 400


@app.route('/restore', methods=['POST'])
@cross_origin()
def restore_password():
    try:
        email = json.loads(request.data)['email']
        user = UserDB().find_user(email=email)
        if user:
            send_mail()
            response = {"message": "You'll receive a link via email"}
            return jsonify(response), 200
    except KeyError as err:
        response = {"message": f"Link not sent, {err.args[0]} is missing"}
        return jsonify(response), 400


@app.route('/issues', methods=['GET'])
@cross_origin()
def select_all_issues():
    try:
        count = IssueDB().select_issue_count()
        issues = IssueDB().select_all_issues()
        issues_data = [{"id": i.id, "name": i.name, "articles": i.articles, "pictures": i.pictures, "editorial": i.editorial} for i in issues]
        response = {"message": "Ok", "count": count[0], "issues": issues_data}
        return jsonify(response), 200
    except Exception as e:
        response = {"message": e.args}
        return jsonify(response), 400


@app.route('/fav', methods=['POST'])
@cross_origin()
@login_required
def add_to_favs():
    try:
        pic_id = json.loads(request.data)['pic_id']
        UserInfoDB().update_favs(current_user.id, pic_id)
        response = {}
        return jsonify(response), 204
    except Exception as e:
        response = {"message": e.args}
        return jsonify(response), 400


@app.route('/reads', methods=['POST'])
@cross_origin()
@login_required
def add_to_reads():
    try:
        article_id = json.loads(request.data)['article_id']
        UserInfoDB().update_reads(current_user.id, article_id)
        response = {}
        return jsonify(response), 204
    except Exception as e:
        response = {"message": e.args}
        return jsonify(response), 400


@app.route('/text/create', methods=['POST'])
@cross_origin()
@login_required
def text_create():
    try:
        content = json.loads(request.data)['content']
        TextDB().add_new_text(content)
        response = {}
        return jsonify(response), 204
    except Exception as e:
        response = {"message": e.args}
        return jsonify(response), 400


@app.route('/issue/create', methods=['POST'])
@cross_origin()
def issue_create():
    try:
        name = json.loads(request.data)['name']
        articles = json.loads(request.data)['articles']
        pictures = json.loads(request.data)['pictures']
        editorial = json.loads(request.data)['editorial']
        IssueDB().add_new_issue(name, articles, pictures, editorial)
        response = {}
        return jsonify(response), 204
    except Exception as e:
        response = {"message": e.args}
        return jsonify(response), 400