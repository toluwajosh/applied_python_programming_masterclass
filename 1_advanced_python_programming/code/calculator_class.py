"""
A class that defines the display of the calculator
"""
import tkinter


class CalcDisplay(object):

    # initialize calculator instance
    def __init__(self, window):
        self.current_display_text = ""

        # create display frame
        top_frame = tkinter.Frame(
            window
        )  # you can also use "y" as the fill parameter

        # insert textbox in the top frame and a button in bottom frame
        self.display_text_variable = tkinter.StringVar()
        current_display_text = ""
        self.display_text_variable.set(current_display_text)
        display_text = tkinter.Label(
            top_frame,
            font={"arial", 120, "regular"},
            textvariable=self.display_text_variable,
            width=32,
            bg="#eee",
            bd=5,
            anchor="e",
            justify="left",
        )
        display_text.grid(column=0, row=0, sticky="E")
        display_text.pack(fill="x")
        top_frame.pack(fill="x")

    # add a text to the calculator
    def add_text(self, text_to_add):
        self.current_display_text += text_to_add
        self.display_text_variable.set(self.current_display_text)

    # evaluate the expression in the calculator
    def eval(self):

        # dont worry about this part.
        # We want to make sure this part runs
        try:
            eval_text = eval(self.current_display_text)
            self.current_display_text = str(eval_text)
            self.display_text_variable.set(str(self.current_display_text))
            self.current_display_text = ""
        # and if there is an error, we have backup plan. :)
        except Exception as e:
            self.display_text_variable.set("Error!")
            pass

    # clear the calculator display
    def clear(self):
        self.current_display_text = ""
        self.display_text_variable.set(self.current_display_text)
