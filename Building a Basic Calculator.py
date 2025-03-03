#Run the code to observe the output.
#Task 1- Change the background color to "Dark"
#Task 2- Change the size of the window to 320x450
#Task 3- Add the tilte of the window to "Calculator"
#Task 4- Remove the comment in the line 19 to make window size fixed.

# Importing all necessary modules from customtkinter
from customtkinter import *

# Function to create and set up the calculator window
def create_calculator():
    # Create the main application window
    root = CTk()

    # Set the window size to 320 pixels wide and 450 pixels tall
    root.geometry("400x450")

    # Prevent the window from being resized to maintain a fixed layout
    #root.resizable(False, False)

    # Set the window title to "Calculator"
    root.title(' ')

    # Set the appearance mode to "Dark" for a dark theme interface
    set_appearance_mode("grey")

    return root  # Return the created window object

# Main execution: Runs the calculator application when the script is executed
if __name__ == "__main__":
    # Call the function to create the calculator window
    calculator = create_calculator()

    # Run the main event loop to keep the application open
    calculator.mainloop()



