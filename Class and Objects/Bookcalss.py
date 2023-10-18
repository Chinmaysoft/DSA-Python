class Book:

    def __init__(self,bookid = None,title = None,price = None):
        self.bookid = bookid
        self.title = title
        self.price = price

    def DisplayBook(self):
        print(f"Please find details of books.. \n Book Id : {self.bookid} \n Book Title : {self.title} \n Book Price : {self.price}")


bookid = int(input("Enter Book Id :"))
title = input("Enter a Book title :")
price = float(input("Enter a Book Price :"))

b1 = Book(bookid,title,price)

b1.DisplayBook()