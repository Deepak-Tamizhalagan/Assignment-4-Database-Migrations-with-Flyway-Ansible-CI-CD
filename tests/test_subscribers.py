import mysql.connector
import pytest

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "sub_user",
    "password": "sub_pass",
    "database": "subscriptions"
}

@pytest.fixture(scope="module")
def connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    yield conn
    conn.close()

def test_create_subscriber(connection):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO subscribers (email, name) VALUES ('test@example.com', 'Deepak');")
    connection.commit()
    cursor.execute("SELECT COUNT(*) FROM subscribers WHERE email='test@example.com';")
    count = cursor.fetchone()[0]
    assert count == 1

def test_read_subscriber(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM subscribers WHERE email='test@example.com';")
    result = cursor.fetchone()
    assert result is not None and result[0] == 'Deepak'

def test_update_subscriber(connection):
    cursor = connection.cursor()
    cursor.execute("UPDATE subscribers SET name='Updated' WHERE email='test@example.com';")
    connection.commit()
    cursor.execute("SELECT name FROM subscribers WHERE email='test@example.com';")
    result = cursor.fetchone()
    assert result[0] == 'Updated'

def test_delete_subscriber(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM subscribers WHERE email='test@example.com';")
    connection.commit()
    cursor.execute("SELECT COUNT(*) FROM subscribers WHERE email='test@example.com';")
    count = cursor.fetchone()[0]
    assert count == 0
