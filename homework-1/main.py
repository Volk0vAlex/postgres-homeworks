"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

employees = os.path.abspath('north_data/employees_data.csv')
customers = os.path.abspath('north_data/customers_data.csv')
orders = os.path.abspath('north_data/orders_data.csv')

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')

try:
    with conn:
        with conn.cursor() as cur:
            with open(employees, 'r', encoding='utf-8') as file:
                info = csv.reader(file)
                next(info)
                for row in info:
                    cur.execute("INSERT INTO employees (%s, %s, %s, %s, %s, %s)",
                                (row[0], row[1], row[2], row[3], row[4], row[5]))

                    cur.execute("SELECT * FROM employees")

finally:
    conn.close()

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')

try:
    with conn:
        with conn.cursor() as cur:
            with open(customers, 'r', encoding='utf-8') as file:
                info = csv.reader(file)
                next(info)
                for row in info:
                    cur.execute("INSERT INTO customers (%s, %s, %s)",
                                (row[0], row[1], row[2]))

                    cur.execute("SELECT * FROM customers")

finally:
    conn.close()

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')

try:
    with conn:
        with conn.cursor() as cur:
            with open(orders, 'r', encoding='utf-8') as file:
                info = csv.reader(file)
                next(info)
                for row in info:
                    cur.execute("INSERT INTO orders (%s, %s, %s, %s, %s)",
                                (row[0], row[1], row[2], row[3], row[4]))

                    cur.execute("SELECT * FROM orders")

finally:
    conn.close()
