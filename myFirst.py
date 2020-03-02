"""
calculator
take in two inputs from user
add them up
Present the answer to the user
"""

# ask the user to input a
a = input("Please type a number: ")
# ask the user to input b
b = input("Please type another number: ")

# convert a and b to integers
a = int(a)
b = int(b)

# add a + b put in answer in sum
sum = a + b
# report the sum to the user
print("{} + {} = {}".format(a, b, sum))


