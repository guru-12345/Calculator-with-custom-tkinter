#Run the code and observe the output
#Task 1- Change the side of the button from LEFT to RIGHT in line 54 run and observe the difference 
from customtkinter import *  

def create_calculator():
    
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
    
        #Loop through each button text in the current row of the layout.
        for button_text in row_buttons:
            width = special_widths.get(button_text, BUTTON_SIZE)
            
            #Create a custom button(CTkButton) with the specified properties.
            button = CTkButton(
            frame,  # The frame to which the button belongs (the current row's frame)
            text=button_text,  # Set the text displayed on the button (e.g., '1', '2', 'C')
            height=BUTTON_SIZE,  # Set the height of the button (default size set by BUTTON_SIZE)
            width=width,  # Set the width of the button (either custom width or default size)
            border_width=1,  # Set the width of the button's border (a value of 1 pixel)
            hover_color=HOVER_COLOR,  # Set the color of the button when hovered over
            fg_color=BUTTON_COLOR,  # Set the background color of the button
            font=("arial", 30) if button_text == '.' else None  # Set a custom font size for the '.' button (30px), otherwise use default font
            )
    
            button.pack(side=LEFT)
    
    return root
    
    
calculator = create_calculator()
calculator.mainloop()
