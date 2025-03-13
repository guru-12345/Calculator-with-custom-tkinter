#Run the code and observe the output
#Task 1: Align all the buttons horizontally using side="LEFT" in button.pack().
#Task 2: Create a new button called button3 and set its text to "3".

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
button_color = "black"
hover_color = "orange"
button_size = 80
button_width = 100  # Set fixed width for the buttons

# Create buttons and pack them horizontally
button1 = CTkButton(root,
                text="1",
                width=button_width,  # Fixed width
                height=button_size,
                border_width=1,
                hover_color=hover_color,
                fg_color=button_color,
                font=("arial", 20) 
            )
button1.pack()  # Add the side inside the paranthesis

button2 = CTkButton(root,
                text="2",
                width=button_width,  # Fixed width
                height=button_size,
                border_width=1,
                hover_color=hover_color,
                fg_color=button_color,
                font=("arial", 20) 
            )
button2.pack()  # Add padding between buttons

# Add the code for button3 here



root.mainloop()
