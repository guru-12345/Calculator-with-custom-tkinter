#Run the code, test all the operators, and identify which one is not working.
#Task 1- Add the below code in line 86 to enable the +/- operator.
# '+/-' : button_opposite 
#Task 2- In line 72 modify the code current[0] with current.startswith, now run and observe the output.
#Task 3- In line 73 modify the code  current[1:] with current[2:], now run and observe the output.

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

def clear():
    result.configure(text="0")
 
 
# Define a function called backspace that removes the last character from the current display
def backspace():
    current = result.cget("text")  
    if len(current) > 1:  # If there is more than one character in the text
        result.configure(text=current[:-1])  # Remove the last character
    else:  
        result.configure(text="0")  # If only one character is left, set it to "0"
        

def calculate():
    try:
        current = result.cget("text")  # Get the current text displayed on the calculator screen
        
        current = current.replace('X', '*')  # Replace 'X' with '*' to allow correct multiplication
        
        eval_result = eval(current)  # Evaluate the mathematical expression entered by the user
        
        # Check if the result is a whole number
        if eval_result % 1 == 0:  
            result_text = str(int(eval_result))  # Convert to an integer to remove unnecessary decimals
        else:
            result_text = f"{eval_result:.3f}"  # Keep three decimal places for non-whole numbers

        result.configure(text=result_text)  # Update the display with the formatted result
    except Exception:  # Handle any errors, such as invalid input
        result.configure(text="Error")  # Show "Error" on the calculator display if evaluation fails


def button_opposite():
        current = result.cget("text")
        
        if current[0] == "-":  # Check if the number is already negative
            result_text = current[1:]  # Remove the negative sign to make it positive
        else:
            result_text = "-" + current  # Add a negative sign to make it negative

        result.configure(text=result_text)  # Update the display with the new value
        



# Create a dictionary that links the button text to the respective functions
button_actions = {
    'Backspace': backspace,
    'C': clear,
    '=' :calculate,
    'X' : lambda: button_click('*'),
    '+/-' : button_opposite
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
