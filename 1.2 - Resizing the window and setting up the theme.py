#Run the code to observe the output.
#Try increasing the height and width of the output window.

#Task 1- Uncomment line 15 to make window size fixed.
#Task 2- Make the width resizable.
#Task 3- Change the appearance mode to "Dark".

from customtkinter import *  

root = CTk()  

root.geometry("320x450")  

#It stops resizing the window's Width & Height.
#root.resizable(False, False)  

root.title('Calculator')  

# Setting the appearance mode to "dark" (changes theme)
set_appearance_mode("light")  

root.mainloop()
