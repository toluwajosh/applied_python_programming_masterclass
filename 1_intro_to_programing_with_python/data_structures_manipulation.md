# Python Programming Essentials - Data Structures and Manipulation

In this post, we are going to look a little deeper in how to manipulate the different data structures we have seen so far in Python programming. Those are `Lists` and `Dictionaries`. More importantly, we will look at the built-in functions for each class and use this knowledge to solve a very common technical problem.

## Outline

- Lists Operations and Functions
- Dictionaries Manipulation
- Time complexity (data cost)
- Data structure problem

## Lists Operations and Functions

We have seen some examples on how to use a list in previous sections. Here we will only outline the various popular operations and functions that can be carried out on a `List`.

| Operations          | Meaning                                                     |
| ------------------- | ----------------------------------------------------------- |
| {List} + {List}     | Concatenation                                               |
| {List} * {int}      | Repeat `List` {int} number of times                         |
| len({List})         | Find the length of `List`                                   |
| {List}.append(x)    | Adds element `x` to end of list                             |
| {List}.sort()       | Return a sorted `List`                                      |
| {List}.reverse()    | Reverse the `List`                                          |
| {List}.index(x)     | Returns the index of first occurrences of `x` in list       |
| {List}.insert(i, x) | Inserts `x` into list at index `i`.                         |
| {List}.count(x)     | Returns the number of occurrences of `x` in list            |
| {List}.remove(x)    | Deletes the first occurrence in the list                    |
| {List}.pop(i)       | Deletes the `i`th element of the list and returns its value |

Some examples of the above operations are shown below.

```python
>>> [1, 2, 3, 4] + [5, 6, 7, 8] # List concatenation
[1, 2, 3, 4, 5, 6, 7, 8]

>>> [1, 2, 3, 4] * 2 # List repetition
[1, 2, 3, 4, 1, 2, 3, 4]

>>> a = [1, 2, 3, 4]
>>> a.append(5)
>>> a
[1, 2, 3, 4, 5]
```

## Dictionaries

Dictionaries are another class of iterable or `collections` that uses `keys` instead of `indices` for elements in the object. The `keys` may not be only numbers but also strings. Therefore the elements of a dictionary consist of a `key` and `value` pairs, just like words and definitions in an English dictionary. This allows us to easily find information stored in them by using the defined `key`.

```python
person_dict = {"name": "Nikola Tesla", "age": 86, "parents": ["Milutin Tesla", "Duka Tesla"] }

# a new key value pair can be assigned in the variable as follows
person_dict["Nationality"] = "American"
```

To get the value associated with a key, we simply do

```python
>>>person_dict["name"]
Nikola Tesla
```

Note that if the `key` is not in the dictionary, a `KeyError` is thrown by the python interpreter.
One important note about dictionaries is that the elements cannot be retrieved in a sequential order since they are accessed using the `keys`.

### Dictionaries Operations and Functions

Dictionaries can be manipulated with the following operations. 

| Function          | Meaning                                                                         |
| ----------------- | ------------------------------------------------------------------------------- |
| {Dict}.keys()     | Returns a sequence of keys.                                                     |
| {Dict}.values()   | Returns a sequence of values.                                                   |
| {Dict}.items()    | Returns a sequence of tuples (`key`, `value`) representing the key-value pairs. |
| del {Dict}[{key}] | deletes the specified entry.                                                    |
| {Dict}.clear()    | Deletes all entries                                                             |

## Difference between `List` and `Dictionary` data structure

We have seen that `Lists` are ordered while `Dictionaries` are not, hence lists are indexed with integers while dictionaries uses keys to obtain the value pair. However, because of how elements are accessed in both data structures, it is more efficient to use a dictionary for lookup of elements because it takes less time to traverse in the dictionary than a list. What this means is that in a list when an element is retrieved, each element is checked from the first one until the desired index but in dictionaries, the key is 'connected' directly to the address of the value so it takes less time to retrieve the value.

## Bibliography

1. John M. Zelle, Python Programming: An Introduction to Computer Science. Franklin, Beedle & Associates, Inc., 2004
2. https://www.geeksforgeeks.org/difference-between-list-and-dictionary-in-python/