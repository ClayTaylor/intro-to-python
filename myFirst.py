"""
-- Building a Calculator --
take in 2 inputs from the user
add those inputs together
return the sum of those two inputs back to the user
"""

# First Input from the User stored in variable x & converting the input to a number.
x = int(input("Enter the first number here: "))
# Second Input from the User stored in variable y & converting the input to a number.
y = int(input("Enter the second number here: "))
# Combining those inputs in a new variable named sum
sum = x + y
# Printing out the variable sum to the user
print("The sum of x and y is: " + str(sum))