import sqlite3
import pandas as pd

with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()

file = pd.read_csv('towns.csv')
# делаю список кортежей из отсортированных регионов без дубляжа
region_name = list(zip(tuple(sorted(set(file.region_name)))))
for x in range(len(region_name)):
    cursor.execute("""INSERT INTO region (region_name) VALUES (?);""", region_name[x])
    connection.commit()


cities_name = list(file.city)
region_name = list(zip(tuple(file.region_name)))

for x in range(len(cities_name)):
    res = cursor.execute('select id from region where region_name = ?', region_name[x])
    region_id = res.fetchone()[0]
    name = cities_name[x]
    cursor.execute("""INSERT INTO city (city_name, region_id) VALUES (?,?);""", (name, region_id))
    connection.commit()
