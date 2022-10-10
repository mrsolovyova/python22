import sqlite3

connection = sqlite3.connect("cities.db")

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
        CONSTRAINT UC_city UNIQUE (city_name, region_id)
        );
"""
cursor.execute(create_table_city)

