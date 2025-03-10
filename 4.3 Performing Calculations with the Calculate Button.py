#Run the code and observe the output by clicking on each button
#Task 1- Find the buttons which are not working and make them functional.
#Task Define opposite button

#Hint:
#Define a button_opposite() function to flip the sign of the current number (positive to negative and vice versa), 
#and link it to the +/- button in the button_actions dictionary. 
#Use result.configure(text=current[1:] if current[0] == "-" else "-" + current) to toggle the sign

from customtkinter import *  

# Constants for appearance
BUTTON_COLOR = "#21201F"  
HOVER_COLOR = "#4D4A48"   
BUTTON_SIZE = 80         

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

def backspace():
    current = result.cget("text")
    result.configure(text=current[:-1] if len(current) > 1 else "0")

def clear():
    result.configure(text="0")

# Define a function to perform the calculation when the '=' button is pressed
def calculate():
    try:
        # Get the current text (equation) from the result display
        current = result.cget("text")
        
        # Replace 'X' with '*' to make it a valid math operator (multiplication)
        current = current.replace('X', '*')
        
        # Evaluate the mathematical expression using Python's eval function
        eval_result = eval(current)
        
        # If the result is an integer, show it as an integer. 
        # If it's a decimal, show it with 3 decimal places
        result.configure(text=str(int(eval_result)) if eval_result == int(eval_result) else f"{eval_result:.3f}")
    except Exception:
        # If there's an error (like invalid math), display "Error" on the screen
        result.configure(text="Error")

button_actions = {
    'Backspace': backspace,
    'C': clear,
    '=': calculate,
    #'X': lambda: button_click('*')
}

root = CTk()  
root.geometry("320x450")  
root.resizable(False, False)  
root.title('Calculator')  
set_appearance_mode("Dark")  

result = CTkLabel(root, text="0", width=400, bg_color="grey", 
                 anchor="e", font=("arial", 60, "bold"))  
result.pack()  

for row_buttons in button_layout:
    frame = CTkFrame(root)
    frame.pack()
    
    for button_text in row_buttons:
        width = special_widths.get(button_text, BUTTON_SIZE)
        button = CTkButton(
            frame,
            text=button_text,
            height=BUTTON_SIZE,
            width=width,
            border_width=1,
            hover_color=HOVER_COLOR,
            fg_color=BUTTON_COLOR,
            font=("arial", 30) if button_text == '.' else None
        )
        if button_text in button_actions:
            button.configure(command=button_actions[button_text])
        elif button_text.isdigit() or button_text in '+-.*/':
            button.configure(command=lambda t=button_text: button_click(t))
        button.pack(side=LEFT)

root.mainloop()
