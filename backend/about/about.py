from database.init_db import DataBase


class About:
    def __init__(self, about_id, name, social_1, social_2, social_3, photo_link):
        self.id = about_id
        self.name = name
        self.social_1 = social_1
        self.social_2 = social_2
        self.social_3 = social_3
        self.photo_link = photo_link


class AboutDB(DataBase):
    def __init__(self):
        super().__init__()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS abouts
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
        self.cur.execute('INSERT INTO abouts (name, social_1, social_2, social_3, photo_link)'
                         'VALUES (%s, %s, %s, %s, %s)',
                         (name, social_1, social_2, social_3, photo_link))
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM abouts WHERE abouts.name = '{name}'")
        data = self.cur.fetchone()
        about = About(data[0], data[1], data[2], data[3], data[4], data[5])
        return about

    def select_all_abouts(self):
        self.cur.execute("SELECT * FROM abouts")
        data_many = self.cur.fetchall()
        returned = []
        for el in data_many:
            data = About(el[0], el[1], el[2], el[3], el[4], el[5])
            returned.append(data)

        return returned

