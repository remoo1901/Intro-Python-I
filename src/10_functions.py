# Write a function is_even that will return true if the passed-in number is even.


# YOUR CODE HERE

def is_even(num):
    if num % 2 == 0:
        print("EVEN!")
        return True
    else:
        print("ODD!")
        return False

# Read a number from the keyboard


num = input("choose a number: ")
print(f"you entered  {num}")

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


print(is_even(5))
