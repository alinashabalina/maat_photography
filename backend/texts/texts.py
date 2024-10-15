from backend.init_db import DataBase


class Text:
    def __init__(self, text_id, content):
        self.id = text_id
        self.content = content


class TextDB(DataBase):
    def __init__(self):
        super().__init__()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS texts
(
    id
    serial \
    PRIMARY
    KEY,
    content varchar);
''')
        self.conn.commit()

    def add_new_text(self, content):
        self.cur.execute('INSERT INTO texts(content)'
                         'VALUES (%s)',
                         content)
        self.conn.commit()


