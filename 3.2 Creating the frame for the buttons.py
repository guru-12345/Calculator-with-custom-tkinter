#Run the code and observe the output
#Task 1- Uncomment the line 34 and observe the change in the output.

from customtkinter import *  # Importing CustomTkinter for modern UI styling

def create_calculator():
    # Constants for appearance
    BUTTON_COLOR = "#21201F"  # Button background color
    HOVER_COLOR = "#4D4A48"   # Button hover color
    BUTTON_SIZE = 80          # Default button size

    # Button configurations (layout of the calculator)
    button_layout = [
        ['+/-', 'C', 'Backspace'],  
        ['7', '8', '9', 'X'],       
        ['4', '5', '6', '-'],      
        ['1', '2', '3', '+'],       
        ['0', '.', '=', '/' ]        
    ] 
    
    root = CTk()  
    root.geometry("320x450") 
    root.resizable(False, False)  
    root.title('Calculator')  
    set_appearance_mode("Dark")  

    result = CTkLabel(root, text="0", width=400, bg_color="grey", 
                     anchor="e", font=("arial", 60, "bold"))  # Right-aligned text
    result.pack()  
    
    #The loop creates a frame for each row of buttons in button_layout, grouping buttons together.
    for row_buttons in button_layout: 
        frame = CTkFrame(root)  #create a frame for each row
        #frame.pack()

    
    return root
    
    
# Create and display the calculator window
calculator = create_calculator()
calculator.mainloop()
