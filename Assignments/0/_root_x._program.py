"""Root and Square Root Calculator.

Demonstrates calculation of square roots and other root operations.
"""

# TODO: Add implementation code here 



def Root(x : int):
    guess: float = 1.0 
    while guess * guess  != x:
        guess = (guess + x/guess)/2
        print(guess)
    return guess
print(Root(16))
