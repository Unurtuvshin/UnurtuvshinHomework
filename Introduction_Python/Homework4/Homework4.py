import psycopg2 as ps
import pandas as pd

connection = ps.connect(
    user = "postgres",
    password = "postgres",
    host = "localhost",
    port = "5432",
    database = "mydata"
)

cursor = connection.cursor()

cursor.execute("CREATE TABLE mytable (id integer, firstName text, lastName text, age integer);")
cursor.execute("COPY mytable FROM 'C:\\Users\\unur0\\Desktop\\projects\\Python\\UnurtuvshinHomework\\Homework4\\data.csv' DELIMITER ',' CSV HEADER;")
cursor.execute("SELECT * FROM mytable;")
record = cursor.fetchall()
record

cursor.execute("SELECT firstName, lastName from mytable order by id asc limit 3;")
task2 = cursor.fetchall()
df2 = pd.DataFrame(task2)
df2.columns = ['firstName', 'lastName']
print(df2)
# task2 = first 3: firstname, lastname

cursor.execute("SELECT firstName, age from mytable order by id desc limit 3;")
task3 = cursor.fetchall()
df3 = pd.DataFrame(task3)
df3.columns = ['firstName', 'age']
print(df3)
# task3 = last 3: firstname, age

cursor.close()
connection.close()


