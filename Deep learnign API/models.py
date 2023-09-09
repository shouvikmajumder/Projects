from peewee import Model, SqliteDatabase, CharField, TextField

file = "translations.db"
database= SqliteDatabase(file)

class TranslationModel(Model): 
    text = TextField()
    baselang= CharField()
    finallang = CharField()
    translation = TextField(null=True)

    class Meta:
        db = database

database.create_tables([TranslationModel])
 



