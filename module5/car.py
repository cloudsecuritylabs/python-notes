class Car:
    def __init__(self, color, windows_number, price):
        self.color = color
        self.window_number = windows_number
        self.price = price
    def speed_up(self):
        print("Speed up by 10 miles/hour")

jeep = Car("White", 4, 40000)
toyota = Car("Red", 6, 25000)

print(f'Color of the jeep is {jeep.color}')
print(f'Color of the toyota is {toyota.color}')
jeep.speed_up()

