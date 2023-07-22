from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print('Title: ' + str(self.title))
        print('Author: ' + str(self.author))
        print('Price: ' + str(self.price))

title=input("Enter Title")
author=input("Enter Author Name:")
price=int(input("Enter price"))
new_novel=MyBook(title,author,price)
new_novel.display()
