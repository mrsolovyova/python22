import sqlite3

with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()

    sql = """
                SELECT region.region_name, COUNT (city_name) from city, region
                WHERE region.id = city.region_id
                GROUP BY region.region_name
                ;
            """
    res = cursor.execute(sql)
    for x, y in res.fetchall():
        print([x], ' - ', [y])
