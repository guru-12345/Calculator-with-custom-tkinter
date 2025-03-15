#Run and Observe the output.
#Task1- Uncomment line 42 and observe the output again

from customtkinter import *

root = CTk()
root.geometry("320x450")
root.resizable(True, True)
root.title('Calculator')
set_appearance_mode("Dark")


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

special_widths = {'Backspace': 160} #Set custom width for specific buttons (e.g., 'Backspace' = 160px)


for row_buttons in button_layout:
    frame = CTkFrame(root)  
    frame.pack()
    
    for button_text in row_buttons:
        width = special_widths.get(button_text,button_size ) # Use custom width if set, else default size  
        button = CTkButton(
            frame,   
            text=button_text,
            width=width,
            height=button_size,
            border_width=1,
            hover_color=hover_color,
            fg_color=button_color,
            font=("arial", 30)
        )
        button.pack(side="left")  

root.mainloop()
