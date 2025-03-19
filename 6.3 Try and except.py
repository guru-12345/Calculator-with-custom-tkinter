
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

# Task 1: Modify the code to handle an error caused by accessing an invalid list index.


# Example 2: Try and except without specifying an error type
# This will catch any error that happens in the try block.
try:
    print(undefined_variable)  # This variable is not defined, causing an error
except:
    print("An error occurred!")

# Task 2: Modify the code to handle an error when trying to open a file that does not exist.


# Example 3: Using finally
# The 'finally' block runs no matter what, even if an error occurs.
try:
    print("Trying something...")
    num = 5 / 1  # No error here
except:
    print("Something went wrong!")
finally:
    print("This will always run!")

# Task 3: Modify the code to raise an error inside the try block and see how finally still runs.

# Summary:
# - 'try' lets us test a block of code for errors.
# - 'except' catches and handles the error.
# - 'finally' runs no matter what, useful for cleanup tasks.
