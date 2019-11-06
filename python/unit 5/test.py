library = [
    'To Kill a Mockingbird', 
    'The Catcher in the Rye', 
    'The Great Gatsby',
    'Gone with the Wind'
]

print('Welcome to the library!')

print('Selection: ')

for book in library:
    print(f'{library.index(book)} - {book}')

choice = input('Pick out a book: ')

def thing()