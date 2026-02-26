# ============================================================
# PYTHON DICTIONARIES
# ============================================================

# ============================================================
# 1. CREATING DICTIONARIES
# ============================================================

# Empty dictionary
movies = {}
favourite_movies = dict()

# Dictionary with initial values
favourite_books = {
    'author': 'Frank Herbert',
    'title': 'Dune'
}
print(favourite_books)  # Output: {'author': 'Frank Herbert', 'title': 'Dune'}

# Dictionary using the dict() constructor
food = dict(sort='regular', name='fries')
print(food)  # Output: {'sort': 'regular', 'name': 'fries'}

# ============================================================
# 2. ACCESSING VALUES
# ============================================================

person = {
    'name': 'Alice',
    'age': 30,
    'email': 'alice@example.com'
}

# Access by key - direct
print(person['name'])   # Output: Alice
print(person['age'])    # Output: 30

# !!! If the key does not exist, Python raises a KeyError
# print(person['phone'])  # KeyError: 'phone'

# To avoid a KeyError, you can use try/except
try:
    print(person['phone'])
except KeyError:
    print("Key not found!")  # Output: Key not found!

# Or use the safer .get() method - returns None if key doesn't exist
print(person.get('phone'))            # Output: None
print(person.get('phone', 'N/A'))     # Output: N/A (custom default)
print(person.get('name'))             # Output: Alice

# ============================================================
# 3. MODIFYING A DICTIONARY
# ============================================================

# Adding a new key-value pair
person['city'] = 'Bucharest'
print(person)  # Output: {'name': 'Alice', 'age': 30, 'email': 'alice@example.com', 'city': 'Bucharest'}

# Updating an existing value
person['age'] = 31
print(person['age'])  # Output: 31

# Updating multiple values at once with update()
person.update({'email': 'alice@gmail.com', 'country': 'Romania'})
print(person)

# ============================================================
# 4. REMOVING ITEMS
# ============================================================

favourite_food = {
    'name': 'burger',
    'delivered_by': 'burger island',
    'price': '60',
    'currency': 'ron'
}

# del - removes a key (raises KeyError if key doesn't exist)
del favourite_food['currency']
print(favourite_food)  # Output: {'name': 'burger', 'delivered_by': 'burger island', 'price': '60'}

# pop() - removes and returns the value
price = favourite_food.pop('price')
print(price)           # Output: 60
print(favourite_food)  # Output: {'name': 'burger', 'delivered_by': 'burger island'}

# pop() with a default avoids KeyError
result = favourite_food.pop('rating', 'not rated')
print(result)  # Output: not rated (no error)

# popitem() - removes and returns the last inserted item
favourite_food.update({'cooking_type': 'medium_rare'})
last = favourite_food.popitem()
print(last)  # Output: ('cooking_type', 'medium_rare')

# !!! popitem() on an empty dictionary raises a KeyError
empty = {}
try:
    empty.popitem()
except KeyError:
    print("Cannot pop from an empty dictionary!")  # Output: Cannot pop from an empty dictionary!

# clear() - removes all items
favourite_food.clear()
print(favourite_food)  # Output: {}

# ============================================================
# 5. DICTIONARY OPERATIONS
# ============================================================

games = {
    'title': 'Diablo',
    'type': 'RPG',
    'publisher': 'Blizzard'
}

# Check if a key exists
print('title' in games)      # Output: True
print('players' in games)    # Output: False

# Length
print(len(games))  # Output: 3

# ============================================================
# 6. VIEWS: keys(), values(), items()
# ============================================================

# These return dynamic view objects - they update automatically when the dictionary changes

print(games.keys())    # Output: dict_keys(['title', 'type', 'publisher'])
print(games.values())  # Output: dict_values(['Diablo', 'RPG', 'Blizzard'])
print(games.items())   # Output: dict_items([('title', 'Diablo'), ('type', 'RPG'), ('publisher', 'Blizzard')])

# Views are dynamic
games['year'] = 2023
print(games.keys())  # Output: dict_keys(['title', 'type', 'publisher', 'year'])

# ============================================================
# 7. ITERATING
# ============================================================

for key in games:
    print(key, games[key])

for key, value in games.items():
    print(f"{key}: {value}")

# ============================================================
# 8. setdefault() - Get a value or set a default if key is missing
# ============================================================

student = {'name': 'Bob', 'age': 22}

# Key exists - returns existing value, does NOT overwrite
age = student.setdefault('age', 99)
print(age)      # Output: 22 (existing value kept)

# Key doesn't exist - sets it and returns the default
gpa = student.setdefault('gpa', 3.5)
print(gpa)      # Output: 3.5
print(student)  # Output: {'name': 'Bob', 'age': 22, 'gpa': 3.5}

# ============================================================
# 9. DICTIONARY COMPREHENSION
# ============================================================

# Create a dict with squares of numbers
squares = {x: x * x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Create a dictionary from two lists
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combined = {k: v for k, v in zip(letters, numbers)}
print(combined)  # Output: {'a': 1, 'b': 2, 'c': 3}

# ============================================================
# 10. NESTED DICTIONARIES
# ============================================================

# Dictionaries can contain other dictionaries as values
company = {
    'name': 'TechCorp',
    'address': {
        'city': 'Bucharest',
        'country': 'Romania'
    }
}

print(company['address']['city'])  # Output: Bucharest

# Safely access a nested key
print(company.get('address', {}).get('zip', 'No zip code'))  # Output: No zip code
