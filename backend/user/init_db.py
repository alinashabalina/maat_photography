import psycopg2


class DataBase:
    database = "maat_user"
    user = "postgres"
    password = "postgres"
    host = "localhost"
    port = "5432"

    def __init__(self):
        self.conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host,
                                     port=self.port)
        self.cur = self.conn.cursor()
