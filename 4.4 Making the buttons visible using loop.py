#Run and Observe the output.
#Task 1: Make the window resizable so you can expand it and see all the buttons.
#Task 2:Increase the border width to 3 and see the difference 

from customtkinter import *

root = CTk()
root.geometry("320x450")
root.resizable(False, False)
root.title('Calculator')
set_appearance_mode("Dark")

# Display result label
result = CTkLabel(root, text="0", width=400, bg_color="grey",
                  anchor="e", font=("arial", 60, "bold"))
result.pack()

button_color = "black"
hover_color = "orange"
button_size = 80

# Button layout (nested list)
button_layout = [
    ['+/-', 'C', 'Backspace'],
    ['7', '8', '9', 'X'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '/']
]

# Create buttons in a single row
for row_buttons in button_layout:
    for button_text in row_buttons:
        button = CTkButton(
            root,                     # The main window where the button will be placed
            text=button_text,         # The text displayed on the button
            height=button_size,       # Sets the height of the button
            border_width=1,           # Defines the border width of the button
            hover_color=hover_color,  # Changes color when the mouse hovers over it
            fg_color=button_color,    # Sets the default background color of the button
            font=("arial", 30)        # Defines the font style and size for the button text
        )
        button.pack(side="left")  # Arrange buttons in a single row

root.mainloop()
