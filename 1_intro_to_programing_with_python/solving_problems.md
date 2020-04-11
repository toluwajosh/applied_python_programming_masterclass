# Solving Programing Problems with Python (LeetCode 3)

In this video post, I talk about the general approach to solving a programming problem, while utilizing the ideas we have covered so far in this series. To drive home this idea, I use a popular problem from Leetcode.com.

## Outline (use a sample problem)

- writing pseudocodes
- create a simple program structure from the pseudocode
- write the code
  - use functions as much as possible
- Sample problem solution

This a topic which is best explain through an example. Here we are going to use a popular problem from leetcode.com. This is a problem you need to be familiar with if you ever want to get a job as a software engineer. Here, we are going to solve the problem with the Python language. The problem is called [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/).

## Writing Pseudocodes

A pseudocode is 'false' code. This means the code or set of instructions is written in a way that does not follow any particular programming language. It helps us to understand the steps necessary to solve a particular problem without thinking about the syntax of the programming language. Suppose we want to write the pseudocode for checking the largest of two numbers `a` and `b`, we might write something like;

```txt
1. Get a and b
2. check a>b
3. if 2 is true, then a is largest
4. else(if 2. is not true) then b is largest
5. return largest
```

This is not a real code but it shows the steps someone might take to solve the problem. It turns out that this step is very important and it helps many programmers to save a lot of time in solving the problem. Without this step, it is easy to run into problems while writing the code and spending a lot of time to fix bugs and logic of the problem solution. Now let us use this idea to solve our problem. Here is a possible pseudocode for the `Longest Substring Without Repeating Characters` problem;

```txt
1. For each letter s in the string
2. If s did not appear before, store s and index of s somewhere
3. If s appeared before, calculate the lenght between index of now and index of before
4. Compare lenght if it is the largest
5. Return largest lenght
```

Next, we will create a program structure from the pseudocode. This will be the structure that we follow when finally write our code. In our case, we will write actual code but only lines that show the parts of the solution. In reality, we can do something like this, bearing in mind that we will use functions as much as possible;

```python
# function to find lenght
def lengthofLongestSubstring(string):
  # check edge cases

  # initialize variables

  # for loop to check string
  
  # if seen

  # check longest length.

  # return result
  pass


# test an example
answer = lengthOfLongestSubstring("baaaccb")
print(answer)
```

With this down, we can begin to fill in the code to the different parts of the program. At the end, we will have this final code (See the YouTube Video for the process).

```python
# function to find lenght
def lengthOfLongestSubstring(s):
    # check edge cases
    if s == "":
        return 0

    # initialize variables
    tail = 0
    cur_len = 0
    seen = {s[0]: 0}
    longest = 1

    # for loop to check string
    for head in range(1, len(s)):
        # if seen
        if s[head] in seen:
            tail = max(seen[s[head]] + 1, tail)
        seen[s[head]] = head
        cur_len = head - tail + 1

        # check longest length.
        if cur_len > longest:
            longest = cur_len

    # return result
    return longest

# test an example
answer = lengthOfLongestSubstring("baaaccb")
print(answer)
```

Go ahead and see if you can try some other problems on the [Leetcode](leetcode.com) website using the idea in this post.

See you in the next post.
