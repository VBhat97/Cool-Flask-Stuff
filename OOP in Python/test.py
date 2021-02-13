class Book :
    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

class LightBook(Book):
    def __init__(self, title, author, pages, price, backcover):
        super().__init__(title,author,pages,price)
        self.backcover = backcover


L1 = LightBook("Small things","John Reynold",321,29.95,"cardboard")
B1 = Book("Small things","John Reynold",321,29.95)

print(L1.backcover)
