import pymysql

HOST = "remotemysql.com"
PORT = 3306
USER = "yUnzgHhpnT"
PASSWORD = "M1JOXyXOlh"
DB = "yUnzgHhpnT"


class DataBase(object):
    def __init__(self):
        self.conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()

    def get_user_name(self, user_id):
        query = "SELECT * FROM yUnzgHhpnT.users WHERE id =" + user_id
        self.cursor.execute(query)
        user_c = self.cursor.fetchall()
        self.cursor.close
        return user_c[0][1]

    def create_user(self, user_id, user_name):
        query = "INSERT into yUnzgHhpnT.users (name, id) VALUES (%s, %s)"
        data = (user_name, user_id)
        self.cursor.execute(query, data)
        self.cursor.close

    def update_user(self, user_id, user_name):
        query = "UPDATE yUnzgHhpnT.users SET name = '" + user_name + "' WHERE id =" + user_id
        print(query)
        self.cursor.execute(query)
        self.cursor.close

    def delete_user(self, user_id):
        query = "DELETE FROM yUnzgHhpnT.users WHERE id =" + user_id
        print(query)
        self.cursor.execute(query)
        self.cursor.close

    def __del__(self):
        if self.cursor:
            self.cursor.close

        self.conn.close


if __name__ == '__main__':
    db = DataBase()
    db.close()
