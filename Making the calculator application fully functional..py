from customtkinter import *

def create_calculator():
    # Constants for appearance
    BUTTON_COLOR = "#21201F"
    HOVER_COLOR = "#4D4A48"
    BUTTON_SIZE = 80

    # Button configurations (layout)
    button_layout = [
        ['+/-', 'C', 'Backspace'],
        ['7', '8', '9', 'X'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['0', '.', '=', '/']
    ]

    # Button widths (most buttons are square except for backspace and equals) so we can set custom widths for them
    special_widths = {'Backspace': 160,}

    def button_click(value):
        current = result.cget("text")
        result.configure(text=value if current == "0" else current + value)

    def clear():
        result.configure(text="0")

    def backspace():
        current = result.cget("text")
        result.configure(text=current[:-1] if len(current) > 1 else "0")

    def calculate():
        try:
            current = result.cget("text")
            # Replace 'X' with '*' for evaluation
            current = current.replace('X', '*')
            result.configure(text=f"{eval(current):.3f}")
        except Exception:
            result.configure(text="Error")

    def button_opposite():
        current = result.cget("text")
        result.configure(text=current[1:] if current[0] == "-" else "-" + current)

    # Button actions mapping
    button_actions = {
        '+/-': button_opposite,
        'C': clear,
        'Backspace': backspace,
        '=': calculate,
        'X': lambda: button_click('*'),
    }

    # Setup window
    root = CTk()
    root.geometry("320x450")
    root.resizable(False, False)
    root.title('Calculator')
    set_appearance_mode("Dark")

    # Create result display
    result = CTkLabel(root, text="0", width=400, bg_color="grey",
                     anchor="e", font=("arial", 60, "bold"))
    result.pack()

    # Create frames and buttons
    for row_buttons in button_layout:
        frame = CTkFrame(root)
        frame.pack()

        for button_text in row_buttons:
            width = special_widths.get(button_text, BUTTON_SIZE)
            button = CTkButton(
                frame,
                text=button_text,
                height=BUTTON_SIZE,
                width=width,
                border_width=1,
                hover_color=HOVER_COLOR,
                fg_color=BUTTON_COLOR,
                font=("arial", 30) if button_text == '.' else None
            )

            # Configure button command
            if button_text in button_actions:
                button.configure(command=button_actions[button_text])
            elif button_text.isdigit() or button_text in '+-.*/':
                button.configure(command=lambda t=button_text: button_click(t))

            button.pack(side=LEFT)

    return root

if __name__ == "__main__":
    calculator = create_calculator()
    calculator.mainloop()
