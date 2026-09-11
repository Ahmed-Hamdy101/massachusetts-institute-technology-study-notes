"""Lecture 03: MITOPENCOURSEWARE common code patern | iterative programs
"""
# find square root of a number
x=16
ans = 0
while ans*ans < x:
    ans = ans + 1

print(ans)


print ("---------------------- Square Root------------------------")
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

#definsive programming 
# A) Assume inputs may be invalid or unexpected.
# B) Assume code written by anyone, including yourself, may contain mistakes.


print ("---------------------- While Loop------------------------")


# get all divisors of b using while loop

b = 10
icount = 1 
# while icount < b:
#     if b % icount == 0:
#         print("b is divisible by",icount)
#     icount = icount + 1



print ("---------------------- For Loop------------------------")

# get all divisors of b using for loop
for icount in range(1,b):
    if b % icount == 0:
        print("b is divisible by",icount)


print ("---------------------- Tuples ------------------------")

# tuples are immutable
# eric does the mistake as he means it   and  let anyone catch it  to see if anyone catch it
# RTX = [1,2,3,4,5] // catch error of eric
print("tuples are immutable")
RTX = (1,2,3,4,5,6)
# we can change the tuples values by casting
RTX = (11,) + RTX[1:]
# So yes, it leaves out indexes 0 and 1, then adds 11 at the beginning. It effectively replaces index 0 and deletes the old value at index 1.
# RTX = (11,) + RTX[2:]
print(RTX)
print(RTX[0])
print(RTX[1])
print(RTX[2])
print(RTX[3])
print(RTX[4])
print(RTX[5])
# print(RTX[6]) //  out of range error
# print(RTX[7]) //  out of range error
print(RTX[-1])  # print last element : reverse indexing

# Slicing in tuples
# keep in mind that tuple is immutable can't be changed but slicing is possible
# and in slice indexing the first index is inclusive and second index is exclusive while slicing
# means last index is not included in the slice
print(RTX[-3:-1])  
# first of that  index is included and last index is excluded in the slice
print(RTX[1:3])
# bring all of the elements from the start to the end of the tuple
print(RTX[:3])

# converte tuple to list
print(list(RTX))


# range is a function that returns a sequence of numbers from start to end-1 
# list(range(1, 10)) # range is a function that returns a sequence of numbers from start to end-1
#  range creates a range object that it does not immediately display all its values.
list(range(1, 10)) # range is a function that returns a sequence of numbers from start to end-1
print(list(range(1, 10))) # range is a function that returns a sequence of numbers from start to end-1


# execute a program that prints the numbers from 1 to 100 and add div to 
def div(s):
    # range is a function that returns a sequence of numbers from start to end-1
    size = s
    # range creates a range object that it does not immediately display all its values.
    devisors = ()
    # range is a function that returns a sequence of numbers from start to end-1
    i = 1
    # range creates a range object that it does not immediately display all its values.
    for  i in range(i,size):
        # range is a function that returns a sequence of numbers from start to end-1
        if size%i == 0 :
         # add value to devisorList 
         # important u must add "," to make it tuple
         # TypeError: can only concatenate tuple (not "int") to tuple  
         # devisors = devisors + (i) 
         devisors = devisors + (i,)
    # return devisorList 
    return devisors

# execute a program that prints the numbers from 1 to x
print(div(int(input("Enter a number: "))))



# couple of string are mutable and immutable can be changed but slicing is possible
text = "friend"
#       012345
text = text[:2] + text[3] + text[2] + text[4:]

# text[3:4].append("i")

print(text)

# another way
# 1. convert string to list
# 2. swap the characters
# 3. convert list to string
# 4. print
characters = list(text)

characters[2], characters[3] = characters[3], characters[2]

# The empty string "" is the separator. It means “join them with nothing between them”:

text = "".join(characters)
print(text)  # freind
print(text[1])  # f


# program adds the digits of the number 1995
digit = 0
temp = "" 
for c in str("1995"):
    reversed_num = c + temp
    digit = digit + int(reversed_num)

print(digit)