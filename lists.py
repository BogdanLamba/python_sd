# Python List Methods: A Deep Dive with Examples

# Creating Lists
# Empty list
empty_list = []
empty_list = list()

# List with initial values
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

# Using list() constructor
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# Access Methods
# 1. Indexing - Access elements by position
print(fruits[0])  # "apple" (first element)
print(fruits[-1])  # "cherry" (last element)

# 2. Slicing - Get sublists
print(numbers[1:3])  # [2, 3]
print(numbers[:3])  # [1, 2, 3]
print(numbers[2:])  # [3, 4, 5]
print(numbers[::2])  # [1, 3, 5] (every 2nd element)

# 3. index() - Find position of element
print(fruits.index("banana"))  # 1
# Raises ValueError if not found

# 4. count() - Count occurrences
nums = [1, 2, 3, 2, 4, 2]
print(nums.count(2))  # 3

# Modification Methods

# 1. append() - Add to end
fruits.append("date")
print(fruits)  # ['apple', 'banana', 'cherry', 'date']

# 2. insert() - Add at specific position
fruits.insert(1, "avocado")
print(fruits)  # ['apple', 'avocado', 'banana', 'cherry', 'date']

# 3. extend() - Add multiple items
fruits.extend(["elderberry", "fig"])
print(fruits)
# ['apple', 'avocado', 'banana', 'cherry', 'date', 'elderberry', 'fig']

# 4. remove() - Delete by value
fruits.remove("banana")
print(fruits)
# ['apple', 'avocado', 'cherry', 'date', 'elderberry', 'fig']

# 5. pop() - Remove by index (returns removed item)
removed = fruits.pop(2)  # Remove and return 'cherry'
print(removed)  # "cherry"
print(fruits)  # ['apple', 'avocado', 'date', 'elderberry', 'fig']

# 6. clear() - Empty the list
fruits.clear()
print(fruits)  # []

# Ordering Methods
# 1. sort() - In-place sorting
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# With parameters
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# 2. reverse() - Reverse in-place
nums = [1, 2, 3]
nums.reverse()
print(nums)  # [3, 2, 1]

# 3. sorted() - Return new sorted list
original = [3, 1, 2]
new_list = sorted(original)
print(original)  # [3, 1, 2] (unchanged)
print(new_list)  # [1, 2, 3]

# List Operations
# 1. Concatenation
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4]

# 2. Repetition
repeated = [0] * 5
print(repeated)  # [0, 0, 0, 0, 0]

# 3. Membership Testing
print(2 in [1, 2, 3])  # True
print(5 in [1, 2, 3])  # False

# List Comprehensions
# Create new list by transforming elements
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Copying Lists
# 1. Shallow Copy
original = [1, [2, 3]]
copied = original.copy()  # or copied = original[:]

# Modifying top level doesn't affect original
copied[0] = 5
print(original)  # [1, [2, 3]]

# But nested objects are shared!
copied[1][0] = 99
print(original)  # [1, [99, 3]]

# 2. Deep Copy
from copy import deepcopy

original = [1, [2, 3]]
deep_copied = deepcopy(original)

# Now nested objects are independent
deep_copied[1][0] = 99
print(original)  # [1, [2, 3]] (unchanged)

# List Views (Python 3)
# While lists don't have view objects like dictionaries, you can create similar functionality:

# 1. Memoryview (for homogeneous data)
arr = bytearray(b'abcdef')
mv = memoryview(arr)
print(mv[2:4].tobytes())  # b'cd'

# Modifying through view affects original
mv[3] = 122  # 'z'
print(arr)  # bytearray(b'abczef')

# 2. Slices as Views
numbers = [1, 2, 3, 4, 5]
view = numbers[1:4]  # Not a true view - creates new list
numbers[2] = 99
print(view)  # [2, 3, 4] (doesn't update)

# Performance Considerations
# Appending (append()) is O(1) time complexity
# Inserting (insert()) is O(n) - slower for large lists
# Searching (in operator) is O(n) - consider sets for faster lookups
# Slicing creates a new copy - O(k) where k is slice size

# Common Patterns

# 1. Iterating with Index
for index, value in enumerate(fruits):
    print(f"{index}: {value}")

# 2. Zipping Lists
names = ["Alice", "Bob"]
scores = [95, 87]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
'''
Alice: 95
Bob: 87
'''

# 3. Flattening Lists

nested = [[1, 2], [3, 4]]
flat = [item for sublist in nested for item in sublist]
print(flat)  # [1, 2, 3, 4]

# Here are 10 real-world examples of how Python lists are used in practical applications, with code examples for each:

# 1. Shopping Cart (E-commerce)
cart = []
cart.append({"item": "Laptop", "price": 999.99, "quantity": 1})
cart.append({"item": "Mouse", "price": 19.99, "quantity": 2})

# Calculate total
total = sum(item["price"] * item["quantity"] for item in cart)
print(f"Total: ${total:.2f}")  # Total: $1039.97

# 2. To-Do List App
todos = ["Buy groceries", "Pay bills", "Call mom"]

# Add new task
todos.append("Schedule meeting")

# Complete first task
completed = todos.pop(0)
print(f"Completed: {completed}")  # Completed: Buy groceries
print(f"Remaining: {todos}")  # Remaining: ['Pay bills', 'Call mom', 'Schedule meeting']

# 3. Temperature Monitoring (IoT)
daily_temps = [22.5, 23.1, 24.8, 25.3, 24.9]

# Analyze data
max_temp = max(daily_temps)
min_temp = min(daily_temps)
avg_temp = sum(daily_temps) / len(daily_temps)

print(f"Max: {max_temp}°C, Min: {min_temp}°C, Avg: {avg_temp:.1f}°C")
# Max: 25.3°C, Min: 22.5°C, Avg: 24.1°C

# 4. Social Media Posts
posts = [
    {"user": "alice", "content": "Enjoying Python!", "likes": 42},
    {"user": "bob", "content": "My new project", "likes": 87}
]

# Sort by popularity
top_posts = sorted(posts, key=lambda x: x["likes"], reverse=True)
print(f"Top post: '{top_posts[0]['content']}' by {top_posts[0]['user']}")
# Top post: 'My new project' by bob

# 5. Game Leaderboard
scores = [("Alice", 4500), ("Bob", 3200), ("Charlie", 6700)]

# Update score
scores.append(("Diana", 5100))

# Top 3 players
top_players = sorted(scores, key=lambda x: x[1], reverse=True)[:3]
print("Leaderboard:")
for i, (name, score) in enumerate(top_players, 1):
    print(f"{i}. {name}: {score} pts")

# 6. Inventory Management
inventory = ["Laptop", "Monitor", "Keyboard", "Mouse"]

# Process shipment
new_items = ["Headphones", "Webcam", "Mouse"]  # Note duplicate "Mouse"
inventory.extend(new_items)

# Remove duplicates
unique_items = list(set(inventory))
print(f"Inventory: {unique_items}")
# Inventory: ['Webcam', 'Laptop', 'Headphones', 'Keyboard', 'Monitor', 'Mouse']

# 7. Survey Data Analysis
responses = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

# Calculate frequencies
from collections import Counter

rating_counts = Counter(responses)
print("Survey Results:")
for rating, count in sorted(rating_counts.items()):
    print(f"{count} people rated {rating}/5")

# 8. File Processing (CSV Data)
# Simulating CSV data
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", "28", "New York"],
    ["Bob", "32", "Chicago"]
]

# Extract column
names = [row[0] for row in csv_data[1:]]  # Skip header
print(f"Names in dataset: {names}")  # Names in dataset: ['Alice', 'Bob']

# 9. Music Playlist
playlist = [
    {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 354},
    {"title": "Imagine", "artist": "John Lennon", "duration": 183}
]

# Add new song
playlist.insert(1, {"title": "Yesterday", "artist": "The Beatles", "duration": 125})

# Calculate total duration
total_seconds = sum(song["duration"] for song in playlist)
print(f"Playlist duration: {total_seconds // 60}m {total_seconds % 60}s")
# Playlist duration: 11m 2s

# 10. Scientific Data Processing
# Simulating sensor readings
readings = [23.7, 24.1, 23.9, 24.2, 24.5, 24.3, 24.0]

# Remove outliers (outside 2 standard deviations)
import statistics

mean = statistics.mean(readings)
stdev = statistics.stdev(readings)
clean_data = [x for x in readings if mean - 2 * stdev <= x <= mean + 2 * stdev]

print(f"Original: {readings}")
print(f"Cleaned: {clean_data}")

# Key Takeaways:

# Dynamic Collections: Lists are perfect for storing ordered, changeable data.
# Mixed Data Types: Can hold numbers, strings, dictionaries, even other lists.
# Built-in Methods: Methods like append(), sort(), and extend() make manipulation easy.
# Real-world Flexibility: Used in web apps, data science, gaming, IoT, and more.
# Each example demonstrates how lists handle ordered data that changes over time -
# their core strength in Python programming.
