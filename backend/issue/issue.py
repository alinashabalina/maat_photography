from backend.init_db import DataBase


class Issue:
    def __init__(self, issue_id, name, articles, pictures, editorial):
        self.id = issue_id
        self.name = name
        self.articles = articles
        self.pictures = pictures
        self.editorial = editorial


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
), articles integer array, 
pictures integer array,
editorial varchar);
''')
        self.conn.commit()

    def add_new_issue(self, name, articles, pictures, editorial):
        self.cur.execute('INSERT INTO issues (name, articles, pictures, editorial)'
                         'VALUES (%s, %s, %s, %s)',
                         (name, articles, pictures, editorial))
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM issues WHERE issues.name = '{name}'")
        data = self.cur.fetchone()
        issue = Issue(data[0], data[1], data[2], data[3], data[4])
        return issue

    def select_issue_count(self):
        self.cur.execute("SELECT COUNT(*) FROM issues")
        data = self.cur.fetchone()

        return data

    def select_all_issues(self):
        self.cur.execute("SELECT * FROM issues")
        data_many = self.cur.fetchall()
        if len(data_many) > 0:
            returned = []
            for el in data_many:
                data = Issue(el[0], el[1], el[2], el[3], el[4])
                returned.append(data)
        else:
            returned = 0
        return returned

