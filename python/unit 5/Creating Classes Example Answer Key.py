"""Unit 5 - Creating Classes
In this example there will be 4 different tasks to complete by creating classes.
Make sure to run your code in between each task to make sure that program is working correctly before moving on."""

# Task 1: Create a class called "Books". Creating the __init__ function for this class that defines what this object contains.
# You should include title, author, ISBN number, and number of pages.

class Books:
    def __init__(self, title, author, isbn, pages):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages

# Task 2: Create an object "book_1" using your Books class you created above. Make sure you give the object all of the
# parameters from above (title, author, ISBN, number of pages). Repeat with "book_2" and "book_3"

book_1 = Books("A Tale of Two Cities", "Charles Dickens", 9781562542788, 341)
book_2 = Books("Great Expectations", "Charles Dickens", 9781517717704, 544)
book_3 = Books("Oliver Twist", "Charles Dickens", 9780812580037, 496)

# Task 3: Print the title of "book_1", the author of "book_2", and the number of pages of "book_3".

print(book_1.title)
print(book_2.author)
print(book_3.pages)

# Task 4: Have the user create an object "book_4", where they enter all of the parameters. Then, print each of the book_4 
# parameters to check that the object has been created correctly.

book_4_title = input("What is the title of the book: ")
book_4_author = input("Who is the author of the book: ")
book_4_isbn = input("What is the ISBN number of the book: ")
book_4_pages = input("What is the number of pages of the book: ")

book_4 = Books(book_4_title, book_4_author, book_4_isbn, book_4_pages)

print(book_4.title, book_4.author, book_4.isbn, book_4.pages)