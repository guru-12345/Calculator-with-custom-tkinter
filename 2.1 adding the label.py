#Run the code to observe the output.
#Task 1- uncomment the line 26 and observe output.
#Task 1- Make the label as wide as the window width.
#Task 2- Change the text alignment of label to right.

# Importing all necessary modules from customtkinter
from customtkinter import *  

# Creating the main application window (root)
root = CTk()  

# Setting the size of the window (Width x Height)
root.geometry("320x450")  

# Disabling the option to resize the window (Fixes size)
#root.resizable(False, False)  

# Setting the title of the window
root.title('Calculator')  

# Setting the appearance mode to "dark" (changes theme)
set_appearance_mode("light")  

# Create result display
result = CTkLabel(root, text="0", width=220, bg_color="grey", anchor="w", font=("arial", 60, "bold"))
#result.pack()

# Running the main event loop to keep the window open
root.mainloop()
