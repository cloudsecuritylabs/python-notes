# Lab1 - Module 4
# ask user for two different numbers
# store the result of division number1/number
# make sure you can catch if the user is providing bad input (0)

# Improvement goal - only ask for re-entering the number if the number is invalid.
# Improvement goal - keep going with miltiple calculations until the user really wants to end.

keep_going = True
while keep_going:
    try:
        first_number = int(input("Please enter the first number: "))
        second_number = int(input("Please enter the second number: "))
        division = first_number/second_number
        print(f'result is {division}')
        keep_going = False
    except ZeroDivisionError as error:
        print("Can't divide by zero!")
        print(error)
    except ValueError as error:
        print("Only enter digits")
        print(error)






# > write(overwrite) w
# >> append
