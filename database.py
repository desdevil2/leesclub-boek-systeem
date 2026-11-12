import pyodbc
from credentials import database
def connect_to_db():
    try:
        connection = pyodbc.connect(database)
        cursor = connection.cursor()
        cursor.commit()
        cursor.execute("CREATE TABLE Leesdagen (id INT IDENTITY(1,1) PRIMARY KEY, max_guests INT, book_name VARCHAR(255), book_description VARCHAR(MAX), date DATE, time TIME, location VARCHAR(255));")
        cursor.execute("INSERT INTO Leesdagen (max_guests, book_name, book_description, date, time, location) VALUES (10, 'The hunger games', 'This is a cool book', '2001-12-15', '19:00:00', 'Meilweg 7, 3600 Genk');")
        cursor.execute("CREATE TABLE Leesboekingen (id INT IDENTITY(1,1) PRIMARY KEY, dag_id INT, email VARCHAR(255), unsubscribe_key VARCHAR(255), CONSTRAINT dag FOREIGN KEY (dag_id) REFERENCES Leesdagen(id));")
        cursor.execute("INSERT INTO Leesboekingen (dag_id, email, unsubscribe_key) VALUES (1, 'robinweynjes@gmail.com', 'abc');")
        #cursor.execute("DELETE FROM Leesdagen WHERE id = 2;")
        connection.commit()
        #cursor.execute("SELECT * FROM Leesdagen;")
        #data = cursor.fetchall()
        print("SUCCES")
    except Exception as e:
        print("Error!")
        print(e)



def get_connection():
    connection = pyodbc.connect(database)
    return connection


def get_book_day(id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Leesdagen WHERE id = ?"
    cursor.execute(query, [id])
    data = cursor.fetchone()
    query = "SELECT COUNT(*) FROM Leesboekingen WHERE dag_id = ?"
    cursor.execute(query, [id])
    number = cursor.fetchone()
    return tuple(data) + tuple(number)
#connect_to_db()
print(get_book_day(1))



def register_for_event(id, email):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Leesboekingen (dag_id, email, unsubscribe_key) VALUES (?, ?, 'abc');"
    cursor.execute(query, [id, email])
    connection.commit()
    cursor.execute("SELECT * FROM Leesboekingen;")
    data = cursor.fetchall()
    print(data)


def delete_leesboekingen():
    connection = get_connection()
    cursor = connection.cursor()
    query = "DELETE FROM Leesboekingen WHERE 1=1;"
    cursor.execute(query)
    connection.commit()

#delete_leesboekingen()