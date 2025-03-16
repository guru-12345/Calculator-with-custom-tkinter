#Run the code and observe the output by clicking Backspace
#Task 1- Create a function named clear that resets the result label text to "0" in line 36.
#Add the clear function to the button_actions dictionary and link it to the "C" button in line 53



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
    current = result.cget("text")
    result.configure(text=value if current == "0" else current + value)
    
 


 
# Define a function called backspace that removes the last character from the current display
def backspace():
    current = result.cget("text")  
    if len(current) > 1:  # If there is more than one character in the text
        result.configure(text=current[:-1])  # Remove the last character
    else:  
        result.configure(text="0")  # If only one character is left, set it to "0"


# Create a dictionary that links the button text to the respective functions
button_actions = {
    'Backspace': backspace,
    
    
}

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
    
        if button_text in button_actions:  
            # If the button's text (like "C" or "Backspace") is found in the button_actions dictionary,
            # assign the corresponding function to the button's command.
            button.configure(command=button_actions[button_text])  

        elif button_text.isdigit() or button_text in '+-.*/':  
            # If the button is a number (0-9) or an operator (+, -, ., *, /),
            # set its command to call button_click() with the button's text as an argument.
            button.configure(command=lambda t=button_text: button_click(t))

                
        button.pack(side=LEFT)

root.mainloop()
