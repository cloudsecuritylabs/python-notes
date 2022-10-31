# ask user for some input
# write to a file
while True:
    animal = input("What is the name of your favorite animals? or type exit to end the program: ")
    if animal == 'exit':
        break
    with open("animal_names_delano.txt", "w") as file:
        file.write(animal+"\n")

with open ("animal_names_delano.txt", "r") as file:
    result = file.read()
    print(result)