# Lecture 04

This folder contains materials for Lecture 04 of the MIT CS study notes.

## Topic

Functions, scope, and modular programming.

This lecture focuses on breaking programs into reusable blocks of code, understanding local versus global variables, and practicing cleaner problem-solving patterns.

## Files

- `_console_mit_6.00.py` — Python examples covering function definition, return values, scope, and recursion.

## How to run

From this folder, run:

```bash
python _console_mit_6.00.py
```

## Learning goals

- Define and call functions
- Use parameters and return values
- Understand local and global variables
- Practice decomposition with smaller reusable routines
- Explore recursion and a simple algorithmic design pattern

## Most important note

### Question

"Any program that can be written using only function definitions and calls, the basic arithmetic operators, assignment, and conditionals will run in constant time."

### Answer

False.

Constant time means the runtime does not depend on the input size, so it is $O(1)$. A program can use only simple primitives and still not be constant time because recursion and loops can repeat many times depending on the input.

Example:

```python
def countdown(n):
    if n == 0:
        return
    countdown(n - 1)
```

This uses only function calls, conditionals, and assignment, but it is not constant time. It is linear: $O(n)$.

### Key idea

- Constant time = fixed amount of work
- Recursion is not automatically constant time
- A recursive function must have a base case
- Without a base case, recursion can run forever

### Memory phrase

"Recursion is not constant time unless the number of calls is fixed; without a base case, it can be infinite."
