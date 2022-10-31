# this code is to learn input function

"30"
name = input("What is your name? ")
number = input("Give me a number? ")
# do not use ever in python
print("Your name is %s and the number is %s" % (name, number))
# improved but still do not use
print("Your name is {} and the number is {}".format(name, number))
# use this format
print(f"Your name is {name} and the number is {number}")