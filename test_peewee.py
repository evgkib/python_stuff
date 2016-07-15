
import peewee as pw
import random

myDB = pw.MySQLDatabase("test", host="localhost", port=3306, user="python", passwd="spartak")

class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB

class Users(MySQLModel):
    id = pw.IntegerField(primary_key = True)
    email = pw.CharField()
    password = pw.CharField()


# when you're ready to start querying, remember to connect
myDB.connect()

for user in Users.select():
    print user.id, user.email, user.password

myDB.close()
