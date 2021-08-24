# cassandra_queris.py contains keyspace queries for cassandra

# create keyspace 
q_create_keyspace=("""
CREATE KEYSPACE IF NOT EXISTS project2 
WITH REPLICATION = 
{ 'class' : 'SimpleStrategy', 'replication_factor' : 1 } """)


# create question query tables
q_create_table_1=(""" 
CREATE TABLE IF NOT EXISTS q1_table (artist text ,song text, length text,sessionid int ,iteminsession int, primary key(artist,song))
""")

q_create_table_2=(""" 
CREATE TABLE IF NOT EXISTS q2_table (artist text ,song text, firstname text ,lastname text,sessionid int ,userid int, primary key(artist,song))
""")

q_create_table_3=(""" 
CREATE TABLE IF NOT EXISTS q3_table (firstname text, lastname text ,song text, userid int, primary key(userid))
""")


#  List of Tables for bulk create and drop operations
q_tables_create=[q_create_table_1,q_create_table_2,q_create_table_3]

q_tables_drop=[]


# query = "CREATE TABLE IF NOT EXISTS music_library "
# query = query + "(year int, artist_name text, album_name text, PRIMARY KEY (year, artist_name))"
# try:
#     session.execute(query)
# except Exception as e:
#     print(e)


# insert tables

q1_table_insert =("""
insert into q1_table(artist  ,song , length ,sessionid  ,iteminsession ) values(%s,%s,%s,%s,%s)
""")

# query = "INSERT INTO music_library (year, artist_name, album_name)"
# query = query + " VALUES (%s, %s, %s)"

# query1 = "INSERT INTO album_library (artist_name, year, album_name)"
# query1 = query1 + " VALUES (%s, %s, %s)"

# try:
#     session.execute(query, (1970, "The Beatles", "Let it Be"))
# except Exception as e:
#     print(e)


# select from tables

q_select_1=("""
SELECT artist,song,length from q1_table where sessionid= 338 and iteminsession=4
""")

q_select_2=("""
SELECT artist,song,firstname ,lastname from q2_table where sessionid= 182 and userid=10 order by iteminsession
""")

q_select_3=("""
SELECT firstname ,lastname from q3_table where song='All Hands Against His Own'
""")


# query = "select * from music_library WHERE YEAR=1970"
# try:
#     rows = session.execute(query)
# except Exception as e:
#     print(e)
    
# for row in rows:
#     print (row.year, row.artist_name, row.album_name,)



# drop tables
q_drop_table_1=("""drop table if exists q1_table
""")

# query = "drop table music_library"
# try:
#     rows = session.execute(query)
# except Exception as e:
#     print(e)
