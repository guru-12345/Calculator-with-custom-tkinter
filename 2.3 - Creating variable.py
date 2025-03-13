# Run the code and observe the output.
#Task 1: Create a variable button_color and set it to "black" on line 22.
#Task 2: Create another variable hover_color and set it to "orange" on line 23.
#Task 3: Create a variable button_size and set it to 80 on line 24.


from customtkinter import * 

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

# Button variables for styling



# Run the application
root.mainloop()
