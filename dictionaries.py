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

# Update multiple values at once
persons.update({'surname': 'Antonia', 'age': '39'})
print(persons)  # Output: {'name': 'Lamba', 'surname': 'Antonia', 'email': 'milena.lamba@yahoo.com', 'children':
# 'yes', 'age': '39'}

# Removing items
favourite_food = {
    'name': 'burger',
    'delivered_by': 'burger island',
    'price': '60',
    'currency': 'ron'
}
print(favourite_food)  # Output{'name': 'burger', 'delivered_by': 'burger island', 'price': '60', 'currency': 'ron'}
del favourite_food['currency']
print(favourite_food)  # Output {'name': 'burger', 'delivered_by': 'burger island', 'price': '60'}

print(favourite_food.pop('price'))  # Output: 60 (pop removes and also returns the removed value)
print(favourite_food)  # Outout: {'name': 'burger', 'delivered_by': 'burger island'}

favourite_food.update({'cooking_type': 'medium_rare'})
print(favourite_food)  # Output {'name': 'burger', 'delivered_by': 'burger island', 'cooking_type': 'medium_rare'}
print(favourite_food.popitem())  # Outout: ('cooking_type', 'medium_rare') (removes last entry and also returns it)
print(favourite_food)  # Output: {'name': 'burger', 'delivered_by': 'burger island'}

# Clear dictionary
favourite_food.clear()  # Output {}

# Dictionary operations
games = {
    'title': 'Diablo',
    'type': 'RPG',
    'publisher': 'Blizzard'
}

# Check if the keys exists
print('title' in games)  # Output: True

# Length of the dictionary
print(len(games))  # Output: 3

# Get all the keys, values, items (Dynamic view; it returns view object)
print(games.keys())  # Output: dict_keys(['title', 'type', 'publisher'])
print(games.values())  # Output: dict_values(['Diablo', 'RPG', 'Blizzard'])
print(games.items())  # Output: dict_items([('title', 'Diablo'), ('type', 'RPG'), ('publisher', 'Blizzard')])
