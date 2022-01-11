class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def name(self):
        return self.name

    def author(self):
        return self.author()

    def pages(self):
        return int(self.pages())