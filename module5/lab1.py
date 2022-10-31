# Request from the user two numbers and an operator.
while True:
    first_number = int(input("Please give me the first number:  or type 999 to end"))
    if first_number == 999:
        break
    second_number = int(input("Please give me the second number: "))
    operator = input("Which math function? allowed [+ - * /] ")

    def addition(first_number, second_number):
        return first_number + second_number

    def subtraction(first_number, second_number):
        return first_number - second_number

    def multiplication(first_number, second_number):
        return first_number * second_number

    def division(first_number, second_number):
        return first_number / second_number

    # addition
    if operator == "+":
        result = addition(first_number, second_number)
        print(result)
    elif operator == "-":
        result = subtraction(first_number, second_number)
        print(result)
    elif operator == "*":
        result = multiplication(first_number, second_number)
        print(result)
    else:
        result = division(first_number, second_number)
        print(result)



