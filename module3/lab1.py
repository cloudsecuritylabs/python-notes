# ask the user for a range ()
# write a loop to iterate over the range and print each number
# print("what is the range? ")

range_from_user = int(input("Please enter a range of numbers? " ))

for number in range(range_from_user):
    print(number + 1, end = " ")

print("\n")

for number in range(1, range_from_user + 1):
    print(number, end = " ")
