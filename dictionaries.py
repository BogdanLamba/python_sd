# Create an empty dict
movies = {}  # output of print - > {}
favourite_movies = dict()  # Output: of print - > {}

# Dictionary with initial values
favourite_books = {
    'author': 'Frank Herbert',
    'title': 'Dune'
}
print(favourite_books)  # Output: {'author': 'Frank Herbert', 'title': 'Dune'}

# Dictionary with constructor
food = dict(sort='regular', name='fries')
print(food)  # output {'sort': 'regular', 'name': 'fries'}

# Accessing values by key
favourite_books_second = {
    'author': 'Frank Herbert',
    'title': 'Dune'
}
print(f"{favourite_books_second['title']}")  # Output Dune

# Accessing by using get methods (safer as it returns None if the key does not exist
print(favourite_books_second.get("Author"))  # Output: None
print(favourite_books_second.get("author"))  # Output: Frank Herbert
# !!! Interesting - add default message instead of None
print(favourite_books_second.get("Author", "This key does not exist"))  # Output: This key does not exist

# Modifying a dictionary
persons = {
    'name': 'Lamba',
    'surname': 'Milena',
    'email': 'mlamba@yahoo.com'
}

# Adding a new key value pair
persons['children'] = 'yes'
print(persons)  # Output {'name': 'Lamba', 'surname': 'Milena', 'email': 'mlamba@yahoo.com', 'children': 'yes'}

# Update existing value
print(persons)  # Output: {'name': 'Lamba', 'surname': 'Milena', 'email': 'mlamba@yahoo.com'}
persons['email'] = 'milena.lamba@yahoo.com'
print(persons)  # Output: {'name': 'Lamba', 'surname': 'Milena', 'email': 'milena.lamba@yahoo.com'}
