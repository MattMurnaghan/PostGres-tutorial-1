import psycopg2

# connect to the chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * from "Artist"')

# Query 2 - Select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" =%s', [51])

# Query 5 - Select only the albums with "ArtistId" = #51 from the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" =%s', [51])

# Query 6 - Select all tracks where the "Composer" is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Test"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connecton
connection.close()

# print the results
for result in results:
    print(result)
