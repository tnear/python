# sqlite3 — DB-API 2.0 interface for SQLite databases
# https://docs.python.org/3/library/sqlite3.html

import sqlite3
import contextlib
import pathlib

def _initTable(cursor):
    # create table with data
    cursor.execute('create table table1(id int, name text);')
    cursor.execute('insert into table1 values (1, "hello");')
    cursor.execute('insert into table1 values (2, "world");')

def _cleanup(db):
    pathlib.Path(db).unlink()

def connect():
    # connect to a database
    # use closing() for automatic cleanup of the db file
    db = 'db.db'
    with contextlib.closing(sqlite3.connect(db)) as connection:
        assert connection.total_changes == 0

    _cleanup(db)

def cursor():
    db = 'db.db'
    with contextlib.closing(sqlite3.connect(db)) as connection:
        # cursor object interfaces with database
        cursor = connection.cursor()
        assert cursor.lastrowid is None

    _cleanup(db)

def fetchall():
    db = 'db.db'
    with contextlib.closing(sqlite3.connect(db)) as connection:
        cursor = connection.cursor()
        _initTable(cursor)

        # fetchall() retrieves all rows
        rows = cursor.execute('select * from table1').fetchall()
        assert rows == [(1, 'hello'), (2, 'world')]

    _cleanup(db)

def fetchone():
    db = 'db.db'
    with contextlib.closing(sqlite3.connect(db)) as connection:
        cursor = connection.cursor()
        _initTable(cursor)
        rows = []

        # get all data
        cursor.execute('select * from table1')

        # get one result at a time in a loop
        while True:
            row = cursor.fetchone()
            if row:
                rows.append(row)
            else:
                break

        assert rows == [(1, 'hello'), (2, 'world')]

    _cleanup(db)

def createIndex():
    db = 'db.db'
    with contextlib.closing(sqlite3.connect(db)) as connection:
        cursor = connection.cursor()
        _initTable(cursor)

        # create index for ID column
        cursor.execute('create index table1_index on table1(id);')

        # get list of indexes
        indexes = cursor.execute('select name from sqlite_master WHERE type="index";').fetchall()
        assert indexes == [('table1_index',)]

    _cleanup(db)

def main():
    connect()
    cursor()
    fetchall()
    fetchone()
    createIndex()

if __name__ == '__main__':
    main()
    print('Tests passed!')
