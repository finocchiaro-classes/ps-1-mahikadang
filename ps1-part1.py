# Ask the user for the first number, store the value in a variable
firstnum = firstnum = int(input("Enter an integer between 10 and 100: "))

# Ask the user for the second number, store the value in a variable
secondnum = secondnum = int(input("Enter an integer less than 4: "))

# Repeat back the numbers
print(f"You entered {firstnum} and {secondnum}")

# Perform calculations. Be careful about string formatting for autograders.
print(f"{firstnum} + {secondnum} = {firstnum + secondnum}")
print(f"{firstnum} * {secondnum} = {firstnum * secondnum}")
print(f"{firstnum} ** {secondnum} = {firstnum ** secondnum}")
print(f"{firstnum} % {secondnum} = {firstnum % secondnum}")
