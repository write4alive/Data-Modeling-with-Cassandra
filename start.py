import etl

# Starts project operations


# denormalization and creating new csv file which we going to work on it.
etl.data_denormalization()

# second part which is about all cassandra operations
etl.cassandra_operations()

# etl.cassandra_close():