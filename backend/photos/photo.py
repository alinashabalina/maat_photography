from database.init_db import DataBase

class Photo:
    def __init__(self, photo_id, link):
        self.id = photo_id
        self.link = link


class PhotoDB(DataBase):
    def __init__(self):
        super().__init__()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS photos
(
    id
    serial \
    PRIMARY
    KEY,
    link varchar);
''')
        self.conn.commit()

    def add_new_photo(self, link):
        self.cur.execute('INSERT INTO photos(link)'
                         'VALUES (%s)',
                         (link))
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM photos WHERE photos.link = '{link}'")
        data = self.cur.fetchone()
        photo = Photo(data[0], data[1])
        return photo
