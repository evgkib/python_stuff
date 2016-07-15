
import peewee as pw
import random
from datetime import date

myDB = pw.MySQLDatabase("test", host="localhost", port=3306, user="python", passwd="spartak")
class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB

class User(MySQLModel):
    id = pw.PrimaryKeyField()
    email = pw.CharField(index = True)
    password = pw.CharField()
    hiredate = pw.DateTimeField()

class Broker(MySQLModel):
    broker_id = pw.PrimaryKeyField()
    email = pw.CharField(index = True)
    active = pw.BooleanField(default=False)
    rep_id = pw.ForeignKeyField(User)

# when you're ready to start querying, remember to connect
myDB.connect()
myDB.create_tables([User, Broker], safe=True)
user = User(email='ekibalko@franklinamerican.com', password='secret', hiredate=date(2010, 5, 2))
broker = Broker(email='broker@morg.com', active=True, rep_id = user)
user.save()
broker.save()
for user in User.select():
    print user.id, user.email, user.password, user.hiredate

myDB.close()
