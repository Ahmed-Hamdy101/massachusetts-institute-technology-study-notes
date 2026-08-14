"""Even or Odd Number Checker.

Demonstrates how to determine if a number is even or odd using integer division.
"""

x = 15

# Use integer division (//) instead of float division (/) to ensure we work with whole numbers.
# Multiply the result by 2: if the product equals the original number, it's even.
# If (x//2) * 2 == x, then x is even; otherwise, x is odd.
if (x // 2) * 2 == x:
    print("x is even")
else:
    print("x is odd") 
 
    