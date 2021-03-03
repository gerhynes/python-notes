# Python Notes

Python is one of the most popular and flexible programming langauges, used for everything from basic scripting to machine learning.

### Numbers

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

### Variables and Data Types

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

### Strings

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
