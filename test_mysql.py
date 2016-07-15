import mysql.connector

cnx = mysql.connector.connect(user='python', password='spartak',host='127.0.0.1',database='test')
cursor = cnx.cursor()
cursor.execute("INSERT INTO users (email, password) values (%s, %s)",("ekibalko@franklinamerican.com", "secret"))
cnx.commit()
cursor.close()
cnx.close()

import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","python","spartak","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * from users")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()

for row in data:
    print(row)

# disconnect from server
db.close()


import peewee as pw
import random

myDB = pw.MySQLDatabase("test", host="localhost", port=3306, user="python", passwd="spartak")

class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB

class User(MySQLModel):
    id = pw.IntegerField(primary_key = True)
    email = pw.CharField()
    password = pw.CharField()

    # etc, etc


# when you're ready to start querying, remember to connect
myDB.connect()
randid = random.randint(1,100000)
user = User(id = randid, email='evgkib@hotmail.com', password='secret')
user.save(force_insert=True)
print user.id
myDB.close()
