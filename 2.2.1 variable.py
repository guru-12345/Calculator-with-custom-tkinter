#Run  the code and observe.
#Task 1- Fix the errors in the variables 

from customtkinter import *

# Variable for appearance
#5button_color = "#21201F"
#hover-color = "#4D4A48"
#button size = 80


# Setup window
root = CTk()
root.geometry("320x450")
root.resizable(False, False)
root.title('Calculator')
set_appearance_mode("Dark")

# Create result display
result = CTkLabel(root, text="0", width=400, bg_color="grey",anchor="e", font=("arial", 60, "bold"))
result.pack()
root.mainloop()
