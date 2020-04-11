"""
Using the ktinker module of python to write a calculator program
"""
import tkinter

window = tkinter.Tk()
# add a label to the window
window.title("Calculator")
window.geometry("380x380")
window.resizable(False, False)


# creating two frames, top and bottom
top_frame = tkinter.Frame(window) # you can also use "y" as the fill parameter
bottom_frame = tkinter.Frame(window)

# insert textbox in the top frame and a button in bottom frame
# display_area = tkinter.Entry(top_frame, font={"arial", 18, "bold"}, textvariable = "default", width = 50, bg = "#eee", bd=0).pack(fill="x")
display_text_variable = tkinter.StringVar()
current_display_text=""
display_text_variable.set(current_display_text)
display_text = tkinter.Label(top_frame, font={"arial", 120, "bold"}, textvariable = display_text_variable, 
                        width=32, bg = "#eee", bd=5, anchor="e", justify="left")
display_text.grid(column=0, row=0, sticky="E")
display_text.pack(fill="x")
top_frame.pack(fill="x")

class CalcDisplay(object):
  def __init__(self):
    self.current_display_text = ""
  def add_text(self, text_to_add):
    self.current_display_text += text_to_add
    display_text_variable.set(self.current_display_text)
  def eval(self):
    try:
      eval_text = eval(self.current_display_text)
      self.current_display_text = str(eval_text)
      display_text_variable.set(str(self.current_display_text))
      # self.current_display_text = ""
    except Exception as e:
      display_text_variable.set("Error!")
      pass
  def clear(self):
    self.current_display_text = ""
    display_text_variable.set(self.current_display_text)


calc_display = CalcDisplay()

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


seven_button = tkinter.Button(bottom_frame, text ="7", width=6, height=4, command = seven_callBack)
seven_button.grid(column=0, row=0)
# seven_button.pack()

eight_button = tkinter.Button(bottom_frame, text ="8", width=6, height=4, command = eight_callBack)
eight_button.grid(column=1, row=0)
# eight_button.pack()

nine_button = tkinter.Button(bottom_frame, text ="9", width=6, height=4, command = nine_callBack)
nine_button.grid(column=2, row=0)
# nine_button.pack()

left_bracket_button = tkinter.Button(bottom_frame, text ="(", width=6, height=4, command = left_bracket_callBack)
left_bracket_button.grid(column=3, row=0)
# left_bracket_button.pack()

right_bracket_button = tkinter.Button(bottom_frame, text =")", width=6, height=4, command = right_bracket_callBack)
right_bracket_button.grid(column=4, row=0)
# right_bracket_button.pack()

four_button = tkinter.Button(bottom_frame, text ="4", width=6, height=4, command = four_callBack)
four_button.grid(column=0, row=1)
# four_button.pack()

five_button = tkinter.Button(bottom_frame, text ="5", width=6, height=4, command = five_callBack)
five_button.grid(column=1, row=1)
# five_button.pack()

six_button = tkinter.Button(bottom_frame, text ="6", width=6, height=4, command = six_callBack)
six_button.grid(column=2, row=1)
# six_button.pack()

multiply_button = tkinter.Button(bottom_frame, text ="*", width=6, height=4, command = multiply_callBack)
multiply_button.grid(column=3, row=1)
# multiply_button.pack()

divide_button = tkinter.Button(bottom_frame, text ="/", width=6, height=4, command = divide_callBack)
divide_button.grid(column=4, row=1)
# divide_button.pack()

one_button = tkinter.Button(bottom_frame, text ="1", width=6, height=4, command = one_callBack)
one_button.grid(column=0, row=2)
# one_button.pack()

two_button = tkinter.Button(bottom_frame, text ="2", width=6, height=4, command = two_callBack)
two_button.grid(column=1, row=2)
# two_button.pack()

three_button = tkinter.Button(bottom_frame, text ="3", width=6, height=4, command = three_callBack)
three_button.grid(column=2, row=2)
# three_button.pack()


add_button = tkinter.Button(bottom_frame, text ="+", width=6, height=4, command = add_callBack)
add_button.grid(column=3, row=2)
# add_button.pack()

subtract_button = tkinter.Button(bottom_frame, text ="-", width=6, height=4, command = subtract_callBack)
subtract_button.grid(column=4, row=2)
# subtract_button.pack()

zero_button = tkinter.Button(bottom_frame, text ="0", width=6, height=4, command = zero_callBack)
zero_button.grid(column=0, row=3)
# zero_button.pack()

dot_button = tkinter.Button(bottom_frame, text =".", width=6, height=4, command = dot_callBack)
dot_button.grid(column=1, row=3)
# dot_button.pack()

clear_button = tkinter.Button(bottom_frame, text ="C", width=6, height=4, command = clear_callBack)
clear_button.grid(column=2, row=3)
# clear_button.pack()

#equal botton
equal_button = tkinter.Button(bottom_frame, text ="=",width=12, height=4, command = equal_callBack)
equal_button.grid(column=3, row=3, columnspan=2, sticky="WE")
# equal_button.pack()

bottom_frame.pack()

# run the window
window.mainloop()
