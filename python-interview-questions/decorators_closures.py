"""
Python Interview Questions:
Topics covered:
1. Closures
2. Decorators
3. Shallow Copy vs Deep Copy

Instructions:
- Read the questions in comments
- Try to answer by modifying / completing the code
"""

# =====================================================
# 1️⃣ PYTHON CLOSURES
# =====================================================

# Q1: What is a closure in Python?
# Q2: Why are closures used?
# Q3: How does Python remember the value of 'x' even after
#     the outer function has finished execution?

def outer_function(x):
    # TODO: Explain how 'x' is accessible inside inner_function
    def inner_function(y):
        return x + y
    return inner_function


# Q4: What will be the output of the below code and why?
add_10 = outer_function(10)
print(add_10(5))


# =====================================================
# 2️⃣ DECORATORS (Closures + Higher Order Functions)
# =====================================================

# Q5: What is a decorator in Python?
# Q6: How are decorators related to closures?
# Q7: What is the role of *args and **kwargs in decorators?

def auth(role):
    # TODO: Explain how 'role' is preserved using closure
    def decorator(func):
        def wrapper(*args, **kwargs):
            if role != "admin":
                print("Access denied")
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Q8: What happens if role is not 'admin'?
# Q9: How does @auth("admin") work internally?

@auth("admin")
def delete_user(username):
    print(f"User {username} deleted successfully")

delete_user("john")


# =====================================================
# 3️⃣ SHALLOW COPY vs DEEP COPY
# =====================================================

# Q10: What is a shallow copy?
# Q11: What is a deep copy?
# Q12: What is the difference between copy() and deepcopy()?
# Q13: What happens to nested objects in shallow copy?

import copy

original_list = [[1, 2, 3], [4, 5, 6]]

shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)

# Modify nested element
original_list[0][0] = 999

# Q14: Predict the output before running the code
print("Original:", original_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)


# =====================================================
# 4️⃣ COMBINED CONCEPT QUESTION (ADVANCED)
# =====================================================

# Q15: Can a decorator maintain state without using global variables?
# Q16: How does closure help in achieving this?

def counter_decorator():
    count = 0  # preserved via closure

    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            print(f"Function called {count} times")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@counter_decorator()
def greet(name):
    print(f"Hello {name}")


greet("Alice")
greet("Bob")


# =====================================================
# END OF FILE
# =====================================================

# Interview Tip:
# Be prepared to explain:
# - LEGB scope rule
# - nonlocal keyword
# - Why deepcopy is expensive
# - Real-world use cases of decorators

