import sqlite3
from sqlite3 import Error


class DataBase():
    def __init__(self):
        self.__conn = None
        self.__db_file = r"./pythonsqlite.db"
        self.__create_table_sql = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
        self.__create_table()
    
    def __create_connection(self):
        try:
            self.__conn = sqlite3.connect(self.__db_file)
        except Error as e:
            print(e)
    
    def __create_table(self):
        try:
            self.__create_connection()
            self.__conn.cursor().execute(self.__create_table_sql)
            self.__conn.commit()
        except Error as e:
            print(e)
    
    def search_in_table_all(self):

        if self.__conn is not None:
            task = self.__conn.execute("select * from projects")
            self.__conn.commit()
            result = task.fetchall()
            task.close()
            return result

        else:
            print("Error! cannot create the database connection.")
            return []
    
    def find_by_id(self,id):
        if self.__conn is not None:
            result = self.__conn.execute("select * from projects where id=:id", {"id": id})
            self.__conn.commit()
            self.__conn.close()
            return result.fetchall()
            
        else:
            print("Error! cannot create the database connection.")
            return []

    def insert_one(self, values):
        if self.__conn is not None:
            self.__conn.execute("INSERT INTO projects VALUES (?,?,?,?)",values)
            self.__conn.commit()
            self.__conn.close()

        else:
            print("Error! cannot create the database connection.")