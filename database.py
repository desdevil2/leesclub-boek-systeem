import psycopg2
from credentials import database
def connect_to_db():
    try:
        connection = psycopg2.connect(database)
        cursor = connection.cursor()
        #cursor.execute("CREATE TABLE Leesdagen (id serial PRIMARY KEY, max_guests int , book_name varchar, book_description varchar , date date, time time);")
        #cursor.execute("INSERT INTO Leesdagen VALUES (DEFAULT, 10, 'The hunger games', 'This is a cool book', '2001/12/15', '19:00')")
        #cursor.execute("CREATE TABLE Leesboekingen (id SERIAL PRIMARY KEY, dag_id int, email varchar, unsubscribe_key varchar, CONSTRAINT dag FOREIGN KEY (dag_id) REFERENCES Leesdagen(id));")
        #cursor.execute("INSERT INTO Leesboekingen VALUES (DEFAULT, 1, 'robinweynjes@gmail.com', 'abc');")
        cursor.execute("DELETE FROM Leesdagen WHERE id = 2;")
        connection.commit()
        #cursor.execute("SELECT * FROM Leesdagen;")
        #data = cursor.fetchall()
    except Exception as e:
        print("Error!")
        print(e)



def get_cursor():
    connection = psycopg2.connect(database)
    cursor = connection.cursor()
    return cursor


def get_book_day(id):
    cursor = get_cursor()
    query = "SELECT * FROM Leesdagen WHERE id = (%s)"
    cursor.execute(query, [id])
    data = cursor.fetchone()
    query = "SELECT COUNT(*) FROM Leesboekingen WHERE dag_id = (%s)"
    cursor.execute(query, [id])
    number = cursor.fetchone()
    return data + number
print(get_book_day(1))
#connect_to_db()