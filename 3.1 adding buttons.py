#Run the code and observe the output.
#Task 1- Find the reason why button are not visible. 
#Task 2- Add the items into list as given below   
#Line22    ['1', '2', '3', '+'],       
#Line23    ['0', '.', '=', '/'] 

#You will be able to see only label on the window.

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
        [ ],       
        [ ]        
    ]
    
    # Setup window
    root = CTk()  # Create the main application window
    root.geometry("320x450")  # Set window size (320 pixels wide, 450 pixels high)
    root.resizable(False, False)  # Disable window resizing
    root.title('Calculator')  # Set the window title
    set_appearance_mode("Dark")  # Apply dark mode theme

    # Create result display label (to show user input and results)
    result = CTkLabel(root, text="0", width=400, bg_color="grey", 
                     anchor="e", font=("arial", 60, "bold"))  # Right-aligned text
    result.pack()  # Add result display to the window
    return root

    
# Create and display the calculator window
calculator = create_calculator()
calculator.mainloop()
