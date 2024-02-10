from difflib import SequenceMatcher
import datetime
from Pony_DB import db
from pony.orm import *



# s = SequenceMatcher(None, "Джордж Оруэл", "Д. Оруэл")
# print(s.ratio())
class Book(db.Entity):

    def __init__(self, name, author, price, path):
        self.name = name
        self.author = author
        self.price = price
        self.time = datetime.datetime.now()
        self.path = path

class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car')
class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(str)