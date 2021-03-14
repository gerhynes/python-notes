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
a = [1, 2, 3]
b = [1, 2, 3]
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
tasks = list(range(1,4)) # [1, 2, 3]
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
numbers = [1, 2, 3, 4]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
```

### List methods

`append` adds one item to the end of a list.

```python
nums = [1, 2, 3]
nums.append(4) # [1, 2, 3, 4]
```

`extend` adds all of the values you pass it to the end of a list.

```python
nums = [1, 2, 3, 4]
nums.append([5, 6, 7]) # [1, 2, 3, 4, 5, 6, 7]
```

`insert` inserts an item at a given index in a list.

```python
todos = ["clean house", "exercise", "call family"]
todos.insert(2, "take out bins")
# ["clean house", "exercise", "take out bins", "call family"]
```

`clear` removes all items from a list.

```python
nums = [1, 2, 3]
nums.clear() # []
```

`pop` removes the item at a given index and returns it. If you don't specify an index, `pop` removes and returns the last item in the list.

```python
nums = [1, 2, 3, 4]
nums.pop() # 4
nums.pop(1) # 2
```

`remove` removes the first item that matches a specified value. It will throw a ValueError if the item is not found.

```python
nums = [1, 2, 3, 4, 4, 4, 5]
nums.remove(2) # [1, 3, 4]
nums.remove(4) # [1, 3, 4, 4, 5]
```

`index` returns the index of a specified item in a list. You can specify a start and end point.

```python
nums = [5, 6, 7, 8]
nums.index(6) # 1

nums2 = [5, 5, 6, 7, 5, 8, 8, 9, 10]
nums2.index(5,1) # 1
nums2.index(8,6,8) # 6
```

`count` returns the number of times a specified value occurs in a list.

```python
nums = [1, 2, 3, 4, 3, 2, 5, 6, 7, 8, 9, 10, 2]
nums.count(2) # 3
nums.count(3) # 2
```

`reverse` will reverse the elements of a list (in-place).

```python
nums = [1, 2, 3, 4]
nums.reverse() # [4, 3, 2, 1]
```

`sort` sorts the items of a list (in-place).

```python
nums = [4, 1, 2, 5, 3]
nums.sort() # [1, 2, 3, 4, 5]
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
first_list[1, 2, 3, 4]
first_list[1:] # [2, 3, 4]
first_list[3:] # [4]
first_list[-1:] # [4]
first_list[:2] # [1, 2]
first_list[1:3] # [2, 3]
first_list[1:-1] # [2, 3]
first_list[::2] # [1, 3]
first_list[1::-1] # [2, 1]
```

Slices can reverse a list or string.

```python
string = "This is fun!"
string[::-1]
```

Slices let you modify specific portions of a list.

```python
nums = [1, 2, 3, 4, 5]
nums[1:3] = ["a", "b", "c"] # [1, "a", "b", "c", 4, 5]
```

#### Swapping values

You can swap values in a list, for example if you want to shuffle or sort the list.

```python
names = ["James", "Michelle"]
names[0], names[1] = names[1], names[0]
print(names) # ["Michelle", "James"]
```

## List Comprehension

List comprehension lets you take an existing list and output another list with different values but based on the first list.

The syntax is:

```python
[___ for ___ in ___]
```

For example:

```python
nums = [1, 2, 3]
[x*10 for x in nums] # [10, 20, 30]
```

You can use list comprehension to manipulate strings and ranges too.

```python
name = "lisa"
[char.upper() for char in name] # ["L", "I", "S", "A"]

[num*10 for num in range(1,6)] # [10, 20, 30, 40, 50, 60]
```

List comprehension can be a concise way to covert one data type into another.

```python
numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers] # ["1", "2", "3", "4", "5"]
```

### List Comprehension with Conditional Logic

You can combine list comprehension with conditional logic.

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
```

```python
numbers = [1, 2, 3, 4, 5, 6]
[num*2 if num % 2 == 0 else num/2 for num in numbers]
# [0.5, 4, 1.5, 8, 2.5, 12]
```

### Nested Lists (multidimensional lists)

Lists can contain any other kind of element, even other lists.

Nested lists are used in a variety of scenarios:

- complex data structures - matrices
- rows and columns for visualizations, tabulations and grouping data
- mazes, game boards

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list[0][1] # 2
nested_list[1][-1] # 6
```

You can use nested loops to output values from nested lists.

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for el in nested_list:
    for val in el:
        print(val)
```

You can also use list comprehension.

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[print(val) for val in el] for el in nested_list]
```

## Dictionaries

A dictionary is a data structure that consists of key value pairs. The keys describe the data, the values represent the data.

You can create a dictionary by assigning it directly to a variable, or by using the `dict` function.

```python
dog = {
    "name": "Buddy",
    "is_cute": True
}

cat = dict(name="Pangur Ban", age=4)
```

### Accessing Data in Dictionaries

Like with lists, you can access a dictionary's values using [].

```python
instructor = {"name": "Colt"}
instructor["name"] # Colt
```

### Iterating Over Dictionaries

The `values` method gives you an iterable collection of a dictionary's values `dict_values` that you can then run through with a for loop.

The `keys` method does the same thing for the dictionary's keys, creating `dict_keys`.

```python
instructor = {
    "name": "Colt",
    "courses": 6,
    "effective": True
}
for value in instructor.values():
    print(value)

for key in instructor.keys():
    print(key)
```

The `ìtems` method gives you both as `dict_items`.

```python
instructor = {
    "name": "Colt",
    "courses": 6,
    "effective": True
}
for key,value in instructor.items():
    print(key,value)
```

You can use `in` to check if a key is in a dictionary.

```python
"phone" in instructor # False
```

To check for a value, you can use `in` and the `values` method.

```python
"Colt" in instructor.values() # True
```

### Dictionary Methods

`clear` will clear all the kays and values in a distionary.

`copy` will make a copy of a dictionary.

```python
d = {
    "a":1,
    "b":2,
    "c":3
}
c = d.copy()
c == d # True
c is d # False
```

`fromkeys` generates key-value pairs from comma seperated values. It can be used to generate default values.

```python
{}.fromkeys(["name", "bio"], "") # {"name": "", "bio": ""}
```

`get` retrieves a key in an objetc and returns None instead of KeyError if the key doesn't exist.

```python
d = dict(a=1,b=2,c=3)
d["a"] # 1
d.get("a") # 1
d["no_key"] # KeyError
d.get("no_key") # None
```

`pop` takes a single argument corresponding to a key and removes that key-value pair from the dictionary. It returns the value corresponding to the key that was removed.

```python
d = dict(a=1,b=2,c=3)
d.pop() # TypeError
d.pop("a") # 1
d = {"b":2, "c":3}
d.pop("e") # KeyError
```

`popitem` removes a random key in a dictionary.

```python
d = dict(a=1,b=2,c=3,d=4,e=5)
d.popitem() # ("d", 4)
d.popitem("a") # TypeError
```

`update` updates the keys and values in a dictionary with another set of key value pairs. It adds keys and values that aren't there and overwrites the ones that are.

```python
first = dict(a=1,b=2,c=3)
second = {}
second.update(first)
second # {"a":1, "b":2, "c":3}
```

### Dictionary Comprehension

The syntax for a dictionary comprehension is similar to a list comprehension.

```python
{___:___for___in___}
```

It will iterate over keys by default. Use `.items()` to iterate over keys and values.

```python
numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
squared_numbers # {"first": 1, "second": 4, "third": 9}
```

You can use a dictionary comprehension to create a dictionary from another data structure.

```python
{num: num ** 2 for num in [1, 2, 3, 4, 5]}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

num_list = [1, 2, 3, 4]
{num:("even" if num % 2 == 0 else "odd") for num in Num_list}
# {1: "odd", 2: "even", 3: "odd", 4: "even"}
```

## Tuples and Sets

### Tuples

A tuple is an ordered collection or grouping of items, and it is immutable. It's an unchanging way of storing ordered data.

```python
numbers = (1, 2, 3, 4)
```

- Tuples are faster than lists.

- Tuples can make your code safer.

- Tuples can be used as valid keys in a dictionary.

Calling `.items()` on a dictionary will return a list of tuples.

You can create a tuple with `()` of the `tuple` function.

You can access a tuple's values using `[]`.

```python
first_tuple = (1, 2, 3, 3, 3)
first_tuple[1] # 2

second_tuple = tuple(5, 1, 2)
second_tuple[0] # 5
```

You can use a tuple as a key in a dictionary (where you couldn't use a list).

```python
locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office"
}
```

### Tuple Methods and Looping

You can use a for loop on a tuple, just like a list.

```python
names = ("Colt", "Blue", "Rusty")
for name in names:
    print(name)
```

The `count` method returns the number of times a value is in a tuple.

```python
x = (1, 2, 3, 3, 3)
x.count(3) # 3
```

The `index` method retuns the first index at which a value is found in a tuple.

```python
x = (1, 2, 3, 3, 3)
t.index(1) # 0
t.index(3) # 2
```

### Sets

Sets are like formal mathematical sets.

Sets are a collection of unordered data that do not have duplicate values.

You can't access items in a set by index.

You can create a set using `{}` or the `set` function.

```python
first_set = set({1, 2, 2, 3, 4, 5, 5}) # {1, 2, 3, 4, 5}
second_set = {1, 4, 5}
4 in first_set # True
```

Converting a list to a set can be useful if you want to distill it down to unique values or check how many unique values it has.

```python
cities = ["Los Angeles", "London", "Florence", "London", "San Francisco", "Tokyo", "San Fransisco"]
list(set(cities)) # ["Los Angeles", "London", "Florence", "San Francisco", "Tokyo"]
```

### Set Methods

`add` adds an item to a set. If the element is already in the set, the set doesn't change.

```python
s = set([1, 2, 3])
s.add(4) # {1, 2, 3, 4}
```

`remove` removes a value from a set. It returns a KeyError if the value is not found. `discard` does the same thing but doesn't cayuse a KeyError.

```python
set1 = {1, 2, 3, 4, 5, 6}
set1.remove(3)
set1 # {1, 2, 4, 5, 6}
set1.discard(3)
```

`copy` creates a copy of a set.

```python
s = set([1, 2, 3])
another_set = s.copy()
another_set # {1, 2, 3}
another_set is s # False
```

`clear` removes all the contens of a set.

```python
s = set([1, 2, 3])
s.clear()
s # set()
```

#### Set Math

Sets have several mathematical methods. For example, `intersection`, `symmetric_difference`, `union`.

```python
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesult", "Oliver", "James"}
math_students | biology_students # union
# {"Charlotte", "Prashant", "Jane", "James", "Oliver", "Mesult", "Helen", "Aparna", "Matthew"}
math_students & biology_students # intersection
# {"James", "Matthew"}
```

### Set Comprehension

Set comprehension can be useful when converting other data types to a set.

The syntax for a set comprehension is similar to a dictionary comprehension but you don't include both a key and value.

```python
{x**2 for x in range(10)}
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
```

For example, this function checks if a string contains all 5 vowels.

```python
def are_all_vowels_in_string(string):
    return len({char for char in string if char in "aeiou"}) == 5
```

## Functions

Functions are packages of code that you can call at any point. They can accept an input and return an output.

Functions help your code to stay dry and logically organized. They are also useful for abstracting away code.

The syntax is:

```python
def name_of_function():
    # block of reusable code
```

The `return` keyword exits the function, outputs whatever is placed after the return keyword, and pops the function off the call stack.

Parameters are the values passed to a function. You can call them anything but try to give them descriptive names.

```python
def square(num):
    return num * num

def print_full_name(first_name, last_name):
    return(f"Your full name is {first_name} and {last_name}")
```

- Parameters refer to the variable in a method definition.
- When a method is called, the arguments are the data you pass into the method's parameters.
- Parameters are the variables in the declaration of a function.
- Arguments are the actual value of the variables that get passed to the function.

```python
def sing_happy_birthday(name):
    # Print song lyrics with name

sing_happy_birthday("Nicholas")
```

#### Common Mistakes When Returning

Be careful with indentation or you may return too soon.

```python
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
        return num

print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7])) # 1

def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return num

print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7])) # 16
```

#### Default Parameters

You can set default parameters to be used if none are passed in.

They allow you to be more defensive and avoid errors with incorrect parameters.

```python
def exponent(num, power=2):
    return num ** power

exponent(2,3) # 8
exponent(7) # 49
```

Default parameters can be anything - functions, lists, dictionaries, strings, Booleans.

```python
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def math(a,b, fn=add):
    return fn(a,b)

math(2,2) # 4
math(2,2, subtract) # 0
```

#### Keyword Arguments

Keyword arguments let you specify which argument corresponds to whcih parameter if you know that name of the parameters. Order doesn't matter.

This makes functions more flexible and becomes important when passing a dictionary to a function.

```python
def full_name(first, last):
    return f"Your name is {first} {last}"

full_name(first="Colt", last="Steele") # Your name is Colt Steele
full_name(last="Steele", first="Colt") # Your name is Colt Steele
```

When you define a function and use an `=` you are setting a default parameter.

When you invoke a function and use an `=` you are making a keyword argument.
