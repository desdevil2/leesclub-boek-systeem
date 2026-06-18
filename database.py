import psycopg2
from credentials import database
def connect_to_db():
    try:
        connection = psycopg2.connect(database)
        cursor = connection.cursor()
        #cursor.execute("CREATE TABLE Leesdagen (id serial PRIMARY KEY, max_guests int , book_name varchar, book_description varchar , date date, time time);")
        #cursor.execute("INSERT INTO Leesdagen VALUES (DEFAULT, 10, 'The hunger games', 'This is a cool book', '2001/12/15', '19:00')")
        #connection.commit()
        cursor.execute("SELECT * FROM Leesdagen;")
        data = cursor.fetchall()
        print(data)
    except Exception as e:
        print("Error!")
        print(e)
connect_to_db()