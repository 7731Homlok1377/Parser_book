from difflib import SequenceMatcher


# s = SequenceMatcher(None, "Джордж Оруэл", "Д. Оруэл")
# print(s.ratio())
class Book:
    default_color = "green"

    def __init__(self, width, height):
        self.width = width
        self.height = height
