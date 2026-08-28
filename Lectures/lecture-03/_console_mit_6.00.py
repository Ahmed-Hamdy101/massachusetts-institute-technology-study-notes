"""Lecture 03: MITOPENCOURSEWARE common code patern | iterative programs
"""
# find square root of a number
x=16
ans = 0
while ans*ans < x:
    ans = ans + 1

print(ans)


# find square root of a number
# x=16
ans = 0
# check if x is not (-) 
if x >=0 :
    # iteration to reach value
    while ans*ans < x:
        # counter for change result
        ans = ans + 1
        if ans*ans != x:
            # if answer is not perfect root print this
            print(ans,"ans is not prefect root")
        else:
            # else ans is reached
            print(ans,"ans is prefect root")
# if its print it is (-)
else:
    print(x,"x is nagitve value")

print(ans)