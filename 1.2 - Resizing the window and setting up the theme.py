#Run the code to observe the output.
#Task 1- Change the background color to "Dark"
#Task 2- Remove the comment in the line 15 to make window size fixed.

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

# Running the main event loop to keep the window open
root.mainloop()
