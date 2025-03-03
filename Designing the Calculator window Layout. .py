#Run the code to observe the output.
#Task 1: Find out why some buttons are missing and fix the code to show all buttons.
#Task 2: Remove the # from lines 35 & 36 to make the label appear.


from customtkinter import *  # Importing CustomTkinter library for modern UI design

def create_calculator():
    # Constants for appearance
    BUTTON_COLOR = "#21201F"  # Button background color
    HOVER_COLOR = "#4D4A48"   # Button hover color
    BUTTON_SIZE = 80          # Default button size (width & height)

    # Button configurations (layout of the calculator)
    button_layout = [
        #['+/-', 'C', 'Backspace'],  # First row: Special buttons
        #['7', '8', '9', 'X'],       # Second row: Numbers & multiplication
        ['4', '5', '6', '-'],       # Third row: Numbers & subtraction
        ['1', '2', '3', '+'],       # Fourth row: Numbers & addition
        ['0', '.', '/', '=']        # Fifth row: Zero, decimal, division, and equal
    ]

    # Define custom button widths (since some buttons like 'Backspace' need to be wider)
    special_widths = {'Backspace': 160}  # Custom width for Backspace button

    # Setup window
    root = CTk()  # Create the main application window
    root.geometry("320x450")  # Set window size (width x height)
    root.resizable(False, False)  # Disable resizing of the window
    root.title('Calculator')  # Set window title
    set_appearance_mode("Dark")  # Set dark theme for better UI

    # Create result display label
    #result = CTkLabel(root, text="0", width=400, bg_color="grey", anchor="e", font=("arial", 60, "bold"))  # Right-aligned result display
    #result.pack()  # Display result label at the top

    # Create frames and buttons dynamically
    for row_buttons in button_layout:  # Loop through each row in button layout
        frame = CTkFrame(root)  # Create a frame to hold the buttons in each row
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
            button.pack(side='left')  # Align buttons from left to right in the frame

    return root  # Return the created UI window

# Run the calculator application
if __name__ == "__main__":
    calculator = create_calculator()  # Create the calculator window
    calculator.mainloop()  # Start the application loop to keep it running
