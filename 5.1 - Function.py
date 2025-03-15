#Run and observe the output
#Task 1: Modify the message function to take two parameters (name and age) and print a message.
#Example Output: "Hello Alice, you are 12 years old!"

def greet():
    print("Hello, welcome to Python!")

# Call the function to run it
greet()  # This will print: Hello, welcome to Python!


# Function with a parameter
def message(name):     #Hint: Add age as a second parameter and use it inside print().
    print("Hello", name, "welcome to Python!")

# Call the function with different names
message("Alice")  
message("Bob")
