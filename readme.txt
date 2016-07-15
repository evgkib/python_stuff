
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
