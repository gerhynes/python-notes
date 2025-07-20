# Python Notes

Python is one of the most popular and flexible programming languages, used for everything from basic scripting to machine learning.

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

In Python division returns a float by default if applicable: `1/2` returns `0.5`.

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

`None` is Python's version of `null`, representing nothingness.

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

Keyword arguments let you specify which argument corresponds to which parameter if you know that name of the parameters. Order doesn't matter.

This makes functions more flexible and becomes important when passing a dictionary to a function.

```python
def full_name(first, last):
    return f"Your name is {first} {last}"

full_name(first="Colt", last="Steele") # Your name is Colt Steele
full_name(last="Steele", first="Colt") # Your name is Colt Steele
```

When you define a function and use an `=` you are setting a default parameter.

When you invoke a function and use an `=` you are making a keyword argument.

### Scope

Scope governs where variables can be accessed.

Variables created in functions are scoped to that function.

```python
def say_hello():
    instructor = "Colt"
    return f"Hello {instructor}"

say_hello() # Hello Colt
print(instructor) # NameError
```

When you reference a global variable inside a function, the function assumes there is a local variable scoped to that function and will throw an error if you try to mutate the variable.

The `global` keyword lets you reference variables that were originally assigned in the global scope.

```python
total = 0

def increment():
    total += 1
    return total

def decrement():
    global total
    total -= 1
    return total

increment() # Error - local variable referenced before assignment
decrement() # -1
```

The `nonlocal` keyword lets you modify a parent's variable in a child (nested) function.

```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()
```

### Documenting Functions

When writing complex function, Python uses `""" """` to document what the function does.

```python
def say_hello():
    """A simple function that returns the string hello"""
    return "Hello"

say_hello.__doc__ # 'A simple function that returns the string hello'
```

### \*args

`*args` is a special operator you can pass to a function as a parameter. It gathers all remaining arguments as a tuple.

As long as it starts with `*` it can be given other names, for example `*nums`, `*details`.

```python
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

sum_all_nums(4,6,9,4,10) # 33
```

### \*\*kwargs

`**kwargs` (keyword args) is another special operator you can pass to a function. It gathers any remaining keyword arguments as a dictionary.

As long as it starts with `**` you can give it other names, `**extra_stuff`.

```python
def fav_colors(**kwargs):
    print(kwargs)

fav_colors(colt="purple", ruby="red", ethel="teal")
# {"colt": "purple", "ruby": "red", "ethel": "teal"}
```

#### Ordering Parameters

In function declarations, use the following ordering:

1. parameters
2. \*args
3. default parameters
4. \*\*kwargs

### Unpacking Arguments with \*

You can use `*` as an argument to a function to unpack values from lists or tuples.

```python
def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    return total

nums = [1, 2, 3, 4, 5, 6]
sum_all_values(nums) # Error
sum_all_values(*nums) # 21
```

### Unpacking Dictionaries with \*\*

You can use `**` to unpack a dictionary into keyword arguments.

```python
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first":"Colt", "second": "Rusty"}

display_names(names) # Error
display_names(**names) # "Colt says hello to Rusty"
```

### Return Values
You can use a return statement to return multiple values from a function. These will be implicitly converted into a tuple. Write the return values in a comma separated list in the order you want them returned.

```python
def get_coords():
	x = 25.5
	y = 48.2
	return x,y

x, y = get_coords()
```

## Lambdas and Built-in Functions

### Lambdas

Lambdas are short anonymous functions intended to be used one time.

```python
lambda parameters: body of function
```

Lambdas can be stored in variables but are more commonly passed into functions as a parameter.

```python
def square(num): return num * num

square2 = lambda num: num * num

square(9) # 81
square2(9) # 81

scores = [20, 95, 45, 85, 90, 15, 5, 100, 10]
high_scores = filter(lambda:score: score >= 90, scores)

button = tk.Button(frame,
    text="CLICK ME",
    fg="red",
    command=lambda: print("Hello")
)
```

### map

`map` is a standard function that accepts at least two arguments, a function and an iterable.

An iterable is something that can be iterated over (lists, strings, dictionaries, sets, tuples).

`map` runs a lambda for each value in the iterable and returns a map object which can be converted into another data structure.

```python
lst = [1, 2, 3, 4]

doubles = list(map(lambda X: x*2, lst)) # [2, 4, 6, 8]

names = [
    {"first": "Colt", "last":"Steele"},
    {"first": "Rusty", "last":"Steele"},
    {"first": "Blue", "last":"Steele"},
]

first_names = list(map(lambda x: x["first"], names))
# ["Colt", "Rusty", "Blue"]
```

### filter

`filter` allows you to take a collection and filter out desired items.

`filter` calls a lambda for each value in the iterable. It returns a filter object which can be converted into another iterable. The object contains only the values that returned True to the lambda.

```python
lst = [1, 2, 3, 4]
evens = list(filter(lambda num: num % 2 == 0, lst)) # [2, 4]
```

You can combine `filter` and `map`:

```python
names = ["Laurie", "Colt", "Rusty"]
list(map(lambda name: f"Your instructor is {name}",
    filter(lambda value: len(value) < 5, name)))
# ["Your instructor is Colt"]
```

If you can use list comprehension to do the same thing, you probably should.

```python
[f"Your instructor is {name}" for name in name if len(name) < 5]
```

### all

`all` returns True if all elements of the iterable passed in are truthy (or if the iterable is empty).

```python
all([0, 1, 2, 3]) # False
all([char for char in "eio" if char in "aeiou"]) # True
all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]) # True
```

### any

`any` returns True if any element of the iterable is truthy. If the iterable is empty, it returns False.

```python
nums = [2, 60, 26, 18, 21]
any([num % 2 == 1 for num in nums]) # True
```

### Generator Expressions

If all you're doing is iterating once and you don't need to store and use the generated results, you can use a generator expression in place of a list comprehension. It's more lightweight in terms of memory.

```python
import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)]) # 9024 bytes
gen_exp = sys.getsizeof(x * 10 for x in range(1000)) # 88 bytes
```

### sorted

`sorted` returns a new sorted list from the items in an iterable. It doesn't change the original iterable.

```python
more_nums = [6, 1, 8, 2]
sorted(more_nums) # [1, 2, 6, 8]
```

You can sort in descending order by including `reverse=True`

```python
more_nums = [6, 1, 8, 2]
sorted(more_nums, reverse=True) # [8 , 6, 2, 1]
```

You can use `sorted` with dictionaries by using `key` to specify what to sort by.

```python
users = [
    {"name": "Katie", "tweets": ["I make ceramics", "We put another rover on Mars"]},
    {"name": "Colt", "tweets": ["I love cats"]},
    {"name": "Rusty", "tweets": [], "id": 1234, "pro": True },
]
sorted(users, key=lambda user: user["name"])
sorted(users, key=lambda user: len(user["tweets"]))
```

### max

`max` returns the largest item in an iterable or the largest of two or more arguments. You can specify how things are sorted using `key`.

```python
max(3, 67, 99) # 99
max("hello world") # "w"

names = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]
max(names) # Tim - alphabetical
max(names, key=lambda n: len(n)) # Ollivander - length
```

### min

`min` returns the smallest item in an iterable or the smallest of two or more arguments.

```python
min((36, 21, 7)) # 7

song = {
    {"title": "Happy Birthday", "playcount": 1},
    {"title": "I Will Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31},
}
min(songs, key=lambda song: song["playcount"])
```

### reversed

`reversed` returns a reversed iterator (works with other structures than lists). You'd use it if you were iterating over something in reverse.

```python
for x in reversed(range(0, 10)):
    print(x)
```

### len

`len` returns the length (number of items) of an object. The argument may be a sequence (such as a string, tuple, list or range) or a collection (such as a dictionary or set).

```python
len("asdasdas") # 8
len({}) # 0
```

Each object has a built in method `__len__()` which is called when you use `len`.

### abs

`abs` returns the absolute value of a number. The argument may be an integer or float.

```python
abs(-5) # 5
abs(5.44) # 5.44
```

### sum

`sum` takes an iterable and an optional start (by default 0). It returns the sum of the start and the items of the iterable from left to right.

```python
sum([1,2,3]) # 6
sum([1,2,3], 10) # 16
```

### round

`round` returns a number rounded to `ndigits` after the decimal point. If `ndigits` is ommitted or is `None`, it returns the nearest integer to the input.

```python
round(10.2) # 10
round(1.212121, 2) # 1.21
```

### zip

`zip` makes an iterator that aggregates elements from each of the provided iterables.

It returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the provided iterables.

The iterator stops when the shortest input iterable is exhausted.

```python
first_zip = zip([1, 2, 3], [4, 5, 6])
list(first_zip) # [(1, 4), (2, 5), (3, 6)]
dict(first_zip) # {1: 4, 2: 5, 3: 6}
```

You can use `*` to unpack a list of tuples before zipping them. This becomes useful when working with more complex data structures.

```python
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4,5)]
list(zip(*five_by_two))
# [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]
```

```python
midterms = [88, 91, 78]
finals = [98, 89, 73]
students = ["kate", "ang", "dan"]

# zip + dictionary comprehension
final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
# {"kate": 98, "ang": 91, "dan":78}

# zip + lambda
grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)
# {"kate": 98, "ang": 91, "dan":78}
```

## Debugging and Error Handling

`SyntaxError` occurs when Python encounters something it can't parse. Usually due to typos.

`NameError` occurs when a variable hasn't been assigned yet.

`TypeError` occurs when an operation or function is applied to the wrong type.

`IndexError` occurs when you try to access an element in a list using an invalid index (one outside it's range).

`ValueError` occurs when a built-in operation or function receives an argument that has the right type but an inappropriate value, for example `int("abcd")`.

`KeyError` occurs when a dictionary does not have a specific key.

`AttributeError` occurs when a variable does not have an attribute, for example `[1, 2, 3].greet()`.

### Raising Errors

You can deliberately raise specific errors using the `raise` keyword.

```python
def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) != str:
        raise TypeError("text must be instance of str")
    if type(color) != str:
        raise TypeError("color must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")
```

### Try and Except Blocks

In Python you're strongly encouraged to use try/except blocks to catch and handle exceptions.

You don't want to catch all errors with a blank except. You need to correctly identify what went wrong.

```python
def getKey(d, key):
    try:
        return d[key]
    except KeyError:
        return None
```

`try` will attempt to do something. If there's a problem `except` will run. If there's not a problem `else` runs. No matter what, `finally` runs.

```python
while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That's not a number")
    else:
        print("Good job, you entered a number")
        break
    finally:
        print("Runs no mattter what")
print("The rest of the logic runs")
```

If you want the error itself, you can access it using `as`

```python
def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Please don't divide by zero")
    except TypeError as err:
        print("arguments must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")
```

### Debugging with pdb

`pdb` is a module that lets you set breakpoints in your code, check values, and step through your code.

```python
import pdb; pdb.set_trace()
```

```python
import pdb
first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)
```

Common pdb commands include:

- l - list
- n - next line
- p - print
- c - continue, finishes debugging

## Modules

Modules help keep your files small and reuse code across files.

```python
import random

random.choice(["apple", "banana", "cherry", "durian"])
random.shuffle(["apple", "banana", "cherry", "durian"])
```

You can alias a module when importing it.

```python
import random as omg_so_random

omg_so_random.choice(["apple", "banana", "cherry", "durian"])
```

The keyword `from` lets you import only the parts of a module that you need.

```python
from random import randint, choice

from random import * # makes everything available in the namespace
```

### Custom Modules

You can import code from one of your Python files into another file. This is helpful for keeping things organized and reusable.

```python
# file1
def fn():
    return "Do something"

def other_fn():
    return "Do the other thing"

# file2
import file1

file1.fn()
file1.other_fn()
```

### External Modules

External modules can be downloaded using pip, Python's package manager. These modules can be found via [PyPi](https://pypi.org/), the Python package index.

```python
python3 -m pip install NAME_OF_PACKAGE
```

```python
from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan")
    if color not in valid_colors:
        color = "magenta"
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)

msg = input("What would you like to print? ")
color = input("What color? ")
print_art(msg, color)
```

### Virtual Environments

A Python virtual environment is a folder structure that lets you run an isolated, lightweight Python installation with its own packages. It reproduces the folder structure that a standard Python installation creates while keeping all installed packages isolated to that environment.

The main reasons to use virtual environments is to avoid dependency conflicts and avoid global namespace pollution.

Different projects might require different versions of external libraries. If everything is installed globally, then you cannot work with two versions of the same library.

 Linux and MacOS come with a version of Python pre-installed that the OS uses for internal tasks. Globally installed packages can interfere with this. Also, OS updates can overwrite globally installed packages.

There are multiple ways to create a virtual environment but the `venv` module comes installed with Python.

To create a virtual environment in a directory, run:

```shell
python3 -m venv <VENV_NAME>
```

`.venv` is a popular name for virtual environments.

You need to activate the virtual environment to be able to use it.

```shell
source .venv/bin/activate
(.venv) $
```


You can then install packages into just the virtual environment.

```shell
(.venv) $ python3 -m pip install <PACKAGE_NAME>
```

When you are finished working in a virtual environment  you deactivate it.

```shell
(.venv) $ deactivate
$
```

### Replicating Virtual Environments

If you have a project the locally uses a virtual environment, anyone else trying to work on it on their machine would need to replicate the virtual environment.

You don't commit your virtual environment to version control or ship it with your project.

You can create a list of all the dependencies for a project, and their versions, by creating a `requirements.txt` file.

```shell
python3 -m pip freeze > requirements.txt
```

To install all the dependencies from a project that was created in a virtual environment, activate the virtual environment that you want to work in and run:

```shell
python3 -m pip install -r requirements.txt
```

When working with virtual environments, if you get a warning that pip is out of date

```shell
(.venv) $ python -m pip install --upgrade pip
```
### Python Standard Library

The Python Standard Library is a collection of modules that comes with every Python installation.

The standard library includes modules for working with different data types, the filesystem, the operating system, networking, GUIs, etc.

```python
import random

def main():
	number = random.randInt(1,1000)

	numbers = [1,2,3,4,5,6,7]
	random.shuffle(numbers)

	return

if __name__ == "__main__":
	main()

```

### autopep8

The autopep8 package will automatically format your Python code to conform to the pep8 styleguide.

You can set autopep8 to be more or less aggressive in its formatting.

```
autopep8 --in-place --aggressive --aggressive <filename>
```

For example, `-a`or `--aggressive` enables non-whitespace changes; multiple `-a` result in more aggressive changes

### The `__name__` Variable

When run, every Python file has a `__name__` variable.

If the file is the main file being run, its value is **main**. Otherwise, its value is the file name, for example if the file is being imported into another file.

When you use `import`, Python:

1. Tries to find the module (if it fails it throws an error), that is a `.py` file with the same name as `__name__`.
2. Runs the code inside the module being imported.

You can tell Python to not run certain lines on import and only run them when the file is run directly as a script by checking if `__name__` is `__main__`:

```python

def main:
	# do something

if __name__ == "__main__":
    # this code will only run
    # if the file is the main file being run
    main()
```

## Making HTTP Requests with Python

When you enter a url into your browser, the folowing steps happen:

1. DNS lookup turns the url into an IP address
2. Your computer makes a REQUEST to a server
3. The server processes the REQUEST
4. The server issues a RESPONSE.

This is the Request/Response cycle.

DNS lookup connects domain names and IP addresses through a DNS server.

HTTP headers are sent with both requests and responses. They provide additional information about the request or response.

- `Accept` - Acceptable content-types for response (for example, html, json, xml)
- `Cache-Control` - Specify caching behaviour
- `User-Agent` - Contains information about the software used to make the request
- `Access-Control-Allow-Origin` - Specify domains that can make requests
- `Allowed` - HTTP verbs that are allowed in requests

Response Status Codes

- 2xx - Success
- 3xx - Redirect
- 4xx - Client Error (your fault)
- 5xx - Server Error (not your fault)

### HTTP Verbs

`GET` Requests

- Used for retrieving data
- Data passed in a query string
- Should have no side-effects
- Can be cached
- Can be bookmarked

`POST` Requests

- Used for writing data
- Data passed in request body
- Can have side-effects
- Not cached
- Can't be bookmarked

### APIs

An API can be thought of as the version of a website intended for computers rather than humans.

APIs allow you to get data from another application without needing to understand how that application works.

Often, they can send the data back in different formats, such as json or xml.

### requests

The requests module lets you make http requests using Python. It's useful for web scraping/crawling and grabbing data from APIs.

### Requesting json

You can use request headers to specify the format you want to receive data in from an API.

```python
import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()

print(data["joke"])
```

When you make a json request, it comes back as one giant string. You need to use the `json` method to turn it into a Python dictionary.

### Sending Requests with Params

A query string is a way to pass data to a server as part of a GET request: `http://www.example.com/?key1=value1&key2=value2`

The params are the kay value pairs you include in it.

```python
import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}
)

data = response.json()
print(data["results"])
```

### POST Requests

You can make POST requests by providing the url and data in the form of JSON.

```python
def save_post(data):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.post(url, json=data)
    parsed_data = response.json()

    return parsed_data
```

### Handling Errors

An API may not raise an error, for example, if a resource doesn't exist. The requests module provides a function, `raisefor_status`, that will manually raise an error if the response's status code indicates an error (4xx, 5xx).

requests also provide error types that can be checked for, such as `requests.exceptions.HTTPError` for status codes in the 400 and 500 range, or `requests.exceptions.RequestException` if the request timed out.

```python
def get_resource():
    url = "https://jsonplaceholder.typicode.com/xyz"

    try:
        response = requests.get(url)
        response.raise_for_status()
        parsed_data = response.json()
        return parsed_data

    except requests.exceptions.HTTPError as error:
        print(f"There was a HTTP error: {error}")
    except requests.exceptions.RequestException as error:
        print(f"There was an error: {error}")

```

## Object Oriented Programming

OOP is a method of programming that attempts to model some process or thing in the world as a **class** or **object**.

**class** - a blueprint for objects. Classes can contain methods (functions) and attributes (similar to keys in a dict)

**instance** - objects that are constructed from a class blueprint that contain their class's methods and properties.

With OOP, your goal is to encapsulate your code into **logical, hierarchical groupings using classes** so that you can reason about your code at a higher level.

Say you want to model a game of poker. You could have the following entities:

- Game
- Player
- Card
- Deck
- Hand
- Chip
- Bet

A hyptehtical Deck class might have the following attributes and methods:

- \_cards (private list attribute)
- \_max_cards (private list attribute)
- shuffle (public method)
- deal_card (public method)
- deal_hand (public method)
- count (public method)

Some things don't need to be exposed to the outside world, they can be accessed through methods.

Unlike with Java, in Python there isn't a true distinction between public and private but good code follows the convention of designating some things as private.

**encapsulation** - the grouping of public and private atrributes and methods ito a programmatic class, making **abstraction** possible.

**abstraction** - exposing only "relevant" data in a class interface, hiding private attributes and methods (aka the "inner workings") from users.

### Creating Classes and Instances

Classes in Python can have a special `__init__` method, which gets called every time you create (instantiate) an instance of the class. This initializes the data in the instance.

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Vehicle("Ford", "Fiesta", "2012")
car2 = Vehicle("Honda", "Civic", "2014")
```

Creating an object that is an instance of a class is called **instantiating** a class.

The `self` keyword refers to the specific instance of the class you're working with. `self` must always be the first parameter to `__init__` and to any methods and properties you define on class instances.

### Underscores and Names

```python
class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi"
        self.__msg = "Turtles all the way down"

p = Person()
```

Dunder methods, like `__init__`, are built into Python. You generally don't define your own.

Private methods and attributes, not intended for use outside of a class, are conventionally written with a leading underscore `self._secret`.

When you put double underscores before the name of a method or attribute, Python "mangles" the name of that attribute, making it particular to that class. For example, `self.__msg` becomes `_Person__msg`

### Instance Attributes and Methods

Classes are not just storage places for information, they also have functionality.

`self` is necessary for all methods, even if you aren't using it.

```python
class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age} birthday, {self.first}"

user1 = User("Joe", "Woods", 35)
user2 = User("Bianca", "Lopez", 38)
```

### Class Attributes

If an instance attribute is defined on each individual instance of a class, a class attribute is defined once and lives on the class itself. It is shared by all instances of the class and by the class itself.

```python
class User:

    active_users = 0 # <-- class attribute

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

user1 = User("Joe", "Woods", 35)
user2 = User("Bianca", "Lopez", 38)
print(User.active_users) # 2
```

```python
class Pet:

    allowed = ["cat", "dog", "fish", "rodent"]

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet!")
        self.species = species
```

You can refer to a class attribute with `Pet.allowed` or `self.allowed`, as long as you're just accessing and not updating the value. Using the class name is more conventional.

### Class Methods

Class methods are methods (with the `@classmethod` decorator) that are not concerned with instances, but with the class itself (often passed into the class method as `cls`).

One use for a class methid is if you need to pass in data in one format and convert it to another before `__init__` is called.

```python
class User:
    # ...

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

User.display_active_users()
tom = User.from_string("Tom,Jones,79")
```

### Static Methods

Static methods are similar to class level methods but are bound to the class itself rather than instances of the class. 

A static method can be called without an object for that class.

Static methods cannot modify the state of an object as they are not bound to it.

Static methods can be denoted using the `@staticmethod` decorator.

Static methods don't need `self` to be passed as the first argument.

```python
class User:
	...
	
	@staticmethod
	def validate_email(email):
		# validation logic


User.validate_email("leo@example.com")
```

### String Representation

The `__repr__` method is one of several ways to provide a nicer string representation of a class. When you print a class or turn a class into a string, `__repr__` is called behind the scenes.

`__repr__` is what allows a list, for example, to be printed as `[]`.

```python
class Human:

    def __init__(self, name="somebody"):
        self.name = name

    def __repr__(self):
        return self.name

fella = Human()
print(fella) # "somebody"
colt = Human(name="Colt Steele")
print(f"{colt} is totally rad (probably)")
# "Colt Steele is totally rad (probably)"
```

There are also several other dunders to return classes in string formats (`__str__`, `__format__`) and choosing one is a bit complicated.

### Inheritance

A key feature of OOP is the ability to define a class which inherits from another class (a "base" or "parent" class).

In Python, inheritance works by passing the parent class as an argument to the definition of a child class.

```python
class Animal:
	...
    def make_sound(self, sound):
        print(sound)

class Cat(Animal):
    pass

tivaldo = Cat()
tivaldo.make_sound("meow") # "meow"	
```

### Properties

Without having private methods or attributes, Python relies on the following conventions. Properties let you approximate private methods and attributes.

```python
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be a negative")
```

### Super

When initialising a child class, `super` lets you reduce duplication. `super` will refer to the parent class and automatically pass in `self` as the first argument.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(sound)

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

blue = Cat("Blue", "Scottish Fold", "String")
blue.play() # Blue plays with String
```

### Multiple Inheritance

A class can inherit from more than one parent class. It's not super common and a bit controversial.

```python
class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea"

class Ambulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land"

class Penguin(Aquatic, Ambulatory):
    def __init__(self, name):
        super().__init__(name=name)

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")
```

`Penguin` inherits from both `Aquatic` and `Ambulatory`, so instances of Penguin can call both the walk and swim methods.

`Penguin` calls `Aquatic.greet()` instead of `Ambulatory.greet()`.

### Method Resolution Order

Whenever you create a class, Python automatically sets a Method Resolution Order (MRO) for that class, which is the order in which Python will look for methods on instances of that class.

You can programmatically reference the MRO three ways:

- `__mro__` attribute on the class
- use the `mro()` method on the class
- use the built-in `help(cls)` method

### Polymorphism

A key proinciple of OOP is the idea of polymorphism - an object can take on many forms.

Two practical applications of polymorphism are:

1. The same class method works in a similar way for different classes.

A common implementation of this is to have a method in a parent class that is overridden by a subclass (**method overriding**).

Each subclass will have a different implementation of the method.

```python
Cat.speak()
Dog.speak()
Human.speak()
```

2. The same operation works for different kinds of objects.

Python classes have special, "magic", methods, that are dunders. These methods have special names that give instructions to Python for how to deal with objects.

```python
len(sample_list)
len(sample_tuple)
len(sample_string)
```

### Special `__magic__` methods

In the operation `8 + 2` Python knows what to do because the `+` operator is shorthand for a special method `__add__()` that gets called on the first operand.

If the first (left) operand is an instance of `int`, `__add__()` does mathematical addition. If it's a `string`, it does concatenation.

You can delcare special methods on your own classes to mimic the behaviour of built-in objects.

```python
class Human:
    def __init__(self, height):
        self.height = height # in cms

    def __len__(self):
        return self.height

colt = Human(180)
len(colt) # 180
```

A common use case for special methods is to make classes "look pretty" in strings.

By default classes are ugly when printed.

```python
class Human:
    pass

colt = Human()
print(colt) # <__main__.Human at 0x1062b8400>
```

The `__repr__` method is one of several ways to provide a nicer string representation.

```python
class Human:
    def __init__(self, name="somebody"):
        self.name = name

    def __repr__(self):
        return self.name

yer_man = Human()
print(yer_man) # "somebody"
```

## Iterators and Generators

### Iterators

An Iterator is an object that can be iterated upon. It returns data, one element at a time, when `next()` is called on it.

An Iterable is an object whcih will return an Iterator when `iter()` is called on it.

`"hello"` is not an iterator, but it is an iterable.

`iter("hello")` returns an iterator.

When you call a `for` loop on a string, for example, the `for` loop calls `iter()` on it.

When `next()` is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a `StopIteration` error.

```python
# Custom for loop
def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            func(item)

def square(x):
    print(x*x)

my_for("hello", print)
my_for([1, 2, 3], sum)
my_for([1, 2, 3], square)
```

```python
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


for n in Counter(50,55):
    print(n)
```

### Generators

Generators are a subset of iterators.

They can be created with generator functions using the `yield` function or with generator expressions.

| Functions                              | Generator Functions               |
| -------------------------------------- | --------------------------------- |
| uses `return`                          | uses `yield`                      |
| returns once                           | can yield multiple times          |
| when invoked, returns the return value | When invoked, returns a generator |

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
```

```python
def current_beat():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1
```

Generators can be much more memory efficient than using functions with lists, especially when dealing with large sequences.

```python
def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums

fib_list(1000000) # 503 MB

def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count += 1

for n in fib_gen(1000000):
    print(n) # 6.7 MB
```

### Generator Expressions

Generator expressions are a concise syntax for creating generators, comparable to list comprehensions for lists.

```python
# Generator function
def nums():
    for num in range(1,10):
        yield num

# Generator Expression
g = (num for num in range(1,10))
```

Generator expressions can be much more time efficient than list comprehensions.

```python
sum(n for n in range(100000000)) # 6.75 seconds

sum([n for n in range(100000000)]) # 10.47 seconds
```

## Higher Order Functions
Higher order functions can accept other functions as arguments and return functions. 

They can make your code more reusable and modular. A higher order function can be reused without having specific logic tied to it.

There are several higher order functions built into Python, such as `map` and `filter`.

```python
moves = ["punch", "kick", "block", "dodge"]

def power_move(move):
	return f"{move.upper()}!!!"

power_moves = map(power_move, moves)

scores = [20, 95, 45, 85, 90, 15, 55, 100, 10]

def is_high_score(score):
	return score >= 90

high_scores = filter(is_high_score, scores)
```

## Decorators

Decorators are functions that wrap other functions, changing their behaviour.

They have their own syntax, using `@`.

```python
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day")
    return wrapper

@be_polite
def greet():
    print("My name is Matt")

greet() # same as greet = be_polite(greet)
```

Real-world use cases for decorators might include:
- `@require_auth` - check user auth before function conditionally runs
- `@validate_input` - validate function arguments before function runs
- `@preprocess` - modify function arguments to be in a specific format

### Decorator Pattern

Decorated functions can accept arguments using `*args` and `**kwargs`.

```python
def my_decorator(fn):
    def wrapper(*args, **kwargs):
        # do some stuff with fn(*args, **kwargs)
        pass
    return wrapper
```

```python
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs*).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}"

@shout
def order(main, side):
    return f"Hi, I'd like the {main} with a side of {side}, please"
```

### Preserving Metadata

By default, decorated functions don't maintain their metadata. But Python has a module `functools` with a function `wraps` which preserves a function's metadata when it is decorated.

```python
from functools import wraps

def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # do some stuff with fn(*args, **kwargs)
        pass
    return wrapper
```

```python
from functools import wraps

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM A WRAPPER FUNCTION"""
        print(f"You are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x,y):
    """Adds two numbers together"""
    return x + y
```

Decorators can be used to enforce restrictions on arguments.

```python
from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs
            raise ValueError("No kwargs allowed")
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"Hi there, {name}")

greet("Ali") # "Hi there, Ali"
greet(name="Ali") # ValueError
```

Decorators can accept arguments and ensure that an argument is a specific value.

```python
from functools import wraps

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

print(add_to_ten(10,22)) # 12
print(add_to_ten(1,2)) # "First arg needs to be 10"
```

You can also use a decorator to enforce types.

```python
from functools import wraps

def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            # convert args into something mutable
            newargs = []
            for (a,t) in zip (args, types):
                newargs.append(t(a))
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

repeat_msg("hello", "3")
```

### Closures
A closure is a function that remembers values from its enclosing scope even after the enclosing scope has finished execution.

```python
def move_factory(character_name):
    uppercase_name = character_name.upper()

    def print_move(move_name):
        # uppercase_name is available from enclosing scope
        print(f"{uppercase_name} performs {move_name}")
    return print_move

def main():
    ryu_move = move_factory("Ryu")
    ryu_move("Hadouken")

if __name__ == "__main__":
    main()
```


## Testing

Writing tests reduces bugs in existing code, ensures that bugs stay fixed, and ensures that new features don't break old ones, also passing tests is satisfying.

With Test Driven Development:

- development begins by writing tests
- once tests are written, write code to make the tests pass
- once tests pass, a feature is considered complete.

A mantra of TDD is "red, green, refactor".

1. Write a test that fails
2. Write the minimal amount of code to make the test pass
3. Clean up the code, while ensuring that tests still pass

### Assertions

You can make simple assertion statements with the `assert` keyword. `assert` accepts an expression. It returns `None` if the expression is truthy and it raises an `AssertionError` if the expression is falsy. `assert` accepts an optional error message as a second argument.

```python
def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y
```

If a Python file is run with the `-O` flag, assertions will not be evaluated.

There are better options available for testing.

### doctests

You can write tests for functions inside the docstring. But you have to write the code as if it's in a REPL. The syntax is quite finnicky, it clutters up your functions, tests can be brittle, and it lacks many of the features of larger testing tools.

```python
def add(a, b):
    """
    >>> add(2,3)
    5
    >>> add(100,200)
    300
    """
    return a + b
```

To run doctests, use:

```
python3 -m doctest -v name_of_file.py
```

### unittest

Unit testing is the idea of testing the smallest parts of an application in isolation.

Good candidates for unit testing are individual classes, modules, or functions.

Bad candidates for unit testing would be an entire application or dependencies across several classes or modules.

Python comes with a built-in module called `unittest` You write unit tests as classes that inherit from `unittest.TestCase`. This inheritance gives you access to many assertion helpers that let you test the behaviour of your functions.

You run tests by calling `unittest.main()`.

```python
import unittest
from activities import eat, nap

class ActivityTest(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because my body is a temple"
        )
    def test_eat_unhealthy(self):
        """eat should indicate you've given up for unhealthy eating"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO"
        )
    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )
    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(
            nap(3),
            "Ugh, I overslept. I didn't mean to nap for 3 hours"
        )

if __name__ == "__main__":
    unittest.main()
```

You can add comments to tests to make them more informative.

To see comments, run

```
python3 name_of_test_file.py -v
```

### Common Assertions

- `self.assertEqual(x,y)`
- `self.assertNotEqual(x,y)`
- `self.assertTrue(x)`
- `self.assertFalse(x)`
- `self.assertIsNone(x)`
- `self.assertIsNotNone(x)`

### Testing for errors

When testing for errors, `self.assertRaises` lets you test for a specific type of error.

```python
class SomeTests(unittest.TestCase):
    def testing_for_errors(self):
        """testing for an error"""
        with self.assertRaises(IndexError):
            l = [1,2,3]
            l[100]
```

### Before and After Hooks

For larger applications, you may want similar application state before running tests.

`setUp` runs before each test method.

`tearDown` runs after each test method.

Common use cases include: adding/removing data from a test database, creating instances of a class.

```python
class SomeTests(unittest.TestCase):
    def setUp(self):
        # do setup here
        pass

    def test_first(self):
        # setUp runs before
        # tearDown runs after
        pass

    def test_second(self):
        # setUp runs before
        # tearDown runs after
        pass

    def tearDown(self):
        # do teardown here
        pass
```

## File I/O

You can read a file by passing the file to the `open` function.

`open` returns a file object.

You can then read the file object with the `read` method.

```python
file = open("story.txt")
file.read()
```

Python reads files using a cursor (like the one you see when typing). After a file is read, the cursor is at the end of the file. If you call read again on the same file, you'll get an empty string.

You use the `seek` method to move the cursor.

`file.seek(0)` will put the cursor at the start of the file.

The `readline` method will read the specified line and stop at the newline character.

The `readlines` method returns a list of lines.

You can close a file with the `close` method.

You can check if a file is closed using the `closed` attribute.

Once closed, a file can't be read again until you reopen it. Always close files, it frees up system resources.

### `with` Blocks

The `with` statement gives you an alternative syntax for file I/O. Once it's run, the file is automatically closed. Behind the scenes, `__enter__()` and `__exit__()` are called.

```python
file = open("story.txt")
file.read()
file.close()
file.closed # True
```

```python
with open("story.txt") as file:
    file.read()

file.closed # True
```

### Writing to Text Files

You can also use `open` to write to a file.

You need to specify the `w` flag as the second argument.

You don't need to have an existing file to write to. Writing to a non-existing file will create it.

```python
with open("haiku.txt", "w") as file:
    file.write("Writing files is great\n")
    file.write("Here is another line of text\n")
    file.write("Closing now, goodbye!\n")
```

### File Modes

- r - Read a file (no writing) - this is the default
- w - Write to a file (previous content is removed)
- a - Append to the end of a file (previous content is not removed)
- r+ - Read and write to a file (writes based on cursor - starts at beginning, only works with existing files)

### Working with Paths

You can pass a relative path to `open`. That is relative to where the Python script is being called, not where the script file is located.

```python
file = open("sample.txt", "r")
```

Sometimes you will need an absolute path but you don't want to hardcode this or the script won't work on other machines.

The `pathlib` module from the Python standard library lets you construct paths.

You create a new `Path` instance and pass it `__file__` (the full absolute path, including the filename, as a string). 

You can then access properties on this path object, such as `parent` (the absolute path to the file's parent directory).

You can add directories to the path using `/` and make a directory using the `mkdir` method.

`path.write_text()` lets you write text to a file without manually opening it first. `path.read_text()` similarly lets you read a file without manually opening it.
 
```python
from pathlib import Path

def create_path():
	script_dir = Path(__file__).parent

	path = script_dir / "characters"

	# create any parent folders, if needed
	# if directory already exists, don't throw error
	path.mkdir(parents=True, exist_ok=True)

	path = path / "zelda.txt"

	file = path.open("w") # equivalent to file = open(path, "w") 
	file.write("Ganon")
	content = file.read()
	print(content)

	file.close()

	path.write_text("Epona")

	return

def main():
	create_path()

if __name__ == "__main__":
	main()
```

### Handling File Errors

Working with files can cause errors, for example if you try to read a file that doesn't exist you'll get a `FileNotFoundError`.

For this reason you'll want to wrap file operations with a `try` block. Remember to include a catchall error case.

```python
from pathlib import Path

def open_file():
    path = Path(__file__).parent
    path = path / "does" / "not" / "exist"

    try:
        file = path.open("r")
        contents = file.read()
        print(contents)
        file.close()

    except FileNotFoundError:
        print(f"{path} does not exist")

    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    open_file()

if __name__ == "__main__":

    main()
```

### Context Managers

Context managers are a tool to automatically handle the setup and teardown phases when dealing with external resources. 

For example, they allow you to open a file, work with the file, and then the file will automatically close when the work is done.

The `with` statement creates a runtime context that lets you run a group of statements under the control of a context manager.

```python
from pathlib import Path

def open_file():
    path = Path(__file__).parent / "characters.txt"
    characters = ["Mario", "Luigi", "Peach", "Yoshi", "Bowser"]

    # context manager - auto closes
    with path.open("w") as file:
        for character in characters:
            file.write(character + "\n")

def main():
    open_file()

if __name__ == "__main__":
    main()
```

### Working with JSON

Python supports working with JSON through the built-in `json` module, which lets you convert common data types between Python and JSON.

| Python | JSON   |
| ------ | ------ |
| dict   | object |
| list   | array  |
| tuple  | array  |
| str    | string |
| int    | number |
| float  | number |
| True   | true   |
| False  | false  |
| None   | null   |
`json.dump` lets you serialize a Python dictionary into a JSON string.

`json.load` lets you deserialize JSON into Python.

```python
from pathlib import Path
import json

path = Path(__file__).parent / "characters.json"

characters = {
    "characters": [
        {"name": "Mario", "age": 25},
        {"name": "Luigi", "age": 22},
        {"name": "Peach", "age": 26},
        {"name": "Bowser", "age": 35},
    ]
}

def write_json():
    with path.open("w") as file:
	    # data to write, target file, indent
        json.dump(characters, file, indent=2)
    return

def read_json():
    with path.open("r") as file:
        data = json.load(file)
    return data

def main():
    write_json()
    data = read_json()
    print(data)

if __name__ == "__main__":
    main()
```


## Working with CSV

CSV files are a common file format for tabular data. The first row contains the headers, setting up what the data is.

You can read CSV files like any other file, but don't do this.

Python has a built-in CSV module to read/write CSVs more easily.

`reader` lets you iterate over CSV rows as lists.

```python
from csv import reader
with open "fighters.csv" as file:
    csv_reader = reader(file)
    next(csv_reader) # skip headers row
    for fighter in csv_reader:
        print(fighter) # each row is a list
        print(f"{fighter[0]} is from {fighter[1]}")
```

`DictReader` lets you iterate over CSV rows as OrderedDicts.

```python
from csv import DictReader
with open "fighters.csv" as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row) # each row is an OrderedDict
        print(row["Name"])
```
### Delimiters

Readers accept a delimiter kwarg in case your data isn't separated by commas.

```python
from csv import reader
with open "example.csv" as file:
    csv_reader = reader(file, delimiter="|")
    for row in csv_reader:
        print(row) # each row is a list
```

### Writing CSV Files

#### Using Lists

`writer` - creates a writer object for writing to CSV
`writerow` - method on a writer to write a row to the CSV

```python
from csv import writer
with open("fighters.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])
```

You can use nested with statements.

```python
from csv import reader, writer
with open("fighters.csv") as file:
    csv_reader = reader(file)
    with open("screaming_fighters.csv", "w") as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])
```

You can also use `writerows` to write a list of values to multiple rows.

```python
drinks = ["Guinness", "Jameson", "Cavan Cola"]

writer.writerow(["Drink Name"])
writer.writerows(drinks)
```
#### Using Dictionaries

`DictWriter` creates a writer object for writing using dictionaries.

`fieldnames` - kwarg for the DictWriter specifying headers

`writeheader` - method on writer to write the header row

`writerow` - method on writer to write a row based on a dictionary

```python
from csv import DictWriter
with open("example.csv", "w") as file:
    headers = ["Character", "Move"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Ryu",
        "Move": "Hadouken"
    })
```

### Pickling

`pickle` is a module that serializes data, for storing in a file or database, and which you can deserialize and access later.

The data is not human readable while stored.

```python
import pickle
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat") # Call init on parent class
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Fold", "String")

# To pickle an object:
with open("pets.pickle", "wb") as file:
    pickle.dump(blue, file)

# To unpickle something:
with open("pets.pickle", "rb") as file:
    zombie_blue = pickle.load(file)
    print(zombie_blue)
    print(zombie_blue.play())
```

### Pickling with JSON

JSON, while created to send JavaScript code over the web, is now used across multiple languages.

Python has a built-in `json` module.

`json.dumps` formats a Python object as a string of JSON.

```python
j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# ["foo", {"bar": ['baz', null, 1.0, 2]}]
```

jsonpickle is a library that lets you pickle using JSON, which does take up more space but is human-readable.

```python
import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

c = Cat("Charles", "Tabby")

# pickle as JSON
with open("cat.json", "w") as file:
    frozen = jsonpickle.encode(c)
    # {"py/object": "__main__.Cat", "breed": "Tabby", "name": "Charles"}
    file.write(frozen)

# unpickle from JSON
 with open("cat.json", "r") as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
```

## Web Scraping

Web scraping involves programmatically getting data from a web page.

There are three steps: download, extract data, PROFIT!

Why scrape?

- There's data on a site that you want to store or anaylze.
- You can't get it by other means (an API)
- You want to programmatically grab the data (instead of lots of manual copy/pasting)

Is scraping... ok?

- Some websites don't want people scraping them
- Best practice is to consult the `robots.txt` file
- If making many requests, time them out
- If you're too aggressive, your IP can be blocked

### BeautifulSoup

BeautifulSoup lets you navigate through HTML with Python.

BeautifulSoup does not download HTML, you need to use the request module.

`BeautifulSoup(html_string, "html.parser")` - parses HTML

Once parsed, there are several ways to navigate:

- By tag name
- Using `find` - returns one matching tag
- Using `find_all` - returns a list of matching tags
- Using CSS selectors with `select` - returns a list of matching tags

```python
from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup.body.div) # first div
a = soup.find(id="first")
b = soup.select("#first")[0] # returns a list
c = soup.find_all(class_="special")
d = soup.select(".special")
e = soup.find_all(attrs={"data-example": "yes"})
f = soup.select("[data-example]")
print(d)
```

#### Accessing Data in Elements

- `get_text` - method to access the inner text in an element.
- `name` - method to retrieve the tag's name
- `attrs` - method to get a dictionary of attributes
- using square brackets and the name of an attribute - `soup.find("h3")["data-example"]`

### Navigating with BeautifulSoup

Navigating with BeautifulSoup involves finding elements relevant to an element.

Via tags:

- `parent` / `parents`
- `contents`
- `next_sibling` / `next_siblings`

Via searching:

- `find_parent` / `find_parents`
- `find_next_sibling` / `find_next_siblings`
- `find_previous_sibling` / `find_previous_siblings`

Using tags includes newline characters, so you need to remeber to skip over them.

`contents`, gives you a list with a tag's contents, including newline characters.

`soup.body.contents[1].next_sibling.next_sibling`

The searching methods, such as `find_next_sibling`, skip newline characters.

### Web Scraping with Scrapy

Scrapy is a Python framework for web crawling and web scraping, used to crawl websites and extract structured data from their pages.

It operates like BeautifulSoup, parsing HTML for data, even though it has a different syntax.

```python
import scrapy

class BookSpider(scrapy.Spider):
    name = "bookspider"
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        for article in response.css("article.product_pod"):
            yield {
                "price": article.css(".price_color::text").extract_first(),
                "title": article.css("h3 > a::attr(title)").extract_first()
            }
            next = response.css(".next > a::attr(href)").extract_first()
            if next:
                yield response.follow(next, self.parse)
```

To run Scrapy, call it and pass it the Python file to run and the destination file to save the data to.

```
scrapy runspider -o books.csv book_scraper.py
```

## Regular Expressions

Regular expressions (regexes) are a way of describing patterns within strings.

For example, if you want to check that an email is in a valid email format, you need to check that it:

- starts with one or more letters, numbers, +, \_,-,.
- a single @ sign
- one or more letters, numbers, or -
- a single dot
- ends with one or more letters, numbers, -, or .

Instead of writing several conditional statements you can use a regex.

```
(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)
```

Potential use cases include:

- credit card number validating
- phone number validating
- advanced find/replace in text
- formatting text/output
- syntax highlighting

| Character | Matches                           |
| --------- | --------------------------------- |
| \d        | digit 0-9                         |
| \w        | letter, digit or underscore       |
| \s        | whitespace character              |
| \D        | not a digit                       |
| \W        | not a letter, digit or underscore |
| \S        | not a whitespace character        |
| .         | any character except line break   |

| Quantifier | Matches                        |
| ---------- | ------------------------------ |
| +          | one or more                    |
| {3}        | exactly x times. {3} - 3 times |
| {3,5}      | Three to five times            |
| {4,}       | Four or more times             |
| \*         | zero or more times             |
| ?          | once or none (optional         |

You can create a group of acceptable values using `[]`, for example `[a-zA-Z0-9]`.

Inside `[]` `^` means not, rather than starts with. So `[^@$]` means any character that is not @ or $.

| Character | Sets boundary                    |
| --------- | -------------------------------- |
| ^         | start of string or line          |
| $         | end of string or line            |
| \b        | word boundary (space or newline) |

`|` works as logical or. For example `\(\d{3}\)|\d{3}` matches three digits with or without parens.

`()` groups characters. `(\(\d{3}\)|\d{3}) \d{3} \d{4}`

### Using Regex with Python

Python has a built-in `re` module for working with regexes.

With `re` you create a regex object and then use its methods.

```python
import re

pattern = re.compile(r'\d{3} \d{3}-\d{4}')

res = pattern.search("Call me at 415 555-4242")
```

### Parsing urls

A regex to parse a url looks something like this. You can use parens to group parts of the regex into capture groups.

```python
import re

url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")

print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything Else: {match.group(3)}")
print(match.groups())
print(match.group())
```

If you call `group`, or `group(0)` on the match you will get the entire url.

`group(1)`, `group(2)`, `group(3)` will give you the first, second and third capture group.

`groups()` will give you a tuple of the capture groups.

### Symbolic group names

In a regex, you can give groups names to represent them.

```python
name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
```

### Compilation Flags

Flags let you modify how regexes work.

For example, `re.IGNORECASE` `re.I` lets you do case-insensitive searches.

The verbose flag (`re.VERBOSE` or `re.X`) lets you put a regex on multiple lines and comment it.

You can combine flags using `|`.

```python
email_regex = re.compile(r"^([a-z0-9_\.-])@([0-9a-z\.-]+)\.([a-z\.]{2,6})$")

verbose_email_regex = re.compile(r"""
    ^([a-z0-9_\.-])     # username
    @                   # single @
    ([0-9a-z\.-]+)      # email provider
    \.                  # single .
    ([a-z\.]{2,6})$     # top level domain
""", re.VERBOSE | re.IGNORECASE)
```

### Substitutions

Find and replace is a common use-case for regular expressions.

The `sub` method takes a pattern and what you want to replce that pattern with.

```python
import re

def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)
```

You can select capture groups using the syntax `\g<>` and the group number.

```python
import re

text = "Last night Mrs. Peach and Ms. Daisy murdered Mr. Bowser"

pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.I)
result = pattern.sub("\g<1> \g<2>", text)

# Last night Mrs. P and Ms. D murdered Mr. B.
```

## Python and SQL

SQL is popular database choice with Python.

With SQLite, each value is one of five datatypes.

- NULL - a NULL value.

- INTEGER - a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.

- REAL - a floating point value, stored as an 8-byte IEEE floating point number.

- TEXT - a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).

- BLOB - a blob of data, stored exactly as it was input.

By default Sqlite conects to a transient in-memory database. To save it to a file, open/create a file with `.open FILENAME` or `sqlite3 FILENAME`.

SQLite follows the same syntax as other SQL databases.

`CREATE TABLE table_name (column_name datatype);`

`INSERT INTO table_name (column_names) VALUES (values);`

You can run a SQL file using `.read file_name.sql` inside Sqlite.

`SELECT * FROM table_name;`

`SELECT * from table_name WHERE column_name IS value;`

`SELECT * from table_name WHERE column_name IS NOT value AND column_name2 IS NOT value2;`

`SELECT * FROM table_name WHERE column_name LIKE %value%`;

### Connecting to a Database with Python

Python comes with a built-in library to communicate with SQLite.

First you create a connection to the database (if the database doesn't exist it'll be created).

Create a cursor (a temporary workspace for SQL commands).

Use the cursor to execute your SQL command, such as creating or inserting into a table.

Commit the changes.

Finally, close the connection.

```python
import sqlite3
# Create connection
conn = sqlite3.connect("my_friends.db")

# Create cursor object
c = conn.cursor()

# Execute SQL
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# Commit changes
conn.commit()

# Close connection
conn.close()
```

You can create a query before you execute it.

```python
insert_query = "INSERT INTO friends VALUES ('Merry', 'Lewis', 7);"
c.execute(insert_query)
```

You can interpolate variables into your query using `?` and a tuple. This handles quotes and sanitizing the data.

```python
data = ("Mary", "Reed", 9)
query = "INSERT INTO friends VALUES (?,?,?);"
c.execute(query, data)
```

You can carry out bulk inserts using `executemany`.

```python
people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 9),
    ("Henry", "Hudson", 5),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Bruhl", 3)
]

c.executemany("INSERT INTO friends VALUES (?,?,?)", people)
```

If you want to do something with each item along with inserting it, use a loop.

```python
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    print("Inserting now")
```

### Selecting with Python

When you select with Python, you can iterate over the cursor object, use `c.fetchall()` to get back a list containing the results or `c.fetchone()` to get just the first result.

```python
import sqlite3
conn = sqlite3.connect("my_friends.db")
c = conn.cursor()

c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness;")

c.fetchall()

conn.commit()
conn.close()
```

### SQL Injection

If you don't sanitize your inputs, a user could write SQL into their input and manipulate the database.

In the example below, if a user entered `' OR 1=1--` the single quote would close the quote, `1=1` would always evaluate to true and `--` would comment out any remaining characters.

```python
import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()

user_name = input("Please enter your username...")
password = input("Please enter your password...")

# Bad idea
# query = f"SELECT * FROM users WHERE username='{user_name}' AND password='{password}' OR 1=1 --'"

# Better idea
query = "SELECT * FROM users WHERE username=? AND password=?"

c.execute(query, (user_name, password))

result = c.fetchone()
if(result):
    print("Welcome back")
else:
    print("Failed login")

conn.commit()
conn.close()
```

## Match Statements
Python 3.10 added structural pattern matching using match statements.

This lets you:
- extract information from complex data types
- have conditional branching based on the structure of the data
- apply specific actions based on different forms of data

A match statement takes an expression and compares its value to patterns in one or more case blocks. Each pattern is checked from top to bottom. 

You can optionally include a wildcard case (commonly `_`) as the last case. If there is no exact match, the wildcard will be used as the matching case. If there is no match and no wildcard there will be a no-op and nothing will happen.

You can combine patterns using `|` ("or").

```python
def http_error(status):
	match status:
		case 400:
			return "Bad request"
		case 401 | 403:
			return "Not allowed"
		case 404:
			return "Not found"
		case 418:
			return "I'm a teapot"
		case _:
			return "Something's wrong with the internet"
```

### Patterns with literals and variables
Patterns can match a literal value or extract and bind a variable

```python
# point is an (x,y) tuple
match point:
	case (0,0):
		print("Origin")
	case (0,y):
		print(f"Y={y}")
	case (x,0):
		print(f"X={x}")
	case (x,y):
		print(f"X={x}, Y={y}")
	case other:
		raise ValueError("Not a point)
```

### Patterns and classes
You can match a class by using the class name and constructor argument list as a pattern. This pattern lets you capture class attributes as variables.

```python
class Point:
	x: int
	y: int

def location(point):
	match point:
		case Point(x=0, y=0):
			print("Origin is the point's location")
		case Point(x=0, y=y):
			print(f"Y={y} and the point is on the y-axis")
		case Point(x=x, y=0):
			print(f"X={x} and the point is on the x-axis")
		case Point():
			print("The point is located somewhere else on the plane")
		case _:
			print("Not a point")

```

### Complex patterns and wildcards
A wildcard can be used in more complex patterns where you don't care what one or more of the values is.

```python
match test_variable:
	case ("warning", code, 40):
		print("A warning was received")
	case ("error", code, _):
		print(f"An error with code [{code}] occurred")
```

### Pattern guards
You can add an "if" clause to a pattern as a guard. If the guard is false, the match goes on to the next case block. Value capturing happens before the guard is evaluated.

```python
match point:
	case Point(x, y) if x == y:
		print(f"The point is located on the diagonal Y=X at {x}")
	case Point(x, y):
		print("Point is not on the diagonal")
```