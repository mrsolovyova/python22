import sqlite3
import pandas as pd

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
        city_name TEXT NOT NULL UNIQUE,
        region_id INTEGER NOT NULL UNIQUE,
        FOREIGN KEY(region_id) REFERENCES region(id)
        );
"""
cursor.execute(create_table_city)

