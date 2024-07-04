from flask_login import LoginManager, UserMixin

from init_db import DataBase

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return UserDB().find_user_by_id(int(user_id))[0]


class User(UserMixin):
    def __init__(self, user_id, username, email, password_hash, is_admin):
        self.id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.is_admin = is_admin


class UserDB(DataBase):

    def __init__(self):
        super().__init__()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS users (id serial \
        PRIMARY KEY, username varchar(150), email varchar(256), password_hash varchar, is_admin boolean);''')
        self.conn.commit()

    def add_user(self, email, password):
        self.cur.execute('INSERT INTO users (username, email, password_hash, is_admin)'
                         'VALUES (%s, %s, %s, %s)',
                         ('',
                          email, password, False))
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM users WHERE users.email = '{email}'")
        return self.cur.fetchone()

    def find_user(self, email):
        self.cur.execute(f"SELECT * FROM users WHERE users.email = '{email}'")
        data = self.cur.fetchone()
        user = User(data[0], data[1], data[2], data[3], data[4])
        return user

    def find_user_by_id(self, user_id):
        self.cur.execute(f"SELECT * FROM users WHERE users.id = {user_id}")
        data = self.cur.fetchone()
        user = User(data[0], data[1], data[2], data[3], data[4])
        return user
