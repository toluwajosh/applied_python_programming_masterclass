# Python Programming Essentials - Iterables and Functions

## Outline
- Assigning Inputs
- Iterables
  - Lists
  - Tuples
  - Strings as iterables
  - Dictionaries
- Good and bad variable names
- Introduction to Functions

## Assigning Inputs

The purpose of an input statement is to get some information from the user of a program and store it into a variable. The exact form of an input statement depends on what type of data you are trying to get from the user. For textual input, the statement will look like this:

```python
# <variable> = input(<prompt>)
# for example
name = input("Enter your name: ")
```

The `prompt` is a string expression that is used to prompt the user for input. As mentioned, the inputs are received as string values so in case of receiving a number, it needs to be converted to a number before it can be used as intended.

```python
age = input("Enter your age: ")
new_age = age + 5 # this line will give an error since `age` is still a string type
new_age = int(age) + 5 # here, age gets converted to an integer type first.
```

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

# change an element at index 5
nums_list[5] = 56
```

### Tuples

Tuples are similar to lists but the elements cannot be changed making them immutable. They are designated by the parenthesis `()`.

```python
# tuple of numbers
nums_tuple = (0, 1, 2, 3, 4, 5, 6)

# tuples can also be mixed
mixed_tuple = ("house", 45, [0.1, 0.2], False)

# trying to change an element at an index results in an error
nums_tuple[3] = 22
```

### Strings as iterables

We can also consider string as iterables, since we can retrieve elements of a string just like in the lists and tuples. A `for loop` can also be called on it just like in tuples and lists. We will talk more about this in later sections.

### Dictionaries (was skipped in the video, so will be added in the next part)

Dictionaries are a special iterable that uses `keys` instead of `indices`. The `keys` cannot be only numbers but also strings. Therefore the elements of a dictionary consist of a `key` and `value` pairs, just like words and definitions in an English dictionary.

```python
person_dict = {"name": "Nikola Tesla", "age": 86, "parents": ["Milutin Tesla", "Duka Tesla"] }

# a new key value pair can be assigned in the variable as follows
person_dict["Nationality"] = "American"
```

One important note about dictionaries is that the elements cannot be retrieved in a sequential order since they are accessed using the `keys`.

## Good and bad variable names

At this point, it is necessary to talk about variable names that are acceptable in python programming. There is no need to memorize any rules but the following are [guidelines](http://makemeanalyst.com/python-programming/variable-names-and-keywords/) in other to use a suitable variable name in python;

- A variable can contain both letters and numbers, but they cannot start with a number. So, variable1 is valid while 1variable is a invalid name.
- You may use uppercase letters for variable names but it is always perfectly fine to begin variable names with a lowercase letter.
- If your Variable name is long, then you can use underscore character (_) in the name. For example, top_five_members, var_1 etc. all are valid example.
- You can’t use special characters like !, @, #, $, % etc. in variable name.
- Python keywords cannot be used as variable name.

The following are examples of incorrect variable names and python keywords that cannot be used as variable names. Python will output `syntax error` if they are used as variable names or with incorrect syntax.

```python
1var=20 # cannot start with a number
all@1=100 # unacceptable symbol `@` is used in a variable name
False
class
finally
is
return
None
continue
for
lambda
try
True
def
from
nonlocal
while
and
del
global
not
with
as
elif
if
or
yield
assert
else
import
pass
break
except
in
raise
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

# functions with no return value
def print_message(message):
  print("The message is: ", message)

def greet(name):
  print("Hello", name)
  print("How are you?")
```

When we call other packages, we call them in form of functions. More advanced use of functions will be discussed in later sections.

<!-- page break -->
<div style="page-break-after: always;"></div>

## Bibliography

1. https://www.pythonlikeyoumeanit.com/index.html
2. John M. Zelle, Python Programming: An Introduction to Computer Science. Franklin, Beedle & Associates, Inc., 2004
