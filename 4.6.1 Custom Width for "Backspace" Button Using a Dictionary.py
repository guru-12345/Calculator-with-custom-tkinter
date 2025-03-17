#Run and Observe the output.
 
'''
#Task 1-Create a dictionary named special_widths at line 40 to store specific button widths.
1-> The dictionary name is special_widths.
2-> The key in the dictionary is "Backspace" (which represents the button text).
3-> The value is 160, which sets the width of the "Backspace" button to 160 pixels.
'''
#Task 2- In line 47, add width = special_widths.get(button_text, button_size) to set a 
#custom width for the "Backspace" button while keeping others buttons as the same.

#Task 3- Add width=width in line 56 to apply custom button widths, ensuring the "Backspace" button appears wider.

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



for row_buttons in button_layout:
    frame = CTkFrame(root)  
    frame.pack()
    
    for button_text in row_buttons:
         
        button = CTkButton(
            frame,   
            text=button_text,
            height=button_size,
            border_width=1,
            hover_color=hover_color,
            fg_color=button_color,
            font=("arial", 30),
            
        )
        button.pack(side="left")  

root.mainloop()
