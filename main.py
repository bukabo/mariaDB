import mariadb
import pandas as pd
from constant import maria_connect
from sqlalchemy import create_engine

conn = mariadb.connect(
    user=maria_connect['user'],
    password=maria_connect['pass'],
    host=maria_connect['host'],
    port=maria_connect['port'],
    database=maria_connect['db'])
cur = conn.cursor()


def select():
    # retrieving information
    some_name = "ddd"
    cur.execute("SELECT name, phone FROM test.`table` WHERE name=?", (some_name,))

    for name, phone in cur:
        print(f"First name: {name}, Last name: {phone}")


def insert(name, phone):
    # insert information
    try:
        cur.execute(f"INSERT INTO test.`table` (name, phone) VALUES ('{name}', {phone})")
    except mariadb.Error as e:
        print(f"Error: {e}")

    conn.commit()
    print(f"Last Inserted ID: {cur.lastrowid}")

    conn.close()


def maria_to_df2():
    engine = create_engine(
        f"mariadb:///?User={maria_connect['user']}&;Password={maria_connect['pass']}&Database={maria_connect['db']}&Server={maria_connect['host']}&Port={maria_connect['port']}")
    df = pd.read_sql("SELECT name, phone FROM test.`table`", engine)
    return df


def maria_to_df():
    df = pd.read_sql("SELECT name, phone FROM test.`table`", conn)
    return df


if __name__ == '__main__':
    # select()
    # insert('pipa', 91156845)
    df = maria_to_df()
    print(df)
