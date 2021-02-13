# class Book :
#     def __init__(self,title,author,pages,price):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.price = price
#
# class LightBook(Book):
#     def __init__(self, title, author, pages, price, backcover):
#         super().__init__(title,author,pages,price)
#         self.backcover = backcover

class A:
    def __init__(self):
        self.name = "A"

class B:
    def __init__(self):
        self.name = "B"

class C(B,A):
    def __init__(self):
        super().__init__()

    def giveName(self):
        print(self.name)

c1 = C()
print(c1.giveName())
