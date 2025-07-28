# Run the code and observe the output by clicking on each button
#Task 1:- Update the button_click function to Replace "0" with the First Clicked Number & Append Others.
'''Hint:- 
    if current == "0":
        result.configure(text=value)
    else:
        result.configure(text=current + value)'''

from customtkinter import *  

root = CTk()  
root.geometry("320x450")  
root.resizable(False, False)  
root.title('Calculator')  
set_appearance_mode("Dark")  

result = CTkLabel(root, text="0", width=400, bg_color="grey", 
                 anchor="e", font=("arial", 60, "bold"))  
result.pack()  

button_color = "black"
hover_color = "orange"
button_size = 80       

button_layout = [
    ['+/-', 'C', 'Backspace'],  
    ['7', '8', '9', 'X'],       
    ['4', '5', '6', '-'],      
    ['1', '2', '3', '+'],       
    ['0', '.', '=', '/' ]        
]

special_widths = {'Backspace': 160}  

def button_click(value):
    current = result.cget("text")  # Get current text from display
    
    result.configure(text=current + value)  # Directly appends new number

 

for row_buttons in button_layout:
    frame = CTkFrame(root)
    frame.pack()
    
    for button_text in row_buttons:
        width = special_widths.get(button_text, button_size)
        button = CTkButton(
            frame,
            text=button_text,
            height=button_size,
            width=width,
            border_width=1,
            hover_color=hover_color,
            fg_color=button_color,
            font=("arial", 20)
        )
        button.configure(command=lambda t=button_text: button_click(t))
        button.pack(side=LEFT)

root.mainloop()
