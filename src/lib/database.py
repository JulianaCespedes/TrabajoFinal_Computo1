import sqlite3 as sq

class Database:
    def __init__(self,name):
        self._con = sq.connect(name)
        self._cursor = self._con.cursor()
    @property
    def connection(self):
        return self._con
    @property
    def cursor(self):
        return self._cursor
    def execute(self,sql,param=None):
        self.cursor.execute(sql,param or ())
    def commit(self):
        self.connection.commit()
    def fetchone(self):
        return self.cursor.fetchone()
    def fetchall(self):
        return self.cursor.fetchall()
