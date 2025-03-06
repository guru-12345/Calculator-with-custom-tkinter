#Run the code and observe the output by clicking on each button
#Line 27 :Define a function to handle button clicks and update the result display
#Line 28 :Get the current text (value) from the result label
#Line 29 :If the current text is "0", replace it with the clicked value,otherwise append the clicked value to the current text
#Line 60 :Set the command for each button to trigger the button_click function when the button is clicked
#Line 60 :The lambda function ensures that the button's text (button_text) is passed as the 'value' to the button_click function


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
        current = result.cget("text")
        result.configure(text=value if current == "0" else current + value)


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
            button.configure(command=lambda t=button_text: button_click(t))
            button.pack(side=LEFT)
    
    return root
    

calculator = create_calculator()
calculator.mainloop()
