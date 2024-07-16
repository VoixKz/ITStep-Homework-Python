class Device:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def __str__(self):
        return f'Device: {self.name}, Model: {self.model}, Year: {self.year}'


class CoffeeMachine(Device):
    def __init__(self, name, model, year, coffee_type):
        super().__init__(name, model, year)
        self.coffee_type = coffee_type

    def make_coffee(self):
        return f'Making {self.coffee_type} coffee'


class Blender(Device):
    def __init__(self, name, model, year, capacity, mode):
        super().__init__(name, model, year)
        self.capacity = capacity
        self.mode = mode #reverse, 1st, 2nd, 3rd modes

    def change_mode(self, mode):
        self.mode = mode
        return f'Changing mode to {mode}'
    
    def blend_food(self):
        return f'Blending food with {self.capacity} capacity using {self.mode} mode'


class MeatGrinder(Device):
    def __init__(self, name, model, year, capacity):
        super().__init__(name, model, year)
        self.capacity = capacity

    def clean(self):
        return f'Cleaning with {self.capacity} capacity'
    
    def grind_meat(self):
        return f'Grinding meat with {self.capacity} capacity'
    


coffee_machine = CoffeeMachine("Coffee Maker", "CM100", 2022, "Espresso")
print(coffee_machine)
print(coffee_machine.make_coffee())
blender = Blender("Food Blender", "BL200", 2021, "1L", "reverse")
print(blender)
print(blender.change_mode("2nd"))
print(blender.blend_food())
meat_grinder = MeatGrinder("Meat Grinder", "MG300", 2024, "2kg")
print(meat_grinder)
print(meat_grinder.clean())
print(meat_grinder.grind_meat())



class Ship:
    def __init__(self, name, model, year, crew_size):
        self.name = name
        self.model = model
        self.year = year
        self.crew_size = crew_size

    def __str__(self):
        return f'Ship: {self.name}, Model: {self.model}, Year: {self.year}, Crew Size: {self.crew_size}'


class Frigate(Ship):
    def __init__(self, name, model, year, crew_size, armament, country):
        super().__init__(name, model, year, crew_size)
        self.armament = armament
        self.country = country

    def set_country(self, country):
        self.country = country
        return f'Setting country to {country}'

    def fire_cannons(self):
        return f'Firing {self.armament} cannons'


class Destroyer(Ship):
    def __init__(self, name, model, year, crew_size, capacity, target):
        super().__init__(name, model, year, crew_size)
        self.capacity = capacity
        self.target = target

    def set_target(self, target):
        self.target = target
        return f'Setting target to {target}'

    def launch_missiles(self):
        return f'Launching {self.capacity} missiles to {self.target}'


class Cruiser(Ship):
    def __init__(self, name, model, year, crew_size, capacity, town_from, town_to):
        super().__init__(name, model, year, crew_size)
        self.capacity = capacity
        self.town_from = town_from
        self.town_to = town_to
    
    def sail(self):
        return f'Sailing from {self.town_from} to {self.town_to}'

    def fire_guns(self):
        return f'Firing {self.capacity} guns'



frigate = Frigate("Frigate", "FR100", 2017, 100, "10", "China")
print(frigate)
print(frigate.set_country("Kazakhstan"))
print(frigate.fire_cannons())
destroyer = Destroyer("Destroyer", "DS200", 2022, 200, "1000", "Enemy Ship")
print(destroyer)
print(destroyer.set_target("Island"))
print(destroyer.launch_missiles())
cruiser = Cruiser("Cruiser", "CR300", 2013, 300, "500", "Beijing", "Tokyo")
print(cruiser)
print(cruiser.sail())
print(cruiser.fire_guns())



import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class CircleInSquare(Circle, Square):
    def __init__(self, side):
        radius = side / (2**0.5)
        Circle.__init__(self, radius)
        Square.__init__(self, side)



        circle = Circle(3)
        print(circle.area())
        square = Square(4)
        print(square.area())
        circle_in_square = CircleInSquare(5)
        print(circle_in_square.area())


class Engine:
    def __init__(self, engine_type, capacity):
        self.engine_type = engine_type
        self.capacity = capacity

    def engine_info(self):
        return f"Тип двигателя - {self.engine_type}"
    

class Wheels:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def wheel_info(self):
        return f"Количество колес - {self.number_of_wheels}"


class Doors:
    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def door_info(self):
        return f"Количество дверей - {self.number_of_doors}"


class Car(Wheels, Engine, Doors):
    def __init__(self, model, year, number_of_wheels, engine_type, capacity, number_of_doors):
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, engine_type, capacity)
        Doors.__init__(self, number_of_doors)
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.model} {self.year}: {self.engine_info().lower()}, {self.wheel_info().lower()}, {self.door_info().lower()}"
    


car = Car("Toyota Camry", 2023, 4, "Petrol", 3.5, 4)
print(car)



import json
class Shape:
    def show(self):
        return f"Метод show должен быть переопределен в подклассе"

    def save(self, filename):
        with open(f'./homework16/{filename}.json', 'a') as file:
            json.dump(self.__dict__, file)
            file.write('\n')

    @classmethod
    def load(cls, filename):
        shapes = []
        with open(f'./homework16/{filename}.json', 'r') as file:
            for line in file:
                shape_dict = json.loads(line)
                shape = cls(**shape_dict)
                shapes.append(shape)
        return shapes


class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def show(self):
        print(f"Квадрат с левым верхним углом в ({self.x}, {self.y}) и стороной {self.side}")


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Прямоугольник с левым верхним углом в ({self.x}, {self.y}), шириной {self.width} и высотой {self.height}")


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        print(f"Окружность с центром в ({self.x}, {self.y}) и радиусом {self.radius}")


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Эллипс вписанный в прямоугольник с верхним левым углом в ({self.x}, {self.y}), шириной {self.width} и высотой {self.height}")



shapes = [Square(1, 2, 3), Rectangle(4, 5, 6, 7), Circle(8, 9, 10), Ellipse(11, 12, 13, 14), 
          Square(15, 16, 17), Rectangle(18, 19, 20, 21), Circle(22, 23, 24), Ellipse(25, 26, 27, 28)]

for figure in ('square', 'rectangle', 'circle', 'ellipse'):
    open(f'./homework16/shapes_{figure}.json', 'w').close()

for shape in shapes:
    shape.save(f'shapes_{shape.__class__.__name__.lower()}')

for figure in (Square, Rectangle, Circle, Ellipse):
    shapes = figure.load(f'shapes_{figure.__name__.lower()}')
    for shape in shapes:
        shape.show()