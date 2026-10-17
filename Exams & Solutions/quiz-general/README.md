# Quiz General

This folder contains quick revision material and important conceptual questions for the MIT CS study notes.

## Most Important Concept: Constant Time vs Recursion

### Question

"Any program that can be written using only function definitions and calls, the basic arithmetic operators, assignment, and conditionals will run in constant time."

### Short answer

False.

### Why false?

Constant time means the runtime does not depend on the size of the input. In big-O notation, this is $O(1)$.

A program can still use only simple primitives and still not be constant time. For example, recursion uses function calls and conditionals, but if it calls itself repeatedly, the runtime may grow with the input size.

### Example

```python
def countdown(n):
    if n == 0:
        return
    countdown(n - 1)
```

This uses only function calls, conditionals, and assignment, but it is not constant time. The runtime grows with `n`, so it is linear: $O(n)$.

### Important idea

- Constant time means the work is fixed and does not grow with input size.
- Recursion is a programming technique, not automatically constant time.
- If recursion has no base case, it can run forever.
- A recursive function must reduce the problem toward a base case.

### Base case example

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

This is valid recursion because it has a base case and moves toward it.

### Final takeaway

A program built from simple operations is not automatically $O(1)$. The control flow and repetition matter. Recursion can produce linear or worse behavior, and without a stopping condition it may never terminate.

## Quick Revision Questions

### Q1. What does $O(1)$ mean?
A. The algorithm takes a fixed amount of work regardless of input size.

### Q2. Is recursion always constant time?
A. No. Recursive functions can be linear or worse depending on how many times they call themselves.

### Q3. What is a base case in recursion?
A. The condition that stops the recursive calls.

### Q4. What happens if recursion has no base case?
A. It can run forever or until a runtime error such as `RecursionError`.

### Q5. Why does recursion sometimes lead to $O(n)$ time?
A. Because each recursive call reduces the problem and may happen once per input value.

## Memory tip

Remember:

- Constant time = same work for all inputs
- Recursion = repeated calls
- Base case = stopping condition
- No base case = infinite recursion

# my answer / explain to this 

so he means any programs that with these premitives can be O(1) but this not correct because i can use those prem... and let CT Linear as O(N) as recursion