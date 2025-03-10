# Run the code and observe the output
# Task 1 - Change the side of the button from LEFT to RIGHT in line 55, run, and observe the difference 

from customtkinter import *  

BUTTON_COLOR = "#21201F"  
HOVER_COLOR = "#4D4A48"  
BUTTON_SIZE = 80          

# Button layout - Each row is a list of button labels
button_layout = [
    ['+/-', 'C', 'Backspace'],  
    ['7', '8', '9', 'X'],       
    ['4', '5', '6', '-'],      
    ['1', '2', '3', '+'],       
    ['0', '.', '=', '/' ]        
]

# Dictionary to set a custom width for the 'Backspace' button
special_widths = {'Backspace': 160}  

# Creating the main application window
root = CTk() 
root.geometry("320x450")  
root.resizable(False, False)  
root.title('Calculator')  
set_appearance_mode("Dark")  

# Creating a label to display the result (top of the calculator)
result = CTkLabel(root, text="0", width=400, bg_color="grey", 
                 anchor="e", font=("arial", 60, "bold"))  
result.pack()  

# Outer loop - Iterates through each row of buttons in button_layout
for row_buttons in button_layout:
    frame = CTkFrame(root)  # Create a frame to hold the buttons in this row
    frame.pack()  # Add the frame to the window

    # Inner loop - Iterates through each button in the current row
    for button_text in row_buttons:
        # Check if the button has a special width (like 'Backspace'), otherwise use default size
        width = special_widths.get(button_text, BUTTON_SIZE)  

        # Creating a button with the specified properties
        button = CTkButton(
            frame,  # Assign button to the current frame (row)
            text=button_text,  # Display the button's label (text)
            height=BUTTON_SIZE,  # Set button height
            width=width,  # Set button width (custom or default)
            border_width=1,  # Set border width for better appearance
            hover_color=HOVER_COLOR,  # Change color when hovered over
            fg_color=BUTTON_COLOR,  # Set button background color
            font=("arial", 30) #if button_text == '.' else None  # Make '.' button text larger for visibility
        )
        button.pack(side=LEFT)  # Place the button inside the frame (aligned to the left)

# Start the main event loop (displays the window)
root.mainloop()
