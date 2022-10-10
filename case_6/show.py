import sqlite3

with sqlite3.connect('cities.db') as connection:
    cursor = connection.cursor()

    sql = """
        select * from region
    """
    res = cursor.execute(sql)
    for region in res.fetchall():
        print(region)
