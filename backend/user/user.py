from flask_login import LoginManager, UserMixin

from backend.init_db import DataBase
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


class UserInfo(UserMixin):
    def __init__(self, user_id, orders, reads, favorites):
        self.user_id = user_id
        self.orders = orders
        self.reads = reads
        self.favorites = favorites


class UserDB(DataBase):

    def __init__(self):
        super().__init__()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS users
(
    id
    serial \
    PRIMARY
    KEY,
    username
    varchar
(
    150
), email varchar
(
    256
), UNIQUE(email), 
    password_hash varchar, is_admin boolean);
''')
        self.conn.commit()

    def add_user(self, email, password):
        self.cur.execute('INSERT INTO users (username, email, password_hash, is_admin)'
                         'VALUES (%s, %s, %s, %s)',
                         ('',
                          email, password, False))
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM users WHERE users.email = '{email}'")
        data = self.cur.fetchone()
        print(data)
        user = User(data[0], data[1], data[2], data[3], data[4])
        return user

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


class UserInfoDB(DataBase):

    def __init__(self):
        super().__init__()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS infos
(
    id
    serial \
    PRIMARY
    KEY,
    user_id
    integer
, orders integer array
, reads integer array, favorites integer array, CONSTRAINT user_id
      FOREIGN KEY(user_id) 
        REFERENCES users(id))''')
        self.conn.commit()

    def add_user_info(self, user_id, orders, favorites, reads):
        self.cur.execute('INSERT INTO infos (user_id, orders, favorites, reads)'
                         'VALUES (%s, %s, %s, %s)',
                         (user_id, orders, favorites, reads))
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM infos WHERE infos.user_id = '{user_id}'")
        data = self.cur.fetchone()
        info = UserInfo(data[0], data[1], data[2], data[3])
        return info

    def user_info(self, user_id):
        self.cur.execute(f"SELECT * FROM infos WHERE infos.user_id = '{user_id}'")
        data = self.cur.fetchone()
        info = UserInfo(data[1], data[2], data[3], data[4])
        return info

