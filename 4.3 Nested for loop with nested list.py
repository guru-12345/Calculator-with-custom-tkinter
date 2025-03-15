#Run and observe the codec
#Task 1:Modify the code to add a space after each button when printing, so the output looks clean.

'''
+/-  C  Backspace  
7  8  9  X  
4  5  6  -  
1  2  3  +  
0  .  =  /
'''

# Hint:- 
#Use end=" " to print buttons in the same row, then print() to move to the next line

button_layout = [
        ['+/-', 'C', 'Backspace'],
        ['7', '8', '9', 'X'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['0', '.', '=', '/' ]
    ]
    
for row_buttons in button_layout:
    for button_text in row_buttons:
        print(button_text)
    print()
