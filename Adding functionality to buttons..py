#Run the code to observe the output.
#Task 1- Uncomment the code in line 45 to perform calculation
#Task 2- List out all non fuctional buttons and understand why?
#Task 3- Find out the reason why result is not displaying : Hint - See in line 34.

from customtkinter import *  # Importing CustomTkinter for modern UI components

def create_calculator():
    # Constants for appearance
    BUTTON_COLOR = "#21201F"  # Button background color
    HOVER_COLOR = "#4D4A48"   # Button hover color
    BUTTON_SIZE = 80          # Default button size (width & height)

    # Button configurations (layout of the calculator)
    button_layout = [
        ['+/-', 'C', 'Backspace'],  # Special buttons row
        ['7', '8', '9', 'X'],       # Numbers & multiplication
        ['4', '5', '6', '-'],       # Numbers & subtraction
        ['1', '2', '3', '+'],       # Numbers & addition
        ['0', '.', '=', '/']        # Zero, decimal, equals, and division
    ]

    # Define custom button widths (some buttons like 'Backspace' need to be wider)
    special_widths = {'Backspace': 160}

    def button_click(value):
        """Handles button click events by updating the result display."""
        current = result.cget("text")  # Get current text from result label
        result.configure(text=value if current == "0" else current + value)  # Append new value to display

    def calculate():
        """Performs the calculation based on the expression in the result display."""
        try:
            #current = result.cget("text")  # Get current text from result label
            current = current.replace('X', '*')  # Replace 'X' with '*' for evaluation
            result.configure(text=f"{eval(current):.3f}")  # Evaluate the expression and format the result
        except Exception:
            result.configure(text="Error")  # Display error if evaluation fails

    # Button actions mapping (to be implemented later)
    button_actions = {
        #'+/-': button_opposite,
        #'C': clear,
        #'Backspace': backspace,
        #'=': calculate,
        #'X': lambda: button_click('*'),
    }

    # Setup window
    root = CTk()  # Create the main application window
    root.geometry("320x450")  # Set window size
    root.resizable(False, False)  # Disable window resizing
    root.title('Calculator')  # Set window title
    set_appearance_mode("Dark")  # Set dark theme for better UI

    # Create result display label
    result = CTkLabel(root, text="0", width=400, bg_color="grey",
                     anchor="e", font=("arial", 60, "bold"))  # Right-aligned result display
    result.pack()  # Place result label at the top

    # Create frames and buttons dynamically
    for row_buttons in button_layout:  # Loop through each row in button layout
        frame = CTkFrame(root)  # Create a frame to hold buttons in the row
        frame.pack()  # Pack the frame in the main window

        for button_text in row_buttons:  # Loop through buttons in the row
            width = special_widths.get(button_text, BUTTON_SIZE)  # Get custom width or default size
            button = CTkButton(
                frame,
                text=button_text,  # Set button text
                height=BUTTON_SIZE,  # Set button height
                width=width,  # Set button width
                border_width=1,  # Button border width
                hover_color=HOVER_COLOR,  # Button hover color
                fg_color=BUTTON_COLOR,  # Button background color
                font=("arial", 30) if button_text == '.' else None  # Apply custom font for decimal button
            )

            # Configure button command
            if button_text in button_actions:  # If button has an action, set its command
                button.configure(command=button_actions[button_text])
            elif button_text.isdigit() or button_text in '+-.*/':  # If button is a digit or operator
                button.configure(command=lambda t=button_text: button_click(t))  # Assign button click function

            button.pack(side=LEFT)  # Align buttons from left to right in the frame

    return root  # Return the created UI window

# Run the calculator application
if __name__ == "__main__":
    calculator = create_calculator()  # Create the calculator window
    calculator.mainloop()  # Start the application loop to keep it running
