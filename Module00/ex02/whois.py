import sys

# Check if the correct number of arguments were provided
assert len(sys.argv) == 2, "Error: Please provide exactly one argument."

# Try to convert the argument to an integer
try:
    num = int(sys.argv[1])
except ValueError:
    assert False, "Error: Argument must be an integer."

# Check if the number is odd, even or zero
if num == 0:
    print("The number is zero.")
elif num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")