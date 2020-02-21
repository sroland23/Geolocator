from sqlite3 import OperationalError

import psycopg2
import sqlite3
import random
import arcgis
from psycopg2 import errorcodes
from psycopg2._psycopg import cursor, cursor
from shapely.geometry import Polygon
from binascii import hexlify
from psycopg2.extensions import cursor

connection = psycopg2.connect(database="abc", user="postgres", password = "@bcD!234", host = "127.0.0.1", port = "5432")
cur = connection.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS mygis(id serial primary key,Name text,Type  text,x float,y float,geom geometry);')

try:
    query = cur.execute("SELECT * FROM information_schema.tables WHERE table_name = 'mygis'")
    rows = cur.fetchone()
    print(rows)
except OperationalError as e:
    message = e.args[0]
    if message.startswith("no such table"):
        print("Table 'mygis' does not exist")
        exists = False
    else:
        raise

connection.commit()