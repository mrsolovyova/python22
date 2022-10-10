import sqlite3

with sqlite3.connect('cities.db') as connection:
    cursor = connection.cursor()

    sql1 = """
        DROP TABLE IF EXISTS city;
    """
    cursor.execute(sql1)

    sql2 = """
        DROP TABLE IF EXISTS region;
    """
    cursor.execute(sql2)
