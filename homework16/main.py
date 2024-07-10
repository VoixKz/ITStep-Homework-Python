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
    def __init__(self, name, model, year, capacity):
        super().__init__(name, model, year)
        self.capacity = capacity

    def blend_food(self):
        return f'Blending food with {self.capacity} capacity'


class MeatGrinder(Device):
    def __init__(self, name, model, year, capacity):
        super().__init__(name, model, year)
        self.capacity = capacity

    def grind_meat(self):
        return f'Grinding meat with {self.capacity} capacity'


class Ship:
    def __init__(self, name, model, year, crew_size):
        self.name = name
        self.model = model
        self.year = year
        self.crew_size = crew_size

    def get_info(self):
        return f'Ship: {self.name}, Model: {self.model}, Year: {self.year}, Crew Size: {self.crew_size}'


class Frigate(Ship):
    def __init__(self, name, model, year, crew_size, armament):
        super().__init__(name, model, year, crew_size)
        self.armament = armament

    def fire_cannons(self):
        return f'Firing {self.armament} cannons'


class Destroyer(Ship):
    def __init__(self, name, model, year, crew_size, capacity):
        super().__init__(name, model, year, crew_size)
        self.capacity = capacity

    def launch_missiles(self):
        return f'Launching {self.capacity} missiles'


class Cruiser(Ship):
    def __init__(self, name, model, year, crew_size, capacity):
        super().__init__(name, model, year, crew_size)
        self.capacity = capacity

    def fire_guns(self):
        return f'Firing {self.capacity} guns'

