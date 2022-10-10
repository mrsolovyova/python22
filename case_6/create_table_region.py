import sqlite3
import pandas as pd

with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()

create_table_region = """
    CREATE TABLE region(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        region_name TEXT NOT NULL
    );
"""
cursor.execute(create_table_region)

create_table_city = """
    CREATE TABLE city(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_name TEXT NOT NULL,
        region_id INTEGER NOT NULL,
        FOREIGN KEY(region_id) REFERENCES region(id)
        );
"""
cursor.execute(create_table_city)

file = pd.read_csv('towns.csv')
# делаю список кортежей из отсортированных регионов без дубляжа
region_name = list(zip(tuple(sorted(set(file.region_name)))))
cursor.executemany("""INSERT INTO region (region_name) VALUES (?);""", region_name)
connection.commit()


cities_name = list(zip(tuple(file.city)))
region_name = list(zip(tuple(file.region_name)))
list_of_id = []
for x in range(len(region_name)):
    res = cursor.execute('select id from region where region_name = ?', region_name[x])
    region_id = res.fetchone()[0]
    list_of_id.append(region_id)
result_id = list(zip(tuple(list_of_id)))
cursor.executemany("""INSERT INTO city (city_name, region_id) VALUES (?,?);""", ((cities_name, ), (result_id, ), ))
connection.commit()
