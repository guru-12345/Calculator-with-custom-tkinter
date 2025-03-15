#Run the code and observe the output
#Task 1- Find the reason why button are not visible.
#Task 2- Add the items into list as given below
#Line29    ['1', '2', '3', '+'],
#Line30    ['0', '.', '=', '/']

#You will be able to see only label on the window.

from customtkinter import *

root = CTk()
root.geometry("320x450")
root.resizable(False, False)
root.title('Calculator')
set_appearance_mode("Dark")

result = CTkLabel(root, text="0", width=400, bg_color="grey",
                     anchor="e", font=("arial", 60, "bold"))
result.pack()

button_color = "black"
hover_color = "orange"
button_size = 80

button_layout = [
        ['+/-', 'C', 'Backspace'],
        ['7', '8', '9', 'X'],
        ['4', '5', '6', '-'],
        [ ],
        [ ]
    ]

    
root.mainloop()
