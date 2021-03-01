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
