# Run the code and observe the output.
# Task 1 - Find the reason why buttons are not visible. 
# Task 2 - Add the items into the list as given below   
# Line 22    ['1', '2', '3', '+'],       
# Line 23    ['0', '.', '=', '/'] 

# You will be able to see only the label on the window.

from customtkinter import *  

# Constants for appearance
BUTTON_COLOR = "#21201F"  # Button background color
HOVER_COLOR = "#4D4A48"   # Button hover color
BUTTON_SIZE = 80          # Default button size

# Button configurations (layout of the calculator)
button_layout = [
    ['+/-', 'C', 'Backspace'],  
    ['7', '8', '9', 'X'],       
    ['4', '5', '6', '-'],      
    [ ],       
    [ ]        
]

# Setup window
root = CTk()  # Create the main application window
root.geometry("320x450")  # Set window size (320 pixels wide, 450 pixels high)
root.resizable(False, False)  # Disable window resizing
root.title('Calculator')  # Set the window title
set_appearance_mode("Dark")  # Apply dark mode theme

# Create result display label (to show user input and results)
result = CTkLabel(root, text="0", width=400, bg_color="grey", 
                 anchor="e", font=("arial", 60, "bold"))  # Right-aligned text
result.pack()  # Add result display to the window

# Run the application
root.mainloop()
