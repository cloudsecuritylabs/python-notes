while True:
    animal = input("What is the name of your favorite animal?: or Type exit to end: ")
    with open("animal_names_tyler.txt", "a+") as file:
        if animal == 'exit':
            break
        file.write(animal + "\n")

