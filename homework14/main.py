class Car:
    #Конструктор класса
    def __init__(self, model=None, year=None, manufacturer=None, engine_capacity=None, color=None, price=None):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def __str__(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Engine Capacity: {self.engine_capacity}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")

    #Методы для ввода и вывода данных
    def input_data(self):
        self.model = input("Enter model: ")
        self.year = int(input("Enter year: "))
        self.manufacturer = input("Enter manufacturer: ")
        self.engine_capacity = float(input("Enter engine capacity: "))
        self.color = input("Enter color: ")
        self.price = float(input("Enter price: "))

    def output_data(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Engine Capacity: {self.engine_capacity}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")

    #Доступ к полям через методы
    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model

car1 = Car("BMW X3", 2020, "BMW", 3.0, "Black", 100000)
car2 = Car()
car2.input_data()
car1.output_data()
print(car1.get_price())



class Book:
    def __init__(self, title=None, year=None, publisher=None, genre=None, author=None, price=None):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Publisher: {self.publisher}")
        print(f"Genre: {self.genre}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

    def input_data(self):
        self.title = input("Enter title: ")
        self.year = int(input("Enter year: "))
        self.publisher = input("Enter publisher: ")
        self.genre = input("Enter genre: ")
        self.author = input("Enter author: ")
        self.price = float(input("Enter price: "))

    def output_data(self):
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Publisher: {self.publisher}")
        print(f"Genre: {self.genre}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

book1 = Book("The Great Gatsby", 1925, "Scribner", "Fiction", "F. Scott Fitzgerald", 10.0)
book2 = Book()
book2.input_data()
book1.output_data()
print(book1.get_price())



class Stadium:
    def __init__(self, name=None, opening_date=None, country=None, city=None, capacity=None):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        print(f"Name: {self.name}")
        print(f"Opening Date: {self.opening_date}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Capacity: {self.capacity}")

    def input_data(self):
        self.name = input("Enter name: ")
        self.opening_date = input("Enter opening date: ")
        self.country = input("Enter country: ")
        self.city = input("Enter city: ")
        self.capacity = int(input("Enter capacity: "))

    def output_data(self):
        print(f"Name: {self.name}")
        print(f"Opening Date: {self.opening_date}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Capacity: {self.capacity}")

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

stadium1 = Stadium("Wembley Stadium", "1923-07-13", "United Kingdom", "London", 90000)
stadium2 = Stadium()
stadium2.input_data()
stadium1.output_data()
print(stadium1.get_capacity())



class MainClass:
    def __init__(self, text=None):
        self.text = text

    def set_text(self, text=None):
        if text is not None:
            self.text = text
        else:
            self.text = input("Enter text: ")

    def get_text(self):
        return self.text


class ChildClass(MainClass):
    def __init__(self, text=None, number=None):
        super().__init__(text)
        self.number = number

    def set_number(self, number=None):
        if number is not None:
            self.number = number
        else:
            try:
                self.number = float(input("Enter number: "))
            except ValueError:
                print("Invalid type. Please enter a number")

    def get_number(self):
        return self.number

mainObj = MainClass()
mainObj.set_text("Halo-o!")
mainObj.set_text()
print(mainObj.get_text())
childObj = ChildClass()
childObj.set_text("Halo-o my child!")
childObj.set_text()
childObj.set_number(1337.228007993)
childObj.set_number()
print(childObj.get_text())
print(childObj.get_number())