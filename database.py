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
    row = tuple(data) + tuple(number)
    return get_event_from_row(row)
#connect_to_db()
#print(get_book_day(1))



def register_for_event(id, email, name):
    connection = get_connection()
    cursor = connection.cursor()
    registration_data = get_book_day(id)
    amount_registered = registration_data["registered_count"]
    max_registered = registration_data["capacity"]
    if amount_registered >= max_registered:
        return RegisterStatus.FULL
    elif is_registered(id, email):
        return RegisterStatus.DUPLICATE
    else:
        query = "INSERT INTO Leesboekingen (dag_id, email, unsubscribe_key, name) VALUES (?, ?, 'abc', ?);"
        cursor.execute(query, [id, email, name])
        connection.commit()
        return RegisterStatus.SUCCES


def delete_leesboekingen():
    connection = get_connection()
    cursor = connection.cursor()
    query = "DELETE FROM Leesboekingen WHERE 1=1;"
    cursor.execute(query)
    connection.commit()


def is_registered(id, email):
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM Leesboekingen WHERE dag_id = ? AND email = ?;"
    cursor.execute(query, [id, email])
    registered = cursor.fetchone()[0]
    if registered == 1:
        return True
    else:
        return False
#delete_leesboekingen()
class RegisterStatus(enumerate):
    SUCCES = 1
    DUPLICATE = 2
    FULL = 3


def add_bookings():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Leesdagen (max_guests, book_name, book_description, date, time, location) VALUES (57, 'Midnight library', 'This is a very cool book!!', '2025-05-30', '17:00:00', 'Narnia');")
    cursor.commit()
#add_bookings()

def get_all_book_days():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT *, (SELECT COUNT(*) FROM Leesboekingen WHERE Leesboekingen.dag_id = Leesdagen.id) FROM Leesdagen;"
    cursor.execute(query)
    data = cursor.fetchall()
    return_list = []
    print(data)
    for row in data:
        return_list.append(get_event_from_row(row))
    return return_list

def get_event_from_row(row):
    vars = {}
    vars["id"] = row[0]
    vars["capacity"] = row[1]
    vars["book_title"] = row[2]
    vars["book_description"] = row[3]
    vars["date"] = row[4]
    vars["time"] = row[5]
    vars["location"] = row[6]
    vars["registered_count"] = row[7]
    return vars

def create_event(data):
    title = data["title"]
    description = data["description"]
    date = data["date"]
    location = data["location"]
    capacity = data["capacity"]
    time = data["time"]
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Leesdagen (max_guests, book_name, book_description, date, time, location) VALUES (?, ?, ?, ?, ?, ?);"
    cursor.execute(query, [capacity, title, description, date, time, location])
    cursor.commit()
#print(get_all_book_days())

def clear_events():
    connection = get_connection()
    cursor = connection.cursor()
    query = "DELETE FROM Leesdagen WHERE date >= '2026-01-01';"
    cursor.execute(query)
    cursor.commit()

def get_registered_for_event(id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Leesboekingen WHERE dag_id = ?;"
    cursor.execute(query, [id])
    data = cursor.fetchall()
    visitors = []
    for row in data:
        visitor = get_visitor_from_row(row)
        visitors.append(visitor)
    return visitors


def get_visitor_from_row(row):
    print(row)
    id = row[0]
    dag_id = row[1]
    email = row[2]
    unsub_token = row[3]
    name = row[4]
    visitor = {
        "id" : id,
        "dag_id" : dag_id,
        "unsub_token" : unsub_token,
        "email" : email,
        "name" : name,
    }
    return visitor

#clear_events()
#print(get_registered_for_event(2))