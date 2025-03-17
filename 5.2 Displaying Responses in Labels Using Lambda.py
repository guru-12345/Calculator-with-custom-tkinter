# Run the code and observe the output by clicking on each button

#Add Task 1 on line 43, Task 2 on line 44, and Task 3 on line 45. 
#Task 1- Create a function called 'button_click' with a value parameter.

#Task 2- Get the current text using, 'current = result.cget("text")'.
#(This retrieves the text displayed on the calculator.)

#Task 3- Change the text using, 'result.configure(text=value)'.
#(This updates the display with the new value.)

#Task 4:- Add the code, "button.configure(command=lambda t=button_text: button_click(t))' 
#at line 64 inside the loop to enable button functionality.
#(It ensures each button updates the display with its text when clicked.)


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
        
        button.pack(side=LEFT)

root.mainloop()
