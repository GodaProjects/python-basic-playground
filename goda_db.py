import sqlite3

database_connection = sqlite3.connect("goda.db")
print("Database created")
database_cursor = database_connection.cursor()
print(database_cursor)

# Create table
try:
    database_connection.execute(
        "CREATE TABLE IF NOT EXISTS Friends(ID integer primary key autoincrement not null, name TEXT, age INT, gender TEXT);")
    database_connection.commit()
    database_connection.execute(
        "insert into Friends (name, age, gender)" "VALUES('Goda', 15, 'f')")
    database_connection.execute(
        "insert into Friends (name, age, gender)" "VALUES('Tanu', 14, 'f')")
    result = database_connection.execute("select * from Friends")
    print(result)
    for row in result:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
except sqlite3.OperationalError:
    print("Table not created")
except:
    print("Error")
