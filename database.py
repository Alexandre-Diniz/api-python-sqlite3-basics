import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

def insert_in_table(values):
    database = r"./pythonsqlite.db"
    conn = create_connection(database)

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        conn.execute("INSERT INTO projects VALUES (?,?,?,?)",values)
        conn.commit()

    else:
        print("Error! cannot create the database connection.")

def search_in_table_by_id(id):
    database = r"./pythonsqlite.db"
    conn = create_connection(database)

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        result = conn.execute("select * from projects where id=:id", {"id": id})
        conn.commit()
        return result.fetchall()

    else:
        print("Error! cannot create the database connection.")
        return []

def search_in_table_all():
    database = r"./pythonsqlite.db"
    conn = create_connection(database)

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        task = conn.execute("select * from projects")
        conn.commit()
        result = task.fetchall()
        task.close()
        print(result)
        return result

    else:
        print("Error! cannot create the database connection.")
        return []

search_in_table_all()