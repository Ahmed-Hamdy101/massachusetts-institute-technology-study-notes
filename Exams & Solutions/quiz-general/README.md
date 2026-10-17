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
<hr>

## my answer / explain 
so he means any programs that with these premitives can be O(1) but this not correct because i can use those prem... and make run tinme is O(N) as recursion

<hr>
## AI 

## Yes — exactly

Your understanding is correct.

He is probably making a very simplified claim like:

> If a program is built only from a fixed set of primitive operations, then it may look like it runs in constant time.

But in real algorithm analysis, that is not automatically true.

Because with those same primitives, you can still build:

- loops
- recursion
- repeated calls
- input-driven behavior

and then the runtime can become:

- $O(1)$
- $O(\log n)$
- $O(n)$
- $O(n^2)$
- etc.

So the right conclusion is:

> The primitives alone do not guarantee constant time.  
> The control flow and repetition matter.

---

## Example

This uses only assignment, conditionals, and recursion:

```python
def f(n):
    if n == 0:
        return
    f(n - 1)
```

It uses only primitive constructs, but its runtime is $O(n)$.

So your point is exactly right:

- “only these primitives” does not imply “constant time”
- recursion can make it linear
- without a base case it can be infinite

---

## Best way to phrase it

You can say:

> A program built from basic operations is not necessarily constant time. Constant time only means the number of steps is independent of input size. Recursion and loops can make the runtime grow with input size, even if each step uses simple primitives.

That is the correct CS idea.

If you want, I can also help you turn this into a short answer that sounds like a proper MIT class response.