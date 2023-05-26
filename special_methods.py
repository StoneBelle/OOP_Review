# aka "dunder methods" to represent double underscores on each side of the method call
# dunder methods are usefulfor displaying things to the user

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Prints out the str representation of what you want when printing the object."""
        return f"{self.title} written by {self.author}"

    def __len__(self):
        """Prints out the int representation of what you want when printing the object."""
        return self.pages
my_book = Book("JK", "Just Kidding", 000)

print(my_book)
print(len(my_book))

