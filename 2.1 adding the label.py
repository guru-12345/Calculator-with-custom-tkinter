#Run the code to observe the output.
#Task 1- Uncomment line 19 and observe the output.
#Task 2- Make the label as wide as the window width.
#Task 3- Change the text alignment of label to right.


from customtkinter import *  

root = CTk()  
root.geometry("320x450")  
root.resizable(False, False)  
root.title('Calculator')  
set_appearance_mode("light")  

'''The below code creates a result label to display 
the result with "0" as the starting text, grey as background colour, 
bold font, and anchor set to "w" (left-aligned) '''

result = CTkLabel(root, text="0", width=220, bg_color="grey", anchor="w", font=("arial", 60, "bold"))
#result.pack() #pack() arranges widgets inside a window automatically.

# Running the main event loop to keep the window open
root.mainloop()
