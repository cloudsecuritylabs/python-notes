# factorial
# factorial(4) -> 4*3*2*1
# factorial(6) -> 6*5*4*3*2*1
# factorial(1) -> 1
# factorial(0) -> 1

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

result = factorial(4)
print(result)
