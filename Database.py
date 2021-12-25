from peewee import SqliteDatabase, Model, BigIntegerField

db = SqliteDatabase('bot.db')


class Users(Model):
    chat_id = BigIntegerField(primary_key=True)

    class Meta:
        database = db


db.connect()
db.create_tables([Users])
