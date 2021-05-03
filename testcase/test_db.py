import psycopg2
import pytest
import os


@pytest.mark.skip('')
def test_db():

    db_pwd = os.getenv('DB_PWD')
    print(db_pwd)
    conn = psycopg2.connect(database="test", user="postgres", password=db_pwd)

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM company;')
    rows = cursor.fetchall()

    for row in rows:
        for ro in row:
            print(ro)

    conn.close()
