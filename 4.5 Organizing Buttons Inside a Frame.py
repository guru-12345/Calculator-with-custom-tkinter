#Run and Observe the output.
#Task 1: Uncomment the line 35 to and observe the output/error.
#Task 2: Add frame.pack() on line 36 to fix the error.
#Task 3: Replace 'root' with 'frame' inside the loop 
#to place buttons inside the frame instead of the main window.

from customtkinter import *

root = CTk()
root.geometry("320x450")
root.resizable(True, False)
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
    #frame = CTkFrame(root) It creates a frame in the main window to group widgets.   
                      
    
    for button_text in row_buttons:
        button = CTkButton(
            root,   # Replace with frame
            text=button_text,
            height=button_size,
            border_width=1,
            hover_color=hover_color,
            fg_color=button_color,
            font=("arial", 30)
        )
        button.pack(side="left")  

root.mainloop()
