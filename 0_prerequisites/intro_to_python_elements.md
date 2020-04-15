# Introduction to Programming using Python

Introduction to Programming using Python

## Outline

- Writing simple programs (introduction to elements of a python program)
  - Printing
  - Comments
  - Strings
  - Variables
  - Arithmetic Operations
  - Booleans
- Iterables
  - list
  - tuples
  - strings as iterables
- Control Structures
  - If/else/elif
  - For Loops
  - While Loops
- Data Structures Introduction (Dictionaries)
- Using Functions

<!-- page break -->
<div style="page-break-after: always;"></div>

## Python Programming Essentials - Part 1

### [Python Interactive Environment](https://docs.microsoft.com/en-us/visualstudio/python/python-interactive-repl-in-visual-studio?view=vs-2019)

In this tutorial, we are going to be using the python interactive environment, through the command line. The Interactive environment lets you enter arbitrary Python code and see immediate results. This way of coding helps you learn and experiment with APIs and libraries, and to interactively develop working code to include in your projects. This is a very great feature of the python programming language. In VScode, we will access this by typing `python` in the terminal at the bottom of the window.

### Printing

To print to the terminal in python is as simple as;

```python
print("whatever you want")
```

It is necessary at this point to introduce a variable type called `strings`. This is a kind of variable that stores alphanumeric values such as `"Names"` and `"Places"`. So if we would like to print out a message with a string variable, it is a simple as;

```python
full_name = "Joshua Owoyemi"
# print out the message with the name
print("Full Name: ", full_name)
```

You will notice that a line was started with `#`. This is to tell python program to ignore that line. Therefore anything written on that line is ignored and will not be `compiled`. It is called a `comment`. So if we do something like;

```python
full_name = "Joshua Owoyemi"
#print("Full Name: ", full_name)
```

Nothing will be printed to the terminal because the line has been commented out. `Comments` are useful to add human readable information to our code so we can easily remember or understand what we are trying to do in that part of the code. Please use comments as much as possible.

In python, other variables can also be printed in the already introduced manner. For example a variable storing a number can be printed as such;

```python
number = 7800000000
print("World Population = ", number)

# this is also possible
number = 7.8
print("There are, ", 7.8, "billion people in the world right now")
```

The print statement can be used in more various ways. More of this will be introduced in future sections.

### Strings

One class of variable that deserves to be treated separately is `strings`. This section will focus on `string` manipulation as it has been introduced earlier. Two major manipulation for python strings are `concatenation` and `slicing`. `Concatenation` allows two or more string sequences to be combined into one, such as;

```python
first_name = "Joshua"
last_name = "Owoyemi"
full_name = first_name + " " + last_name
```

Notice that a space (`" "`) is added in the middle as will be expected in a full name.

On the other hand, `slicing` allows us to split a single string variable to smaller pieces as such;

```python
full_name = "Joshua Owoyemi"
first_name = full_name[:6]
last_name = full_name[7:]
```

What happened here is that we give an `index` of the point where we want the string variable to be split. This idea can be applied to some other variable types. We will talk about them in later sections. We can also specify the starting and the ending index, sucha as;

```python
full_name = "Joshua Owoyemi"
first_name = full_name[0:6] # same output as previous example
last_name = full_name[7:13] # same output as previous example
```

### Numbers

Generally, in python, a variable type is whatever you assign to it. In other programming languages like `c++` and `java` this is not the case as you have to explicitly specify or declare the variable type. Even though there is still a differentiation between types such as `integers` (whole numbers) and `floats` (numbers with decimal places), this is only done implicitly.

```python
# assign a value of 2 to the variable x
x = 2

# assign a value of 10.5 to the variable y
y = 10.5
```

We can find out the type of a variable by using the keyword `type`.

```python
>>> type(x)
int

>>> type(y)
float
```

### Arithmetic Operations

The following are the arithmetic operations on numbers in python.

| Operation | Description                                             |
| --------- | ------------------------------------------------------- |
| x + y     | Sum of two numbers                                      |
| x - y     | Difference of two numbers                               |
| x * y     | Product of two numbers                                  |
| x / y     | Quotient of two numbers                                 |
| x // y    | Quotient of two numbers, returned as an integer         |
| x % y     | x “modulo”: y: The remainder of x / y for positive x, y |
| x ** y    | x raised to the power y                                 |
| -x        | A negated number                                        |
| abs(x)    | The absolute value of a number                          |

Arithmetic operations can also be combined;

```python
>>> 5 + 2 * 5
15

# opetations can be grouped using the parenthesis
>>> (5 + 2) * 5
35
```

### Boolean

Another important class of variable types is the boolean or simply `bool`. This has only two values; `True` or `False`, which can also be `numbers` or `0` respectively. this is very useful in making comparisons, which happens a lot in programming.

```python
# assign the boolean value True to the variable check
check = True

# assign the boolean value False to the variable present
present = False
```

### Boolean Operations

The following are operations for comparing variables. Results are either `True` or `False`.

| Operation | Description                                |
| --------- | ------------------------------------------ |
| x == y    | Check if two numbers have the same value   |
| x != y    | Check if two numbers have different values |
| x > y     | Check if x is greater than y               |
| x >= y    | Check if x is greater than or equal to y   |
| x < y     | Check if x is less than y                  |
| x <= y    | Check if x is less than or equal to y      |

## Iterables

An iterable is an object capable of returning its elements one at a time. The elements of the iterables can be retrieved by using the addresses, known as the `index`. The following are python iterables.

### Lists

Lists are designated by square brackets - `[]` and can store various types of elements. The elements can be changed making them mutable.

```python
# a list of integer numbers
nums_list = [0, 1, 2, 3, 4, 5, 6]

# a list of names
names_list = ["Tolu", "John", "Maxwell", "Bill"]

# elements can be mixed or contain other lists
mixed_list = ["fish", 45, [3.6, 5.6], True]
```

### Tuples

Tuples are similar to lists but the elements cannot be changed making them immutable. They are designated by the parenthesis `()`.

```python
# tuple of numbers
nums_tuple = (0, 1, 2, 3, 4, 5, 6)

# tuples can also be mixed
mixed_tuple = ("house", 45, [0.1, 0.2], False)
```

### Strings as iterables

We can also consider string as iterables, since we can retrieve elements of a string just like the lists and tuples. A `for loop` can also be called on it just like in tuples and lists. We will talk more about this in later sections.

### Dictionaries

Dictionaries are a special iterable that uses `keys` instead of `indices`. The `keys` cannot be only numbers but also strings. Therefore the elements of a dictionary consist of a `key` and `value` pair just words and definitions in an English dictionary.

```python
person_dict = {"name": "Nikola Tesla", "age": 86, "parents": ["Milutin Tesla", "Duka Tesla"] }
```

One important note about dictionaries is that the elements cannot be retrieved in a particular order since they are accessed using the `keys`.

## Good and bad variable names

The following are [rules or guidelines](http://makemeanalyst.com/python-programming/variable-names-and-keywords/) in other to use a suitable variable name in python;

- A variable can contain both letters and numbers, but they cannot start with a number. So, variable1 is valid while 1variable is a invalid name.
- You may use uppercase letters for variable names but it is always perfectly fine to begin variable names with a lowercase letter.
- If your Variable name is long, then you can use underscore character (_) in the name. For example, top_five_members, var_1 etc. all are valid example.
- You can’t use special characters like !, @, #, $, % etc. in variable name.
- Python keywords cannot be used as variable name.

The following are examples of python keywords that cannot be used as variable names. Python will output `syntax error` if they are used.

```python
1var=20
class=5
global=10
all@1=100
```

## Introduction to Functions

Blocks of code that achieve special defined purposes. Helps to keep our code organized and easy to reuse. A function is defined as in;

```python

# function with one argument
def square_of(x):
  # a function that returns the square of a number
  x_square = x**2
  return x_square

# a function with 2 arguments
def add(x,y):
  # a function that adds two numbers
  sum = x + y
  return sum

# function with no return value
def print_message(message):
  print("The message is: ", message)
```

When we call other packages, we call them in form of functions. More advanced use of functions will be discussed in later sections.

## More on Iterables

- How to use iterables
- Functions to manipulate iterables
- Pros and cons of each class

<!-- page break -->
<div style="page-break-after: always;"></div>

## Bibliography

https://www.pythonlikeyoumeanit.com/index.html