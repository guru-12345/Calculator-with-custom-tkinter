# Why Use Lambda?
# 1. It’s a shortcut for small functions.
# 2. No need to write 'def' and 'return'.
# 3. Useful for quick, one-time calculations.
# 4. In GUI libraries like CustomTkinter, lambda is useful when passing arguments to functions in buttons or events.

# Example 1: Basic lambda function to double a number
# A lambda function is created using the 'lambda' keyword
# It takes one argument (x) and returns x multiplied by 2
double = lambda x: x * 2  # Lambda function to double a number
print(double(4))  # Output: 8

# Equivalent regular function
# This function does the same thing as the lambda function above, but with more code
def double(x):
    return x * 2
print(double(4))  # Output: 8

# Task 1: Modify the lambda function to triple the number instead of doubling it. 
# Then, print the result for 5.


# Example 2: Using lambda in CustomTkinter (hypothetical example)
# Suppose we have a button that needs to call a function with an argument
# Normally, if we use command=greet("Alice"), it will run immediately instead of waiting for a click
# Using lambda helps us call the function only when the button is clicked
import customtkinter as ctk

def greet(name):
    print("Hello,", name)  # This function prints a greeting message

root = ctk.CTk()
button = ctk.CTkButton(root, text="Click Me", command=lambda: greet("Alice"))  # Lambda delays execution
button.pack()
root.mainloop()

# Task 2: Modify the code to print a different name when the button is clicked.

# Summary:
# - Lambda functions are used for short, simple tasks.
# - They help in GUI applications where we need to pass arguments to a function.
# - They make the code shorter and cleaner when defining small functions.
