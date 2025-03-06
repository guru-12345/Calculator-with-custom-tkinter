#Run the code and observe the output by clicking Backspace
#Create a function named clear that resets the result label text to 0 in line 28.
#Add the clear function to the button dictionary and link it to the "C" button in line 41


from customtkinter import *  

def create_calculator():
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
        current = result.cget("text") # 
        result.configure(text=value if current == "0" else current + value)



    # Define a function called backspace that removes the last character from the current display
    def backspace():
        current = result.cget("text")  # Get the current text on the screen (result)
        # If the current text is longer than 1 character, remove the last character. 
        # Otherwise, set the display text to "0" (the default starting value)
        result.configure(text=current[:-1] if len(current) > 1 else "0")


    # Create a dictionary that links the button text to the backspace function
    button_actions = {
        'Backspace': backspace,
        
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
    
    return root
    

calculator = create_calculator()
calculator.mainloop()
