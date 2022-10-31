first_number = int(input("Please give me the first number"))
second_number = int(input("Please give me the second number:"))

def return_list(first_number, second_number):
    return [first_number, second_number]

def return_tuple(first_number, second_number):
    return (first_number, second_number)

def return_dictionary(first_number, second_number):
    return {first_number:second_number}

my_list = return_list(first_number, second_number)
my_tuple = return_tuple(first_number, second_number)
my_dictionay = return_dictionary(first_number, second_number)

print(my_list)
print(my_tuple)
print(my_dictionay)