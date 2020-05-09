# Code Organization in Python Projects

The more function we add in our program the more lines of code we get. Therefore it becomes cumbersome to edit or manage several lines of code in a single file. Being able to use codes from other locations make our program less clumpsy and more manageable. Furthermore, we can work on only the parts that are important to use and leave the rest untouched. This is the same way packages are used in programming languages. For example;

```python
import numpy # here we are getting already available codes packaged as `numpy`
```

It is also possible to use files in the same directory. If we have a script like the one below, and we save the file as `print_my_name.py`.

```python
# script to print my name
print("My name is Joshua")
```

I can call this script in another file of the same directory;

```python
import print_my_name

print("I live in Tokyo")
```

If we run the new file we will get the output from both the imported file and the new file;

```bash
My name is Joshua
I live in Tokyo
```

Ideally, we want to instead make use of functions from another file like so.

```python
# print_info.py

# function to print name
def print_name():
    print("My name is Joshua")
```

And in our new file;

```python
# use the function in another file
from print_info import print_name

# now call print_name to use it
print_name()
print("I live in Tokyo")
```

This second approach is the way to use functions (and classes) from another file.

To demonstrate this approach we are going to `refactor` our previous code of the python calculator to hide the `CalcDisplay` class in another file. This way we can focus on the calculator design in a separate file.

> **Code Refactoring** is the process of restructuring existing computer code—changing the factoring—without changing its external behavior. Refactoring is intended to improve the design, structure, and/or implementation of the software (its non-functional attributes), while preserving the functionality of the software.

Save the following code in a file called `calculator_class.py`. Notice how the `CalcDisplay` class is defined and how it is used differently in the main file compared to before.

```python
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
        # and if there is an error, we have backup plan. :)
        except Exception as e:
            self.display_text_variable.set("Error!")
            pass

    # clear the calculator display
    def clear(self):
        self.current_display_text = ""
        self.display_text_variable.set(self.current_display_text)

```

We can now use this class in our main file like shown below. Note that both files have to be in the same directory.

```python
"""
Using the ktinker module of python to write a calculator program
"""
import tkinter

# user defined
from calculator_class import CalcDisplay

# create a window
window = tkinter.Tk()

# add a label to the window
window.title("Calculator")
window.geometry("380x300")
window.resizable(False, False)


# creating frame for keys
bottom_frame = tkinter.Frame(window)


# create the calculator display, using imported calculator class
calc_display = CalcDisplay(window)


# callback functions are function that dictates a behavior when an event happens
def zero_callBack():
    calc_display.add_text("0")


def one_callBack():
    calc_display.add_text("1")


def two_callBack():
    calc_display.add_text("2")


def three_callBack():
    calc_display.add_text("3")


def four_callBack():
    calc_display.add_text("4")


def five_callBack():
    calc_display.add_text("5")


def six_callBack():
    calc_display.add_text("6")


def seven_callBack():
    calc_display.add_text("7")


def eight_callBack():
    calc_display.add_text("8")


def nine_callBack():
    calc_display.add_text("9")


def left_bracket_callBack():
    calc_display.add_text("(")


def right_bracket_callBack():
    calc_display.add_text(")")


def multiply_callBack():
    calc_display.add_text("*")


def divide_callBack():
    calc_display.add_text("/")


def add_callBack():
    calc_display.add_text("+")


def subtract_callBack():
    calc_display.add_text("-")


def dot_callBack():
    calc_display.add_text(".")


def equal_callBack():
    calc_display.eval()


def clear_callBack():
    calc_display.clear()


# add buttons to the calculator
seven_button = tkinter.Button(
    bottom_frame, text="7", width=6, height=4, command=seven_callBack
)
seven_button.grid(column=0, row=0)

eight_button = tkinter.Button(
    bottom_frame, text="8", width=6, height=4, command=eight_callBack
)
eight_button.grid(column=1, row=0)

nine_button = tkinter.Button(
    bottom_frame, text="9", width=6, height=4, command=nine_callBack
)
nine_button.grid(column=2, row=0)

left_bracket_button = tkinter.Button(
    bottom_frame, text="(", width=6, height=4, command=left_bracket_callBack
)
left_bracket_button.grid(column=3, row=0)

right_bracket_button = tkinter.Button(
    bottom_frame, text=")", width=6, height=4, command=right_bracket_callBack
)
right_bracket_button.grid(column=4, row=0)

four_button = tkinter.Button(
    bottom_frame, text="4", width=6, height=4, command=four_callBack
)
four_button.grid(column=0, row=1)

five_button = tkinter.Button(
    bottom_frame, text="5", width=6, height=4, command=five_callBack
)
five_button.grid(column=1, row=1)

six_button = tkinter.Button(
    bottom_frame, text="6", width=6, height=4, command=six_callBack
)
six_button.grid(column=2, row=1)

multiply_button = tkinter.Button(
    bottom_frame, text="*", width=6, height=4, command=multiply_callBack
)
multiply_button.grid(column=3, row=1)

divide_button = tkinter.Button(
    bottom_frame, text="/", width=6, height=4, command=divide_callBack
)
divide_button.grid(column=4, row=1)

one_button = tkinter.Button(
    bottom_frame, text="1", width=6, height=4, command=one_callBack
)
one_button.grid(column=0, row=2)

two_button = tkinter.Button(
    bottom_frame, text="2", width=6, height=4, command=two_callBack
)
two_button.grid(column=1, row=2)

three_button = tkinter.Button(
    bottom_frame, text="3", width=6, height=4, command=three_callBack
)
three_button.grid(column=2, row=2)


add_button = tkinter.Button(
    bottom_frame, text="+", width=6, height=4, command=add_callBack
)
add_button.grid(column=3, row=2)

subtract_button = tkinter.Button(
    bottom_frame, text="-", width=6, height=4, command=subtract_callBack
)
subtract_button.grid(column=4, row=2)

zero_button = tkinter.Button(
    bottom_frame, text="0", width=6, height=4, command=zero_callBack
)
zero_button.grid(column=0, row=3)

dot_button = tkinter.Button(
    bottom_frame, text=".", width=6, height=4, command=dot_callBack
)
dot_button.grid(column=1, row=3)

clear_button = tkinter.Button(
    bottom_frame, text="C", width=6, height=4, command=clear_callBack
)
clear_button.grid(column=2, row=3)

# equal botton
equal_button = tkinter.Button(
    bottom_frame, text="=", width=12, height=4, command=equal_callBack
)
equal_button.grid(column=3, row=3, columnspan=2, sticky="WE")

bottom_frame.pack()

# run the calculator window
window.mainloop()
```

## Bibliography

1. Code Refactoring - https://en.wikipedia.org/wiki/Code_refactoring