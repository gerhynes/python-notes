# Python Notes

Python is one of the most popular and flexible programming langauges, used for everything from basic scripting to machine learning.

## Numbers

Python stores integers and floating point numbers differently, as an `int` or `float`.

If you do calculations with an `int` and a `float`, Python will return a `float`.

#### Common maths operators

| Symbol | Name             |
| ------ | ---------------- |
| +      | Addition         |
| -      | Subtraction      |
| \*     | Multiplication   |
| /      | Divison          |
| \*\*   | Exponentiation   |
| %      | Modulo           |
| //     | Integer Division |

In Python division retuns a float by default if applicable: `1/2` returns `0.5`.

Exponentiation raises a number to a given power:

```python
2 ** 3    # 8
49 ** 0.5 # 7.0
```

Modulo divides two numbers and returns the remainder. It's often used to check if a number is even or odd.

```python
10 % 3 # 1
16 % 2 # 0
```

Integer division will return a floored `int`:

```python
10/3 #3.33333333
10//3 #3
```

#### Comments

Comments in Python files start with a #, `# more of a comment than a question`.

## Variables and Data Types

Variables are named symbols that hold a value.

Variables must be assigned before they can be used.

Assigning a variable: `x = 100`

Variables can be reassigned at any time.

You can assign multiple variables at the same time.

```python
all, at, once = 5, 10, 15
```

#### Naming Restrictions

- Variables must start with a letter or underscore
- The rest of the name must consist or letters, numbers or underscores
- Names are case sensitive

### Naming Conventions

- Most variables should be snake_case
- Most variables should be lowercase
- CAPITAL_SNAKE_CASE ususally refers to constants, for example PI
- UpperCamelCase usaully refers to a class
- Variables that start and end with two underscores ("dunder") are supposed to be private and left alone: `__no_touchy__`

### Data Types

| Data Type | Description                                              |
| --------- | -------------------------------------------------------- |
| bool      | True or False values                                     |
| int       | an integer (1,2,3)                                       |
| str       | a sequence of unicode characters                         |
| list      | an ordered sequence of values [1,2,3]                    |
| dict      | a collection of key value pairs {"first_name": "Gerard"} |

### Dynamic Typing

Unlike statically-typed languages, Python lets you reassign variables to different types.

```python
example = "a Bernese Mountain Dog"
example = 7
```

### None

`None` is Python's version of `null`, respresenting nothingness.

## Strings

String literals can be declared with either single or double quotes. Be consistent.

In Python, there are escape sequences, all starting with a backslash, which are interpreted according to specific rules.

| Escape Sequence | Meaning     |
| --------------- | ----------- |
| \n              | new line    |
| \\              | backslash   |
| \"              | doublequote |
| \'              | singlequote |

#### Formatting Strings

You can concatenate strings with the "+" operator. If you try to concatenate a number and string, you'll get a TypeError.

You can update a string using the "+=" operator.

```python
str_one = "ice"
str_one += " cream"
str_one # "ice cream"
```

Python lets you interpolate variables into strings. Since Python 3.6 you can use F-Strings:

```python
x = 10
formatted_str = f"I've told you {x} times already!"
```

Before Python 3.6, the format method was common:

```python
x = 10
formatted_str = "I've told you {} times already!".format(x)
```

You can access individual string characters using square brackets and the characters index: `"yes"[0] # 'y'`

### Converting Data Types

In string interpolation, data types are implicitly coverted into string form.

You can explicitly convert variables by using the name of the built-in type as a function.

```python
decimal = 3.14159
integer = int(decimal) # 3

my_list = [1, 2, 3]
my_list_as_string = str(my_list) # "[1, 2, 3]"
```

## Booleans and Conditional Logic

Python has a built in function, `input`, to prompt the user and store the result in a variable.

```python
name = input()
if name == "Arya Stark":
    print("Stabby stabby")
elif name == "John Snow":
    print("*Indecision*")
else:
    print("Carry on")
```

In Python, all conditional checks resolve to True or False.

Besides False conditional checks, other things that are naturally falsy include: empty objects, empty strings, None, and zero.

#### Comparison Operators

| Operator | What it does                                  |
| -------- | --------------------------------------------- |
| ==       | Truthy if a has the same value as b           |
| !=       | Truthy if a does not have the same value as b |
| >        | Truthy if a is greater than b                 |
| <        | Truthy if a is less than b                    |
| >=       | Truthy if a is greater than or equal to b     |
| <=       | Truthy if a is less than or equal to b        |

#### Logical Operators

| Operator | What it does                        |
| -------- | ----------------------------------- |
| and      | Truthy if both a and b are true     |
| or       | Truthy if either a or b are true    |
| not      | Truthy if the opposite of a is true |

#### is vs ==

In Python `==` and `is` are similar but not the same.

```python
a = [1,2,3]
b = [1,2,3]
a == b # True
a is b # False
c = b
b is c # True
```

`==` checks if the variables' values are the same. `is` checks if the variables are stored in the same place in memory.

#### Nested if statement

In Python, nested if statements are constructed through indentation:

```python
age = input("How old are you?: ")
if age:
    age = int(age)
    if age >= 21:
        print("You are good to enter and can drink")
    elif age >= 18:
        print("You can enter but need a wristband")
    else:
        print("You can't come in little one! :(")
else:
    print("Please enter an age")
```

## Loops

Loops let you iterate over a collection of data and perform an action on each item.

#### for loops

`for` loops are written like this:

```python
for item in iterable_object:
    # do something with item
```

Here, `item` is a variable representing the current position of the iterator within the iterable. It will run through every item in the collection and then go away.

#### ranges

`ranges` are a way to generate a sequence of numbers, commonly used in for loops.

```python
times = input("How many times do I have to tell you? ")
times = int(times)
for times in range(times):
    print("CLEAN UP YOUR ROOM!")
```

The third paramter, step, tells your code how many numbers to skip.

- `range(7)` gives you the integers from 0 to 6
- `range(1,8)` gives you the integers from 1 to 7
- `range(1,10,2)` gives you odd integers from 1 to 10
- `range(7, 0, -1)` gives you the integers from 7 to 1

#### while loops

While loops will continue to execute while a condition is truthy.

```python
while im_tired:
    # seek caffeine

user_response = None
while user_response != "please":
    user_response = input("Ah ah ah, you didn't say the magic word: ")
```

The `break` keyword lets you immediately exit out of a loop.

## Lists

A list is a collection of values in an ordered sequence. (It's an array)

The `len` function gives you the length of a list.

```python
tasks = ["Install Python", "Learn about lists", "Take a break"]
len(tasks) # 3
```

You can turn a range into a list using `list`.

```python
tasks = list(range(1,4)) # [1,2,3]
```

Like ranges, lists are zero-indexed. You can use a negative number to index backwards (-1 will give you the list item).

### Iterating over lists

The syntax for iterating over a list with a for loop is very simple.

```python
colors = ["purple", "teal", "magenta"]

for color in colors:
    print(color)
```

With a while loop, it's:

```python
numbers = [1,2,3,4]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
```

### List methods

`append` adds one item to the end of a list.

```python
nums = [1,2,3]
nums.append(4) # [1,2,3,4]
```

`extend` adds all of the values you pass it to the end of a list

```python
nums = [1,2,3,4]
nums.append([5,6,7]) # [1,2,3,4,5,6,7]
```

`insert` inserts an item at a given index in a list

```python
todos = ["clean house", "exercise", "call family"]
todos.insert(2, "take out bins")
# ["clean house", "exercise", "take out bins", "call family"]
```

`clear` removes all items from a list

```python
nums = [1,2,3]
nums.clear() # []
```

`pop` removes the item at a given index and returns it. If you don't specify an index, `pop` removes and returns the last item in the list.

```python
nums = [1,2,3,4]
nums.pop() # 4
nums.pop(1) # 2
```

`remove` removes the first item that matches a specified value. It will throw a ValueError if the item is not found.

```python
nums = [1,2,3,4,4,4,5]
nums.remove(2) # [1,3,4]
nums.remove(4) # [1,3,4,4,5]
```

`index` returns the index of a specified item in a list. You can specify a start and end point.

```python
nums = [5,6,7,8]
nums.index(6) # 1

nums2 = [5,5,6,7,5,8,8,9,10]
nums2.index(5,1) # 1
nums2.index(8,6,8) # 6
```

`count` returns the number of times a specified value occurs in a list

```python
nums = [1,2,3,4,3,2,5,6,7,8,9,10,2]
nums.count(2) # 3
nums.count(3) # 2
```

`reverse` will reverse the elements of a list (in-place)

```python
nums = [1,2,3,4]
nums.reverse() # [4,3,2,1]
```

`sort` sorts the items of a list (in-place)

```python
nums = [4,1,2,5,3]
nums.sort() # [1,2,3,4,5]
```

`join` (technically a string method) takes an iterable as an argument, concatenates a copy of the base string between each item of the iterable, and returns a new string.

```python
words = ["Python", "is", "fun"]
" ".join(words) # "Python is fun"
```

### Slices

Slices copy part or all of a list and makes a new list.

```python
some_list[start:end:step]
```

If you enter a negative number, it will start the slice that many indices from the end.

The end parameter uses exclusive counting. Negative numbers tell you how many items to exclude from the end.

The step gives you the interval to skip. When the step is a negative number, reverse the order.

```python
first_list[1,2,3,4]
first_list[1:] # [2,3,4]
first_list[3:] # [4]
first_list[-1:] # [4]
first_list[:2] # [1,2]
first_list[1:3] # [2,3]
first_list[1:-1] # [2,3]
first_list[::2] # [1,3]
first_list[1::-1] # [2,1]
```

Slices can reverse a list or string.

```python
string = "This is fun!"
string[::-1]
```

Slices let you modify specific portions of a list.

```python
nums = [1,2,3,4,5]
nums[1:3] = ["a","b","c"] # [1,"a","b","c",4,5]
```
