"""
Higher Order Functions – Interview Examples

Definition:
A higher order function is a function that:
1. Takes one or more functions as arguments OR
2. Returns a function
"""

# =====================================================
# 1️⃣ Function as an Argument
# =====================================================

# Q1: What is a higher order function?
# Q2: Why is the function below called a higher order function?

def apply_operation(func, a, b):
    return func(a, b)


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


# Interview Question:
# What will be the output?
print(apply_operation(add, 2, 3))
print(apply_operation(multiply, 2, 3))


# =====================================================
# 2️⃣ Function Returning Another Function
# =====================================================

# Q3: How does this function demonstrate a higher order function?
# Q4: Explain how closure works here.

def power(n):
    def inner(x):
        return x ** n
    return inner


square = power(2)
cube = power(3)

# Interview Question:
# What is stored in square and cube?
print(square(4))
print(cube(4))


# =====================================================
# 3️⃣ Using Lambda with Higher Order Functions
# =====================================================

# Q5: Why is map considered a higher order function?

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x * x, numbers))

# Predict the output
print(squared_numbers)


# =====================================================
# 4️⃣ filter() as a Higher Order Function
# =====================================================

# Q6: How does filter work internally?
# Q7: What type does filter return in Python 3?

def is_even(n):
    return n % 2 == 0


evens = list(filter(is_even, numbers))

print(evens)


# =====================================================
# 5️⃣ reduce() – Classic Interview Favorite
# =====================================================

# Q8: Why is reduce considered a higher order function?
# Q9: Where is reduce defined?

from functools import reduce

total = reduce(lambda x, y: x + y, numbers)

print(total)


# =====================================================
# 6️⃣ Higher Order Function with Custom Logic
# =====================================================

# Q10: Write a higher order function that adds logging
#      before executing another function.

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logger
def greet(name):
    return f"Hello {name}"


print(greet("Alice"))


# =====================================================
# 7️⃣ Higher Order Function vs Normal Function
# =====================================================

# Q11: Is this a higher order function? Why or why not?

def normal_function(x, y):
    return x + y

# Answer:
# ❌ Not a higher order function because it does not
#    accept or return another function


# =====================================================
# 8️⃣ Are Nested Functions Higher Order Functions?
# =====================================================

# Q12: Are nested functions always higher order functions?

def outer():
    def inner():
        return "Hello"
    return inner   # ✅ Higher order (returns a function)


# If inner() was NOT returned or passed, it would NOT be HOF


# =====================================================
# 9️⃣ Higher Order Function with Decorator (Advanced)
# =====================================================

# Q13: Explain how decorators are higher order functions

def auth(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if role != "admin":
                print(f"Access denied to delete the user {args[0]}")
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator


@auth("admin")
def delete_user(username):
    print(f"Deleted user {username}")


delete_user("john")

# delete the user without defaulting the decorator role
def delete_user_1(username):
    print(f"Deleted user {username}")

delete_user_1_obj = auth("hr")(delete_user_1)
delete_user_1_obj('krishna')

# advanced decorator by dynamically passing the role
def auth(role_getter):
    def decorator(func):
        def wrapper(*args, **kwargs):
            role = role_getter(*args, **kwargs)
            if role != "admin":
                print(f"Access denied to delete the user {args[0]}")
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator


@auth(lambda username, role=None: role)
def delete_user_2(username, role=None):
    print(f"Deleted user {username}")


delete_user_2("king", role="admin")
delete_user_2("anny", role="hr")


# =====================================================
# 10️⃣ Trick Interview Question
# =====================================================

# Q14: Is a recursive function a higher order function?

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Answer:
# ❌ NO
# A recursive function calls itself but does NOT
# accept or return another function


# =====================================================
# Interview Tips:
# - Decorators are higher order functions
# - map, filter, reduce are classic examples
# - Closures often appear with higher order functions
# - Recursive != Higher Order
# =====================================================
