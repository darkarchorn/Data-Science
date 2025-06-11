import sqlite3

class DatabaseConnection:
    def __init__(self, db_path):
        self.__connection = sqlite3.connect(db_path, check_same_thread=False)
        self.__connection.execute('''
        CREATE TABLE IF NOT EXISTS Human (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            job TEXT
        )
        ''')
        self.__connection.commit()

    def getConnection(self):
        return self.__connection
