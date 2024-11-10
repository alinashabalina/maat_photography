from backend.init_db import DataBase


class Issue:
    def __init__(self, issue_id, name, pictures, texts):
        self.id = issue_id
        self.name = name
        self.pictures = pictures
        self.texts = texts


class IssueDB(DataBase):
    def __init__(self):
        super().__init__()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS issues
(
    id
    serial \
    PRIMARY
    KEY,
    name
    varchar
(
    256
), pictures integer array, 
texts integer array);
''')
        self.conn.commit()

    def add_new_issue(self, name, pictures, texts):
        self.cur.execute('INSERT INTO issues (name, pictures, texts)'
                         'VALUES (%s, %s, %s)',
                         (name, pictures, texts))
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM issues WHERE issues.name = '{name}'")
        data = self.cur.fetchone()
        issue = Issue(data[0], data[1], data[2], data[3])
        return issue

    def select_issue_count(self):
        self.cur.execute("SELECT COUNT(*) FROM issues")
        data = self.cur.fetchone()

        return data

    def select_all_issues(self):
        self.cur.execute("SELECT * FROM issues")
        data_many = self.cur.fetchall()
        print(data_many)
        if len(data_many) > 0:
            returned = []
            for el in data_many:
                data = Issue(el[0], el[1], el[2], el[3])
                returned.append(data)
        else:
            returned = 0
        print(returned)
        return returned

