# imports argv from the system
from sys import argv
# assigns argv to script and arg
script, arg = argv
# converts arg into an int
n = int(arg)
#creates a loop which checks if i is in the range of 1 and n
for i in range( 1, n ):
# checks if n divided by i is equal to i and if n mod i is equal to 0
    if n//i == i and n%i == 0:
        # prints the value of n divided by i
        print(n//i)
        # exits the if statement if the requirements aren't met
        exit(0)
print(False)