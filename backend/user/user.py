import flask_login
from flask_login import LoginManager

from init_db import DataBase

login_manager = LoginManager()


class UserDB(DataBase, flask_login.UserMixin):

    def __init__(self):
        super().__init__()
        self.cur.execute('DROP TABLE IF EXISTS users;')
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS users (id serial \
        PRIMARY KEY, username varchar(150), email varchar(256), password_hash varchar(60), is_admin boolean);''')
        self.cur.execute('INSERT INTO users (username, email, is_admin)'
                         'VALUES (%s, %s, %s)',
                         ('admin',
                          'admin@maat_zine.com', True)
                         )
        self.conn.commit()

    @login_manager.user_loader
    def user_loader(self, user_id):
        self.cur.execute(f"SELECT * FROM users WHERE id = '{user_id}'")
        return bool(self.cur.fetchone())
