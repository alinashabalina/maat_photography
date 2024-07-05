from database.init_db import DataBase


class About:
    def __init__(self, about_id):
        self.id = about_id


class AboutDB(DataBase):
    def __init__(self):
        super().__init__()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS about
(
    id
    serial \
    PRIMARY
    KEY,
    name
    varchar
(
    150
), UNIQUE(name), social_1 varchar
(
    256
), 
social_2 varchar
(
    256
), 
social_3 varchar
(
    256
), 
    photo_link varchar);
''')
        self.conn.commit()

    def add_about_user(self, name, social_1, social_2, social_3, photo_link):
        self.cur.execute('INSERT INTO about (name, social_1, social_2, social_3, photo_link)'
                         'VALUES (%s, %s, %s, %s, %s)',
                         (name, social_1, social_2, social_3, photo_link))
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM users WHERE about.name = '{name}'")
        return self.cur.fetchone()

    def select_all_abouts(self):
        self.cur.execute("SELECT * FROM about")
        return self.cur.fetchall()
