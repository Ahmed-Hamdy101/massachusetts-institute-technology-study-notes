"""Lecture 04: all functions are intentionally left without a solution."""


# sqrt is a function that takes a number and returns its square root.
def sqrt(x):
    """
    Return the square root of x.
    """
    # Initialize answer to 0.
    answer = 0 
    # Use a while loop to increment answer until its square is greater than or equal to x.
    if x <=0 :
        while answer * answer < x:
            # Increment answer by a small amount to approach the square root.
            answer += 0.01
            if answer * answer !=x:
                print("The square root of", x, "is approximately", answer)
                return None
            else:
                print("The square root of", x, "is exactly", answer)
                return answer
    else:
        print("Input must be a positive number.")
        return None

    return answer


# x in that function it another scope  in this module from previous examples.
def function_two(x, y):
    """ Local Binds Does not effect the global binds. 
    """
    pass


# not implemented yet
def function_three(name):
    """Incomplete function example 3.

    Add the algorithm later.
    """
    pass

# not implemented yet
def function_four(numbers):
    """Incomplete function example 4.

    This function is intentionally blank.
    """
    pass
