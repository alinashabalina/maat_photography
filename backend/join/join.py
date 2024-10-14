from backend.init_db import DataBase

class Join:
    def __init__(self, join_id, name, email, link):
        self.id = join_id
        self.name = name
        self.email = email
        self.link = link


class JoinDB(DataBase):
    def __init__(self):
        super().__init__()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS joins
(
    id
    serial \
    PRIMARY
    KEY,
    name
    varchar
(
    150
), email varchar (256), 
  UNIQUE(email), 
    link varchar);
''')
        self.conn.commit()

    def add_join_request(self, name, email, link):
        self.cur.execute('INSERT INTO joins (name, email, link)'
                         'VALUES (%s, %s, %s)',
                         (name, email, link))
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM joins WHERE joins.email = '{email}'")
        data = self.cur.fetchone()
        join = Join(data[0], data[1], data[2], data[3])
        return join
