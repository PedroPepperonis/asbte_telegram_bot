import psycopg2
from psycopg2.extras import DictCursor


class Database:
    def __init__(self, db):
        self.connection = psycopg2.connect(db, sslmode='require')
        self.cursor = self.connection.cursor(cursor_factory=DictCursor)

    def add_user(self, username, first_name, user_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO users(username, first_name, user_id) VALUES(%s,%s,%s)', (username, first_name, user_id))

    def get_user(self, user_id):
        with self.connection:
            self.cursor.execute('SELECT * FROM users WHERE user_id=%s', (user_id,))
            result = self.cursor.fetchall()
            return bool(len(result))

    def get_users(self):
        with self.connection:
            self.cursor.execute('SELECT user_id FROM users')
            result = self.cursor.fetchall()
            return result

    def close(self):
        self.connection.close()
