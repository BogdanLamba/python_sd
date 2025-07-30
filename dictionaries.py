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

# Iteration
for key in games:
    print(key, games[key])  # Output:
    '''
    title Diablo
    type RPG
    publisher Blizzard
    '''
for key, value in games.items():
    print(key, value)  # Output:
    '''
    title Diablo
    type RPG
    publisher Blizzard
    '''

# Dictionaty comprehension
# Create a dict with squares of numbers
squares = {x: x * x for x in range(1, 10)}
print(squares)

# Create a dictionary from 2 lists (get k,v from each list and combine them)
let = ['a', 'b', 'c']
num = [1, 2, 3, ]
combined = {k: v for k, v in zip(let, num)}
print(combined)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Python Dictionary Methods: A Deep Dive with Examples

# Access Methods
# 1. keys() - Get all dictionary keys
# Returns a view object containing the dictionary's keys.
student = {"name": "Alice", "age": 22, "major": "Computer Science"}

# Get all keys
keys = student.keys()
print(keys)  # Output dict_keys(['name', 'age', 'major'])

# Convert to list if needed
key_list = list(student.keys())
print(key_list)  # Output ['name', 'age', 'major']

# Keys view is dynamic
student["year"] = "Senior"
print(keys)  # Output dict_keys(['name', 'age', 'major', 'year'])

# 2. values() - Get all dictionary values
# Returns a view object containing the dictionary's values.
values = student.values()
print(values)  # Output dict_values(['Alice', 22, 'Computer Science', 'Senior'])

# Convert to list
value_list = list(student.values())
print(value_list)  # Output ['Alice', 22, 'Computer Science', 'Senior']

# Values view is dynamic
student["age"] = 23
print(values)  # Output dict_values(['Alice', 23, 'Computer Science', 'Senior'])

# 3. items() - Get all key-value pairs -> Returns a view object containing (key, value) tuples.
items = student.items()
print(items)  # dict_items([('name', 'Alice'), ('age', 23), ('major', 'Computer Science'), ('year', 'Senior')])

# Convert to list
item_list = list(student.items())
print(item_list)  # [('name', 'Alice'), ('age', 23), ('major', 'Computer Science'), ('year', 'Senior')]

# Useful for iteration
for key, value in student.items():
    print(f"{key}: {value}")

# 4. get() - Safe value access
# Returns the value for a key if it exists, otherwise returns None or a default value.
# Basic usage
print(student.get("name"))  # Alice
print(student.get("gpa"))  # None

# With default value
print(student.get("gpa", 3.5))  # 3.5 (default since 'gpa' doesn't exist)

# Doesn't add the key to dictionary
print(student)  # {'name': 'Alice', 'age': 23, 'major': 'Computer Science', 'year': 'Senior'}

# 5. setdefault() - Get with automatic setting
# Returns the value if key exists, otherwise sets the key to the default value and returns it.
# Key exists
age = student.setdefault("age", 24)
print(age)  # 23 (existing value)
print(student)  # age remains 23 {'name': 'Alice', 'age': 23, 'major': 'Computer Science', 'year': 'Senior'}

# Key doesn't exist
gpa = student.setdefault("gpa", 3.7)
print(gpa)  # 3.7
print(
    student)  # Now includes 'gpa': 3.7 {'name': 'Alice', 'age': 23, 'major': 'Computer Science', 'year': 'Senior', 'gpa': 3.7}

# Modification Methods
# 1. update() - Merge dictionaries
# Updates the dictionary with elements from another dictionary or iterable.

# Update with another dictionary
student.update({"minor": "Mathematics", "age": 24})
print(student)
# {'name': 'Alice', 'age': 24, 'major': 'Computer Science', 'year': 'Senior', 'gpa': 3.7, 'minor': 'Mathematics'}

# Update with iterable of key-value pairs
student.update([("year", "Graduating"), ("advisor", "Dr. Smith")])
print(student)
# Now includes 'advisor': 'Dr. Smith' and year is 'Graduating'

# 2. pop() - Remove by key
# Removes the specified key and returns its value.
# Remove and get a value
major = student.pop("major")
print(major)  # Computer Science
print(student)  # major is removed

# With default value to avoid KeyError
hometown = student.pop("hometown", "Unknown")
print(hometown)  # Unknown (default returned, no KeyError)

# 3. popitem() - Remove last item (Python 3.7+)
# Removes and returns the last inserted (key, value) pair.


# Remove last item
last_item = student.popitem()
print(last_item)  # ('advisor', 'Dr. Smith')
print(student)  # advisor is removed

# Empty dictionary raises KeyError
empty_dict = {}
# empty_dict.popitem()  # Raises KeyError

# 4. clear() - Remove all items
# Removes all items from the dictionary.
student.clear()
print(student)  # {}

# Dictionary Views

# The keys(), values(), and items() methods return view objects that provide dynamic views of the dictionary's entries.
# Characteristics of view objects:
# Dynamic: Automatically reflect changes to the dictionary
# Iterable: Can be used in loops and comprehensions
# Support membership tests: Can check if elements exist
inventory = {"apples": 5, "oranges": 3, "bananas": 2}

# Create views
keys_view = inventory.keys()
values_view = inventory.values()
items_view = inventory.items()

# Views reflect changes
inventory["grapes"] = 10
print(keys_view)  # dict_keys(['apples', 'oranges', 'bananas', 'grapes'])
print(values_view)  # dict_values([5, 3, 2, 10])
print(items_view)  # dict_items([('apples', 5), ('oranges', 3), ('bananas', 2), ('grapes', 10)])

# Membership tests
print("apples" in keys_view)  # True
print(2 in values_view)  # True
print(("oranges", 3) in items_view)  # True

# Set-like operations (keys view only)
other_keys = {"apples", "pears", "kiwis"}
print(keys_view & other_keys)  # {'apples'} (intersection)
print(keys_view | other_keys)  # {'apples', 'oranges', 'bananas', 'grapes', 'pears', 'kiwis'} (union)

# Here are 10 real-world examples of Python dictionaries in action, with practical code examples for each scenario:

# 1. User Profiles (Social Media)
user = {
    "id": "u123",
    "username": "python_lover",
    "email": "user@example.com",
    "followers": 542,
    "following": 127,
    "preferences": {"theme": "dark", "notifications": True}
}

# Update profile
user["followers"] += 1
user["preferences"]["theme"] = "light"

print(f"{user['username']} now has {user['followers']} followers")
# python_lover now has 543 followers

# 2. Product Catalog (E-commerce)
products = {
    "1001": {
        "name": "Wireless Mouse",
        "price": 24.99,
        "stock": 45,
        "tags": ["electronics", "accessories"]
    },
    "1002": {
        "name": "Mechanical Keyboard",
        "price": 89.99,
        "stock": 12,
        "tags": ["electronics", "premium"]
    }
}

# Check stock
product_id = "1002"
if products[product_id]["stock"] > 0:
    print(f"{products[product_id]['name']} available for ${products[product_id]['price']}")

# 3. Configuration Settings (App Development)
app_config = {
    "debug_mode": False,
    "max_connections": 10,
    "allowed_origins": ["https://example.com", "localhost"],
    "db_config": {
        "host": "db.example.com",
        "port": 5432,
        "username": "admin"
    }
}

# Runtime modification
app_config["debug_mode"] = True
app_config["db_config"]["timeout"] = 30  # Add new setting

print(f"Database timeout set to {app_config['db_config']['timeout']} seconds")


#4. Language Translation System
translations = {
    "en": {
        "greeting": "Hello",
        "farewell": "Goodbye"
    },
    "es": {
        "greeting": "Hola",
        "farewell": "Adiós"
    },
    "fr": {
        "greeting": "Bonjour",
        "farewell": "Au revoir"
    }
}

def translate(lang, phrase):
    return translations.get(lang, {}).get(phrase, phrase)

print(translate("es", "greeting"))  # Hola
print(translate("fr", "farewell"))  # Au revoir

#5. Student Gradebook (Education)
gradebook = {
    "Alice": {"Math": 92, "Science": 88, "History": 95},
    "Bob": {"Math": 78, "Science": 91, "History": 84},
    "Charlie": {"Math": 85, "Science": 90, "History": 89}
}

# Add new student
gradebook["Diana"] = {"Math": 95, "Science": 93, "History": 91}

# Calculate average for a student
alice_grades = gradebook["Alice"].values()
average = sum(alice_grades) / len(alice_grades)
print(f"Alice's average: {average:.1f}")  # Alice's average: 91.7

# 6. API Response Handling (Web Development)
api_response = {
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ],
        "pagination": {
            "total": 2,
            "page": 1,
            "per_page": 20
        }
    },
    "timestamp": "2023-07-20T12:34:56Z"
}

# Extract user emails
emails = [user["email"] for user in api_response["data"]["users"]]
print(f"Fetched emails: {emails}")
# Fetched emails: ['alice@example.com', 'bob@example.com']

# 7. Hospital Patient Records (Healthcare)
patients = {
    "P1001": {
        "name": "John Doe",
        "age": 45,
        "conditions": ["hypertension", "diabetes"],
        "medications": {
            "morning": ["Lisinopril", "Metformin"],
            "evening": ["Metformin"]
        }
    },
    "P1002": {
        "name": "Jane Smith",
        "age": 32,
        "conditions": ["asthma"],
        "medications": {
            "as_needed": ["Albuterol"]
        }
    }
}

# Add new medication
patients["P1001"]["medications"]["afternoon"] = ["Aspirin"]

# Check for drug interactions
if "Aspirin" in patients["P1001"]["medications"].get("afternoon", []):
    print("Warning: Check for aspirin interactions")

# 8. Geolocation Data (Mapping Apps)
cities = {
    "New York": {
        "coordinates": (40.7128, -74.0060),
        "population": 8_804_190,
        "landmarks": ["Statue of Liberty", "Central Park"]
    },
    "London": {
        "coordinates": (51.5074, -0.1278),
        "population": 8_982_000,
        "landmarks": ["Big Ben", "London Eye"]
    }
}

# Find cities with population > 8.5 million
large_cities = [city for city, data in cities.items() if data["population"] > 8_500_000]
print(f"Major cities: {large_cities}")  # Major cities: ['New York', 'London']
