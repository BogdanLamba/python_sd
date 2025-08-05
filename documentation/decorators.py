# Decorators in Python are a way to modify or enhance functions or classes
# without directly changing their source code. They use the `@` symbol syntax.
# Let me explain with examples:

# 1. **Basic Function Decorator**:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function")
        func()
        print("Something is happening after the function")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


# When you call say_hello()
say_hello()
# Output:
# Something is happening before the function
# Hello!
# Something is happening after the function

# 2. **Decorators with Arguments**:
def repeat(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator

@repeat(times=3)
def greet():
    print("Hello!")

greet()
# Output:
# Hello!
# Hello!
# Hello!

# 3 **Practical Example - Timing Functions**:
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

@measure_time
def slow_function():
    time.sleep(1)
    return "Done!"

slow_function()
# Output: slow_function took 1.00 seconds

# 4. **Class Method Decorator**:
def require_login(method):
    def wrapper(self, *args, **kwargs):
        if not self.is_logged_in:
            raise Exception("User must be logged in")
        return method(self, *args, **kwargs)

    return wrapper


class User:
    def __init__(self):
        self.is_logged_in = False

    @require_login
    def view_profile(self):
        return "Profile data"


user = User()
# user.view_profile()  # Raises: Exception: User must be logged in

# 5. **Multiple Decorators**:
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def greet():
    return "Hello!"

print(greet())  # Output: <b><i>Hello!</i></b>

# 6.  **Class Decorators**:
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Initializing database connection")

# Only creates one instance
db1 = Database()  # Prints: Initializing database connection
db2 = Database()  # Doesn't print anything
print(db1 is db2)  # True


# 7.  **Built-in Decorators**:
class MyClass:
    def __init__(self, int1):
        self._value = 0

    @property  # Getter
    def value(self):
        return self._value

    @value.setter  # Setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self._value = new_value

    @staticmethod  # Static method
    def utility_method():
        return "I don't need self"

    @classmethod  # Class method
    def from_string(cls, string_value):
        return cls(int(string_value))



# 8. **Decorator with Parameters and Return Value**:
def validate_types(**expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check arguments types
            for arg, expected_type in zip(args, expected_types.values()):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Expected {expected_type}, got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(x=int, y=int)
def add_numbers(x, y):
    return x + y

print(add_numbers(1, 2))  # 3
# add_numbers("1", 2)  # Raises TypeError


# Common Use Cases for Decorators:
#1 - Logging
#2 - Caching/Memoization:
#3 - Access Control

#logging
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def calculate_sum(a, b):
    return a + b

calculate_sum(5, 3)
# Output:
# Calling calculate_sum
# calculate_sum returned 8

# caching
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# access control
def admin_required(func):
    def wrapper(user, *args, **kwargs):
        if not user.is_admin:
            raise PermissionError("Admin access required")
        return func(user, *args, **kwargs)
    return wrapper

class User:
    def __init__(self, is_admin=False):
        self.is_admin = is_admin

    @admin_required
    def delete_user(self, user_id):
        print(f"Deleting user {user_id}")