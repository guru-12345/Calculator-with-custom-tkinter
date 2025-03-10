#Run the code and observe the output
#Task 1- Uncomment the line 35 and observe the change in the output.
#Line 33: 'button_layout' is a list of button rows, and 'row_buttons' is each row in that list.
"""The for loop helps arrange buttons in rows so they look organized in the calculator"""

from customtkinter import *  

# Variable for appearance
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

root = CTk()  
root.geometry("320x450") 
root.resizable(False, False)  
root.title('Calculator')  
set_appearance_mode("Dark")  

result = CTkLabel(root, text="0", width=400, bg_color="grey", 
                 anchor="e", font=("arial", 60, "bold"))  # Right-aligned text
result.pack()  

# The loop creates a frame for each row of buttons in button_layout, grouping buttons together.
for row_buttons in button_layout: 
    frame = CTkFrame(root)  # Create a frame for each row
    #frame.pack()


root.mainloop()
