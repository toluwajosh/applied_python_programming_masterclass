# Object Oriented Programming in Python

## Outline (use a sample problem)

- OOP, What and Why
- Inheritance
- Class Methods
- Python Calculator

## OOP, What and Why

The simplest what to explain OOP is "A way of program that allows us to bundle and transfer the properties and behaviors of an `object` from one form to another. If we think of a type of objects as `Animals`. This means an animal has some properties and behaviors that allows us to categorize a `Dog` as an animal. A dog there `inherits` the properties of the animal `class`. However a dog has its own properties and behaviors, that makes it different from a chicken, which are subset of those of the animal family. So, given that we have the dog class, we can also define a new class of of `Bull Dogs` which has inherited properties from the `Dog` class. This is a conceptual idea of OOP. We refer to each entity in OOP as an `Object` and a category as `Class`.
In Python, a simple animal class can be;

```python
class Animal:
    has_blood=True
    can_move=True
    reproduce_sexually=True
```

The `instance` of a class is a copy of that class with actual values. For example;

```python
# create an instance from the Animal class
an_animal = Animal()
# this `an_animal` has all the attributes of the Animal Class.

>>> an_animal.has_blood
True

>>> an_animal.can_move
True
```

In Python typical definition of a class is as follows:

```python
class Animal(object):
    # default attributes
    has_blood=True
    can_move=True
    reproduce_sexually=True
    # Initializer / Instance Attributes
    def __init__(self, name):
        self.name = name
```

`object` is the base class that all other objects `inherit` from. It allows us to use predefined functions or methods for a class, one of which is `__init__`. `__ini__` is used to initialize a class attribute when the instance is created. `self` is used to refer to the current class inside itself. An updated initialization of our `Animals` class will become;

```python
# lets use a name to identify the animal
a_dog = Animal("dog") # we initialize self.name to "dog"

>>> a_dog.name
"dog"
```

## Inheritance

To demonstrate `inheritance` (How an attribute is passed to a child class), we will create another class called `Dog`, as follows;

```python
class Dog(Animal):
    def __init__(self, name, age, color):
        self.name = name
        self.color = color
```

We can check that our new class `Dog` also has the attributes of the `Animal` class.

```python
a_dog = Dog("bull_dog")

>>> a_dog.name
'bull_dog'

>>> a_dog.has_blood
True
```

## Class Methods

We have already used the class method `__ini__`. There are many of such predefined methods but we won't cover them here. However, we can create our own methods. These are just functions that belong to a class. Remember {List}.pop(). `pop` is a function of the `List` class so we can call `pop` on a class instance. 

```python
class Dog(Animal):
    def __init__(self, name, age, color):
        self.name = name
        self.color = color

    # a function to introduce the class instance
    def introduce(self): # may or may not take an argument
        print("I am ", self.name, ".Nice to meet you.")


>>> a_dog = Dog("bull_dog")
>>> a_dog.introduce()

'I am bull_dog. Nice to meet you.'
```

Finally, we will use these ideas to create a python calculator. If you have followed this series up until this point, then you should be able to understand this code to a large extent. We will use another class  (or `Library`) called `tkinker` and its methods. A more detailed documentation of this Library can be found [here](https://docs.python.org/3/library/tkinter.html). I will advise to use this only as a reference since there are a lot of information provided there.

See below my code for the `Python Calculator`. See the inline comments for the explanation of each part, or watch the Video.

```python
"""
Using the ktinker module of python to write a calculator program
"""
import tkinter

# create a window
window = tkinter.Tk()

# add a label to the window
window.title("Calculator")
window.geometry("380x380")
window.resizable(False, False)


# creating two frames, top and bottom. Frames are sections of a window
top_frame = tkinter.Frame(window) # you can also use "y" as the fill parameter
bottom_frame = tkinter.Frame(window)

# insert textbox in the top frame and a button in bottom frame
display_text_variable = tkinter.StringVar()
current_display_text=""
display_text_variable.set(current_display_text)
display_text = tkinter.Label(top_frame, font={"arial", 120, "bold"}, textvariable = display_text_variable, 
                        width=32, bg = "#eee", bd=5, anchor="e", justify="left")
display_text.grid(column=0, row=0, sticky="E")
display_text.pack(fill="x")
top_frame.pack(fill="x")


# a class that defines the display of the calculator
class CalcDisplay(object):

  # initialize calculator instance
  def __init__(self):
    self.current_display_text = ""

  # add a text to the calculator
  def add_text(self, text_to_add):
    self.current_display_text += text_to_add
    display_text_variable.set(self.current_display_text)

  # evaluate the expression in the calculator
  def eval(self):
    
    # dont worry about this part.
    # We want to make sure this part runs
    try:
      eval_text = eval(self.current_display_text)
      self.current_display_text = str(eval_text)
      display_text_variable.set(str(self.current_display_text))
    # and if there is an error, we have backup plan. :)
    except Exception as e:
      display_text_variable.set("Error!")
      pass
  
  # clear the calculator display
  def clear(self):
    self.current_display_text = ""
    display_text_variable.set(self.current_display_text)


# create the calculator display
calc_display = CalcDisplay()


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
seven_button = tkinter.Button(bottom_frame, text ="7", width=6, height=4, command = seven_callBack)
seven_button.grid(column=0, row=0)

eight_button = tkinter.Button(bottom_frame, text ="8", width=6, height=4, command = eight_callBack)
eight_button.grid(column=1, row=0)

nine_button = tkinter.Button(bottom_frame, text ="9", width=6, height=4, command = nine_callBack)
nine_button.grid(column=2, row=0)

left_bracket_button = tkinter.Button(bottom_frame, text ="(", width=6, height=4, command = left_bracket_callBack)
left_bracket_button.grid(column=3, row=0)

right_bracket_button = tkinter.Button(bottom_frame, text =")", width=6, height=4, command = right_bracket_callBack)
right_bracket_button.grid(column=4, row=0)

four_button = tkinter.Button(bottom_frame, text ="4", width=6, height=4, command = four_callBack)
four_button.grid(column=0, row=1)

five_button = tkinter.Button(bottom_frame, text ="5", width=6, height=4, command = five_callBack)
five_button.grid(column=1, row=1)

six_button = tkinter.Button(bottom_frame, text ="6", width=6, height=4, command = six_callBack)
six_button.grid(column=2, row=1)

multiply_button = tkinter.Button(bottom_frame, text ="*", width=6, height=4, command = multiply_callBack)
multiply_button.grid(column=3, row=1)

divide_button = tkinter.Button(bottom_frame, text ="/", width=6, height=4, command = divide_callBack)
divide_button.grid(column=4, row=1)

one_button = tkinter.Button(bottom_frame, text ="1", width=6, height=4, command = one_callBack)
one_button.grid(column=0, row=2)

two_button = tkinter.Button(bottom_frame, text ="2", width=6, height=4, command = two_callBack)
two_button.grid(column=1, row=2)

three_button = tkinter.Button(bottom_frame, text ="3", width=6, height=4, command = three_callBack)
three_button.grid(column=2, row=2)


add_button = tkinter.Button(bottom_frame, text ="+", width=6, height=4, command = add_callBack)
add_button.grid(column=3, row=2)

subtract_button = tkinter.Button(bottom_frame, text ="-", width=6, height=4, command = subtract_callBack)
subtract_button.grid(column=4, row=2)

zero_button = tkinter.Button(bottom_frame, text ="0", width=6, height=4, command = zero_callBack)
zero_button.grid(column=0, row=3)

dot_button = tkinter.Button(bottom_frame, text =".", width=6, height=4, command = dot_callBack)
dot_button.grid(column=1, row=3)

clear_button = tkinter.Button(bottom_frame, text ="C", width=6, height=4, command = clear_callBack)
clear_button.grid(column=2, row=3)

#equal botton
equal_button = tkinter.Button(bottom_frame, text ="=",width=12, height=4, command = equal_callBack)
equal_button.grid(column=3, row=3, columnspan=2, sticky="WE")

bottom_frame.pack()

# run the calculator window
window.mainloop()

```

The calculator is not perfect yet. Can you make it better? Let me know what you did to make it better. Cheers

Here is the end of the Python Programming Essentials Series. In the next series, I will do 10 simple Python Projects that can give anyone a good grasp of the Language. See you then.

## Bibliography

1. https://www.pythonlikeyoumeanit.com/module_4.html
2. https://realpython.com/python3-object-oriented-programming/