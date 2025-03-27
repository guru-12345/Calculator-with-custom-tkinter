
# Why Use Try and Except?
# 1. It prevents the program from crashing when an error occurs.
# 2. It allows us to handle errors gracefully.
# 3. We can display user-friendly messages instead of raw error messages.

# Example 1: Basic try and except
# This code tries to divide a number by zero, which normally causes an error.
# Instead of crashing, it will print a message.
try:
    result = 10 / 0  # This will cause an error (division by zero)
except:
    print("Something went wrong!")  # This message will be shown instead of an error

# Task 1:Uncomment & Modify the code to handle an error caused by accessing an invalid list index.
"""
try:
    my_list = [1, 2, 3]
    print(my_list[5])  
except:
   
"""

