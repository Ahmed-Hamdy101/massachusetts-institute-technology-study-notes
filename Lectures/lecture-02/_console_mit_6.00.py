"""Lecture 02: Basic Operations and String Handling.

Demonstrates arithmetic operations, string operations, type conversions,
lexicographic string comparison, operator precedence, and variable scope.
"""

# Arithmetic: 3 * 4 = 12
print(3 * 4)

# String concatenation: joining two strings together
print('a' + 'c')

# Type conversion error: cannot add string and integer directly
# print('a' + 3)  # TypeError: can only concatenate str (not "int") to str

# Solution: convert the integer to a string before concatenation
print('a' + str(3))

# String comparison using lexicographic (alphabetical) order
# This line would cause a TypeError because you cannot compare different types
# print('a' < 3)  # TypeError: '<' not supported between instances of 'str' and 'int'

# Correct string comparison: comparing two strings lexicographically
# In ASCII, '4' (52) > '3' (51), so '4' is not less than '3'
print(str(4) < '3')  # False

# String comparison: '4' vs '3' in lexicographic order
# Result: False because '4' comes after '3' in ASCII ordering
print('4' < '3')  # False

# Integer division operator (//): returns the quotient without the remainder
# 9 divided by 5 = 1 (with remainder 4, which is discarded)
print(9 // 5)  # 1

# Modulo operator (%): returns the remainder after division
# 9 divided by 4 = 2 remainder 1
print(9 % 4)  # 1

# Operator precedence: multiplication has higher priority than addition
# 3 + 4 * 5 is evaluated as 3 + (4 * 5) = 3 + 20 = 23
print(3 + 4 * 5)  # 23

# Using parentheses to override default operator precedence
# (3 + 4) * 5 is evaluated as 7 * 5 = 35
print((3 + 4) * 5)  # 35
 
# Variable assignment: assign the value 3 to variable x
x = 3

# Variable assignment: assign the value of x to variable y
# Both x and y now reference the same value: 3
y = x

# String comparison demonstration using ASCII values
# ASCII character values:
#   'a' = 97, 'b' = 98, 'c' = 99, ... 'x' = 120, 'y' = 121, 'z' = 122
#
# Comparison: 'x' (120) vs 'b' (98)
# Since 120 > 98, 'x' is NOT less than 'b', so the if block does not execute

z = 'b'
if 'x' < z:
    print('hello z')
# Output: (nothing) - because 'x' is greater than 'b', the condition is false


# Variable scope demonstration
# The print statement below is at the module level, not inside the if block
# It will always execute regardless of the if condition
z = 'b'
if 'x' < z:
    print('hello z')  # This will NOT print because 'x' > 'b'
print('hello x')  # This ALWAYS prints because it's not inside the if block


# Finding the minimum value among three numbers
# Initial values: x = 20, w = 14, z = 13
x = 20
w = 14
z = 13

# Original nested if-else approach (commented out):
# This structure works but is harder to read with multiple nested levels
# if x < w:
#     if x < z:
#         print('x is the smallest')
#     else:
#         print('z is the smallest')
# else:
#     print('w is the smallest')

# Improved approach using logical AND and elif keywords:
# More readable and follows a clearer decision flow
if x < w and x < z:
    print('x is the smallest')
elif w < z:
    print('w is the smallest')
else:
    print('z is the smallest')


# Demonstrating a while loop to count iterations
y = 0 
x = 3
iterations = x 
# instuction 1
# While loop: continues as long as iterations > 0
while iterations > 0:
    # Add the value of x to y in each iteration
    y = y + x
    # if this removed, the loop will (INFINITE LOOP) run indefinitely because iterations will never decrease
    iterations = iterations - 1
# if while is done go excute instruction 2
print(y)

x = 20 
iteration = 1
if(iteration<x):
    if x%iteration == 0:
        print('x is even')

    else:
        print('x is odd')
    iteration = iteration + 1
    