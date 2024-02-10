from pony.orm import *


from config import host, user, password, db_name


db = Database()


# @db_session
# def add_car(make, model):
#     Car(make=make, model=model, owner="22")

class Person(db.Entity):
    name = Required(str)
    age = Required(int)

class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(str)

db.bind(provider='postgres', user=user, password=password, host=host, database=db_name)
db.generate_mapping(create_tables=True)

set_sql_debug(True)
with db_session:
    p = Person(name='Kate', age=33)
    Car(make='Audi', model='R8', owner="p")
# p1 = Person(name='John', age=20)
# p2 = Person(name='Mary', age=22)
# p3 = Person(name='Bob', age=30)
# c1 = Car(make='Toyota', model='Prius', owner="p2")
# c2 = Car(make='Ford', model='Explorer', owner="p3")
# commit()