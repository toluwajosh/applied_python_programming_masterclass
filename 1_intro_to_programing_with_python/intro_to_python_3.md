# Python Programming Essentials - Control Structures

## Outline
- If/else/elif
- Loops
  - For Loop
  - While Loop
- More on Iterables

## If/else/elif

There are times in our program that we want some certain behavior based on some defined conditions. Suppose we want to customize a response based on the age entered by the user, then we will use the `if/else` statement to do this:

```python
age = input("What is your age?")
# customize responce based on value of age
if age > 18:
    print("Wow, you are older than I expected. Awesome!")
else:
    print("Wow, you are younger than I expected, Fabulous!")
```

Notice that the block of code that is execute in each `if` statement is indented. This is very important as only codes indented under the statement is considered under that condition. If no block of code is indented under the `if` statement, an error will occur because this is the expected syntax by python programmin language. We can also have a standalone `if` statement.

```python
# do some computation
...
# this part only executes if the condition is satisfied
if answer < 0:
    answer = 0

# the program continues running
...
```

We can also specify multiple conditions that the we want to satisfy. This is done by adding the `elif` keyword at every new condition. A typical example is giving student grades based on the scores. Also note the use of boolean operations and the combination of multiple comparisons using the `and` keyword.

```python
# get the score
score = input("Enter a score")

if score < 50:
    print("Your grade is D")
elif score >= 50 and score < 60:
    print("Your grade is C")
elif score >= 60 and score < 70:
    print("Your grade is B")
else: # the final condition can be specified implicitly. That is, score >= 70
    print("Your grade is A")
```

Basically, the interpreter goes through every condition one after the other and once a condition is satisfied, it leaves the control structure and continues running the rest of the program. If none of the conditions are satisfied, it runs the final `else` statement. We may also have a multiple condition control structure that does not use the else statement, hence nothing is done if no condition is satisfied.

## Loops

Loops are a way for programmers to execute sequence of statements multiple times in succession. It usually involves a variable that increases or decreases in succession. Python program has two of such kind of constructs - `For Loops` and `While Loops`.

### For Loop

This is a kind of loop that will execute a definite number of times, also known as `Definite Loops`. The number of times it will execute is usually defined at the beginning of the loop, then the program exits the loop after has been executed the specified number of times. Here is a fun example called "I Love you 3000".

```python
for i range(3000):
    print("I love you ", i)
```

```bash
I love you  0
I love you  1
I love you  2
...
I love you  2997
I love you  2998
I love you  2999
```

Note the use of the keyword `range`. This is a simple way in Python to give numbers between an upper and lower bound. The full definition is `range(start: int, stop: int, step: int=...)`. That is we can specify the start value, the stop value and the increment value. In the case that we supplied only one value, then it starts at 0 and the step is `1`. This is a very handy keyword or function. We can also have decreasing range, such as;

```python
for i in range(10, 0, -1):
    print(i, " left")
```

```bash
10  left
9  left
8  left
7  left
6  left
5  left
4  left
3  left
2  left
1  left
```

## While Loop

This is a kind of loop with a condition on how the loop is exited. It can result in an indefinite loop depending on the condition. This is best explained by an example;

```python
i = 10
while i > 0:
    print(i, " left")
    i = i - 1 # without this line the loop will continue indefinitely

```

This basically has the same result has the previous example with the `For Loop`. However, here we explicitly specify the condition to exit the loop. Note that this prone to a bug known as the `infinite lopp` since we have to keep track of the condition to ensure that it can be met.

## For Loop + Iterables

We can use a `For Loop` to access sequentially the elements of an `iterable` such as `list` and `strings`. This is very helpful when we want to perform an operation on each element of the `iterable`. For example

```python
# given points on an `x` axis, we want to find a corresponding points on the `y` axis
x = [-5, -2, 0, 1, 3, 6]
for t in x:
    y = t**2 + 3*t + 5
    print("x: ", t, "y: ", y)
```

In this example, the calculation is performed on each element `t` of List `x`. A similar operation can be done for a string variable;

```python
string = "MISSISSIPPI"
for s in string:
    print(s)
```

```bash
M
I
S
S
I
S
S
I
P
P
I
```

## Bibliography

1. https://www.pythonlikeyoumeanit.com/index.html
2. John M. Zelle, Python Programming: An Introduction to Computer Science. Franklin, Beedle & Associates, Inc., 2004
