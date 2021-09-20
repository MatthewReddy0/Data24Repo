class Car:

    def __init__(self, car_make, max_speed):
        self.car_make = car_make
        self.max_speed = max_speed
        self.current_speed = 0

    def increase_speed(self, speed_increase):
        if self.current_speed + speed_increase > self.max_speed:
            print(f'Your car cannot go any quicker than {self.max_speed}')
            self.current_speed = self.max_speed
        else:
            self.current_speed += speed_increase


my_car = Car('Ferrari', 200)

print(my_car.car_make)
print(my_car.current_speed)
my_car.increase_speed(150)
print(my_car.current_speed)
my_car.increase_speed(75)
print(my_car.current_speed)


"""class Dog:
    animal_species = 'canine'  # class variable

    def bark(self):
        return 'Woof!'


Dog.animal_species = 'dolphin'
fido = Dog()
lassie = Dog()
fido.animal_species = 'lupine'

print(fido.animal_species)
print(lassie.animal_species)
print(lassie.bark())
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


me = Person('Matthew', '21')


me.age = 42

# Here is the Gas class


class Gas:
    def __init__(self, price, unit):
        self.price = price
        self.unit = unit

    def info(self):
        print(f"I am gas. My price is {self.price}, measured in {self.unit}.")

    def make_sound(self):
        print("psssssssssssssss")


class Water:
    def __init__(self, price, unit):
        self.price = price
        self.unit = unit

    def info(self):
        print(f"I am water. My price is {self.price}, measured in {self.unit}.")

    def make_sound(self):
        print("whooooooosh")


# Code that other people can use
g = Gas(0.43, 'cubic metres')
w = Water(0.075, 'litres')
for amenity in (g, w):
    amenity.make_sound()            # These are the lines we care about. Calling the same method for different classes.
    amenity.info()
