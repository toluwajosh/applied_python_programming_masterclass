# Code Organization for the OCR Project

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

This second approach is the way to use functions from another file.

## Assignment

Now 