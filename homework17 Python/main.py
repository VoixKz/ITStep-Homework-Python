import math

class Circle:
    def __init__(self, radius):
        try:
            self.radius = radius
            if self.radius < 0:
                raise ValueError("Radius cannot be negative")
        except ValueError:
            while self.radius < 0:
                print("Radius cannot be negative")
                self.radius = float(input("Enter a positive radius: "))

    def __repr__(self):
        return f"Circle with radius - {self.radius}"

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            return Circle(self.radius + other)

    def __sub__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius - other.radius)
        else:
            return Circle(self.radius - other)

    def __iadd__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            self.radius += other
            return self

    def __isub__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius - other.radius)
        else:
            self.radius -= other
            return self

    def circumference(self):
        return f"Circumference: {2 * math.pi * self.radius}"
    
    def area(self):
        return f"Area: {math.pi * self.radius ** 2}"
    


print("1st task")
circle1 = Circle(5)
circle2 = Circle(3)
print(circle1)
print(circle2)
# circleError = Circle(-4)

print(circle1 == circle2)
print(circle1 > circle2)
print(circle1 < circle2)
print(circle1 >= circle2)
print(circle1 <= circle2)
circle3 = circle1 + circle2
print(circle3)
circle4 = circle1 - circle2
print(circle4)
circle1 += 2
print(circle1)
circle1 -= 2
print(circle2)

print(circle1.circumference())
print(circle1.area())



import re

class Complex:
    def __init__(self, re_or_str, im=0):
        if isinstance(re_or_str, str):
            match = re.match(r'^([+-]?\d+(\.\d+)?)([+-]\d+(\.\d+)?)i$', re_or_str)
            if match:
                self.re = float(match.group(1))
                self.im = float(match.group(3))
            else:
                raise ValueError("Invalid string format for Complex number")
        elif isinstance(re_or_str, (int, float)) and isinstance(im, (int, float)):
            self.re = float(re_or_str)
            self.im = float(im)
        else:
            raise ValueError("Invalid type for Complex number")

    def __str__(self):
        sign = '+' if self.im >= 0 else '-'
        return f"{self.re} {sign} {abs(self.im)}i"

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        elif isinstance(other, str):
            other_complex = Complex(other)
            return self + other_complex
        elif isinstance(other, (int, float)):
            return Complex(self.re + other, self.im)
        else:
            raise ValueError("Invalid type")

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        elif isinstance(other, str):
            other_complex = Complex(other)
            return self - other_complex
        elif isinstance(other, (int, float)):
            return Complex(self.re - other, self.im)
        else:
            raise ValueError("Invalid type")

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re * other.re - self.im * other.im,
                           self.im * other.re + self.re * other.im)
        elif isinstance(other, str):
            other_complex = Complex(other)
            return self * other_complex
        elif isinstance(other, (int, float)):
            return Complex(self.re * other, self.im * other)
        else:
            raise ValueError("Invalid type")

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.re ** 2 + other.im ** 2
            return Complex((self.re * other.re + self.im * other.im) / denominator,
                           (self.im * other.re - self.re * other.im) / denominator)
        elif isinstance(other, str):
            other_complex = Complex(other)
            return self / other_complex
        elif isinstance(other, (int, float)):
            return Complex(self.re / other, self.im / other)
        else:
            raise ValueError("Invalid type")



print()
print("2nd task")
c1 = Complex(3, 2)
c2 = Complex("1+7i")
print(c1)
print(c2)

print(f"Сложение: {c1 + c2}")
print(f"Сложение: {c1 + '5-2i'}")
print(f"Вычитание: {c1 - c2}")
print(f"Вычитание: {c1 - '3-8i'}")
print(f"Умножение: {c1 * c2}")
print(f"Умножение: {c1 * '2+3i'}")
print(f"Деление: {c1 / c2}")
print(f"Деление: {c1 / '-2-3i'}")
print(f"Умножение на скаляр: {c1 * 2}")
print(f"Деление на скаляр: {c1 / 2}")



class Airplane:
    def __init__(self, model: str, max_passengers: int):
        try:
            self.model = model
            self.max_passengers = max_passengers
            self.current_passengers = 0
        except:
            print("Invalid input")
        while self.max_passengers < 0:
            print("Max passengers cannot be negative")
            self.max_passengers = int(input("Enter a positive number of passengers: "))
        while self.current_passengers < 0:
            print("Current passengers cannot be negative")
            self.current_passengers = int(input("Enter a positive number of passengers: "))
        if self.current_passengers > self.max_passengers:
            print("Current passengers cannot be more than max passengers")
            print(f"We need to throw out {self.current_passengers - self.max_passengers} passengers")
            self.current_passengers = self.max_passengers
    
    def __str__(self) -> str:
        return f"Airplane {self.model} with {self.current_passengers} passengers on board"
    
    def __eq__(self, other):
        if not isinstance(other, Airplane):
            return "Can not compare or manipulate with different objects"
        return self.model == other.model

    def __add__(self, other):
        if isinstance(other, int):
            self.current_passengers += other
            if self.current_passengers > self.max_passengers:
                raise ValueError("Количество пассажиров не может превышать максимальное количество")
            return self
        else:
            return "Can not compare or manipulate with different objects"

    def __sub__(self, other):
        if isinstance(other, int):
            self.current_passengers -= other
            if self.current_passengers < 0:
                raise ValueError("Количество пассажиров не может быть отрицательным")
            return self
        else:
            return "Can not compare or manipulate with different objects"

    def __iadd__(self, other):
        if isinstance(other, int):
            self.current_passengers += other
            if self.current_passengers > self.max_passengers:
                raise ValueError("Количество пассажиров не может превышать максимальное количество")
            return self
        else:
            return "Can not compare or manipulate with different objects"

    def __isub__(self, other):
        if isinstance(other, int):
            self.current_passengers -= other
            if self.current_passengers < 0:
                raise ValueError("Количество пассажиров не может быть отрицательным")
            return self
        else:
            return "Can not compare or manipulate with different objects"

    def __gt__(self, other):
        if not isinstance(other, Airplane):
            return "Can not compare or manipulate with different objects"
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        if not isinstance(other, Airplane):
            return "Can not compare or manipulate with different objects"
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        if not isinstance(other, Airplane):
            return "Can not compare or manipulate with different objects"
        return self.max_passengers <= other.max_passengers

    def __ge__(self, other):
        if not isinstance(other, Airplane):
            return "Can not compare or manipulate with different objects"
        return self.max_passengers >= other.max_passengers
    


print()
print("3rd task")
airplane1 = Airplane("Boeing 747", 500)
airplane2 = Airplane("Airbus A380", 800)
print(airplane1)
print(airplane2)
airplane1 += 100
print(airplane1)
airplane1 -= 50
print(airplane1)
airplane2 += 200
print(airplane2)

airplane3 = airplane1 + 50
print(airplane3)
airplane4 = airplane1 - airplane2
print(airplane4)
print(airplane1 == airplane2)
print(airplane1 > airplane2)
print(airplane1 < airplane2)
print(airplane1 >= airplane2)
print(airplane1 <= airplane2)



class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price
        if area < 0:
            raise ValueError("Area cannot be negative")
        if price < 0:
            raise ValueError("Price cannot be negative")

    def __eq__(self, other):
        if not isinstance(other, Flat):
            return "Can not compare or manipulate with different objects"
        return self.area == other.area

    def __ne__(self, other):
        if not isinstance(other, Flat):
            return "Can not compare or manipulate with different objects"
        return self.area != other.area

    def __gt__(self, other):
        if not isinstance(other, Flat):
            return "Can not compare or manipulate with different objects"
        return self.price > other.price

    def __lt__(self, other):
        if not isinstance(other, Flat):
            return "Can not compare or manipulate with different objects"
        return self.price < other.price

    def __ge__(self, other):
        if not isinstance(other, Flat):
            return "Can not compare or manipulate with different objects"
        return self.price >= other.price

    def __le__(self, other):
        if not isinstance(other, Flat):
            return "Can not compare or manipulate with different objects"
        return self.price <= other.price
    


print()
print("4th task")
flat1 = Flat(100, 100000)
flat2 = Flat(120, 150000)
print(flat1 == flat2)
print(flat1 != flat2)
print(flat1 > flat2)
print(flat1 < flat2)
print(flat1 >= flat2)
print(flat1 <= flat2)



class Roman:
    roman_numerals = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        'M': 1000
    }

    def __init__(self, roman):
        self.roman = roman
        self.value = Roman.to_arabic(roman)
        if not roman:
            raise ValueError("Empty string")
        if not re.match(r'^[IVXLCDM]+$', roman):
            raise ValueError("Invalid roman number")
        
    def __str__(self):
        return self.roman

    @staticmethod
    def to_arabic(roman):
        i = 0
        num = 0
        while i < len(roman):
            if i+1 < len(roman) and roman[i:i+2] in Roman.roman_numerals:
                num += Roman.roman_numerals[roman[i:i+2]]
                i += 2
            else:
                num += Roman.roman_numerals[roman[i]]
                i += 1
        return num

    @staticmethod
    def to_roman(num):
        result = ''
        for symbol, value in sorted(Roman.roman_numerals.items(), key=lambda x: x[1], reverse=True):
            while num >= value:
                result += symbol
                num -= value
        return result

    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(Roman.to_roman(self.value + other.value))
        elif isinstance(other, int):
            return Roman(Roman.to_roman(self.value + other))
        else:
            return "Can not compare or manipulate with different objects"

    def __sub__(self, other):
        if isinstance(other, Roman):
            result = self.value - other.value
            if result <= 0:
                raise ValueError("Результат вычитания римских чисел не может быть нулем или отрицательным")
            return Roman(Roman.to_roman(result))
        elif isinstance(other, int):
            result = self.value - other
            if result <= 0:
                raise ValueError("Результат вычитания римского числа не может быть нулем или отрицательным")
            return Roman(Roman.to_roman(result))
        else:
            return "Can not compare or manipulate with different objects"

    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(Roman.to_roman(self.value * other.value))
        elif isinstance(other, int):
            return Roman(Roman.to_roman(self.value * other))
        else:
            return "Can not compare or manipulate with different objects"

    def __truediv__(self, other):
        if isinstance(other, Roman):
            result = self.value // other.value
            if result <= 0:
                raise ValueError("Результат деления римских чисел не может быть нулем или отрицательным")
            return Roman(Roman.to_roman(result))
        elif isinstance(other, int):
            result = self.value // other
            if result <= 0:
                raise ValueError("Результат деления римского числа не может быть нулем или отрицательным")
            return Roman(Roman.to_roman(result))
        else:
            return "Can not compare or manipulate with different objects"
        


print()
print("5th task")
roman1 = Roman("XV")
roman2 = Roman("IX")
print(roman1)
print(roman2)

print(f"Сложение: {roman1 + roman2}")
print(f"Сложение: {roman1 + 20}")
print(f"Вычитание: {roman1 - roman2}")
print(f"Вычитание: {roman1 - 10}")
print(f"Умножение: {roman1 * roman2}")
print(f"Умножение: {roman1 * 5}")
print(f"Деление: {roman1 / roman2}")
print(f"Деление: {roman1 / 2}")