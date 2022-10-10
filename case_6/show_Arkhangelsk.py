import sqlite3

with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()

    sql = """
            select city.city_name from city, region
            where  city.region_id = region.id and region.region_name = 'Архангельская область' 
            ;
        """
    res = cursor.execute(sql)
    for city_name in res.fetchall():
        print(city_name)
