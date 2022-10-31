# Create a new script that checks if users can legally purchase an alcoholic beverage.
# Receive user input for two variables: name and age.
# Use conditional operators to
# compare the age variable against the legal age

name = input("Please enter your legal name: ")
age = input("Please enter your age: ")

# if the age is equal to or greater than 21
if int(age) >= 21:
    print(f"Congratulations {name}! You can legally purchase alcohol.")
else:
    print(f"Too bad, so sad {name}! You can NOT legally purchase alcohol.")


