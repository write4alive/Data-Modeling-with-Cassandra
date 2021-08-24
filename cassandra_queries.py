# cassandra_queris.py contains keyspace queries for cassandra

# create keyspace 
q_create_keyspace=("""
CREATE KEYSPACE IF NOT EXISTS project2 
WITH REPLICATION = 
{ 'class' : 'SimpleStrategy', 'replication_factor' : 1 } """)

# create tables

# query = "CREATE TABLE IF NOT EXISTS music_library "
# query = query + "(year int, artist_name text, album_name text, PRIMARY KEY (year, artist_name))"
# try:
#     session.execute(query)
# except Exception as e:
#     print(e)


# insert tables

# query = "INSERT INTO music_library (year, artist_name, album_name)"
# query = query + " VALUES (%s, %s, %s)"

# query1 = "INSERT INTO album_library (artist_name, year, album_name)"
# query1 = query1 + " VALUES (%s, %s, %s)"

# try:
#     session.execute(query, (1970, "The Beatles", "Let it Be"))
# except Exception as e:
#     print(e)


# select from tables

# query = "select * from music_library WHERE YEAR=1970"
# try:
#     rows = session.execute(query)
# except Exception as e:
#     print(e)
    
# for row in rows:
#     print (row.year, row.artist_name, row.album_name,)



# drop tables

# query = "drop table music_library"
# try:
#     rows = session.execute(query)
# except Exception as e:
#     print(e)